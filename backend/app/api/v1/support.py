import logging
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, status, Request, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.database.session import get_db
from app.models.support_ticket import SupportTicket, TicketStatus
from app.models.audit import AuditLog
from app.schemas.support import SupportTicketCreate
from app.notifications.service import send_email

logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("", status_code=status.HTTP_201_CREATED)
async def submit_support_message(
    payload: SupportTicketCreate,
    request: Request,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db)
):
    try:
        now_str = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
        client_ip = request.client.host if request.client else "Unknown"

        # 1. Store ticket in database
        ticket = SupportTicket(
            name=payload.name,
            email=payload.email,
            subject=payload.subject,
            message=payload.message,
            status=TicketStatus.OPEN,
            ip_address=client_ip
        )
        db.add(ticket)
        await db.flush()

        text_content = f"""New Support Ticket Received [{ticket.ticket_id}]

Ticket ID: {ticket.ticket_id}
Name: {payload.name}
Email: {payload.email}
Subject: {payload.subject}
Timestamp: {now_str}
Client IP: {client_ip}

Message:
{payload.message}
"""

        html_content = f"""
        <div style="font-family: sans-serif; max-width: 560px; margin: 0 auto; padding: 20px; border: 1px solid #e4e4e7; border-radius: 8px;">
          <h2 style="color: #09090b; margin-top: 0;">[{ticket.ticket_id}] {payload.subject}</h2>
          <div style="background: #f4f4f5; padding: 12px; border-radius: 6px; font-family: monospace; font-size: 12px; margin-bottom: 16px;">
            <div><strong>Ticket ID:</strong> {ticket.ticket_id}</div>
            <div><strong>From:</strong> {payload.name} (&lt;{payload.email}&gt;)</div>
            <div><strong>Time:</strong> {now_str}</div>
            <div><strong>IP:</strong> {client_ip}</div>
          </div>
          <div style="font-size: 14px; color: #27272a; line-height: 1.6; whitespace: pre-line;">
            {payload.message}
          </div>
        </div>
        """

        # 2. Dispatch email notification to SUPPORT_EMAIL (cloudlostfound.platform@gmail.com) in background
        background_tasks.add_task(
            send_email,
            to_email=settings.SUPPORT_EMAIL,
            subject=f"[Support Ticket {ticket.ticket_id}] {payload.subject}",
            body_text=text_content,
            body_html=html_content
        )

        # 3. Dispatch automated confirmation receipt to user
        user_ack_text = f"""Hello {payload.name},

Thank you for reaching out to ReFynd Support. We have received your inquiry.

Ticket ID: {ticket.ticket_id}
Subject: {payload.subject}

Our platform team has received your ticket and will respond to this email shortly.

Your Message:
{payload.message}

Best regards,
ReFynd Support Team
cloudlostfound.platform@gmail.com
"""
        user_ack_html = f"""
        <div style="font-family: sans-serif; max-width: 560px; margin: 0 auto; padding: 20px; border: 1px solid #e4e4e7; border-radius: 8px;">
          <h2 style="color: #09090b; margin-top: 0;">Support Ticket Received</h2>
          <p>Hello <strong>{payload.name}</strong>,</p>
          <p>Thank you for contacting ReFynd Support. We have received your message and our team will review it shortly.</p>
          <div style="background: #f4f4f5; padding: 12px; border-radius: 6px; font-family: monospace; font-size: 12px; margin-bottom: 16px;">
            <div><strong>Ticket ID:</strong> {ticket.ticket_id}</div>
            <div><strong>Subject:</strong> {payload.subject}</div>
          </div>
          <div style="font-size: 13px; color: #3f3f46; line-height: 1.5; border-left: 3px solid #FF8A00; padding-left: 12px; margin-bottom: 16px; white-space: pre-line;">
            {payload.message}
          </div>
          <p style="font-size: 12px; color: #71717a;">ReFynd Campus Lost &amp; Found Platform Support</p>
        </div>
        """
        background_tasks.add_task(
            send_email,
            to_email=payload.email,
            subject=f"ReFynd Support • We Received Your Message ({ticket.ticket_id})",
            body_text=user_ack_text,
            body_html=user_ack_html
        )

        # 3. Record audit log
        audit = AuditLog(
            action="SUPPORT_TICKET_SUBMITTED",
            resource="support",
            details={"ticket_id": ticket.ticket_id, "email": payload.email, "subject": payload.subject, "ip": client_ip}
        )
        db.add(audit)
        await db.commit()

        return {
            "message": "Support ticket submitted successfully.",
            "ticket_id": ticket.ticket_id
        }

    except Exception as e:
        logger.error(f"Support message delivery failed: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unable to send your message. Please try again in a few minutes."
        )
