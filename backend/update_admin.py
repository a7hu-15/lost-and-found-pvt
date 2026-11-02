import asyncio
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from sqlalchemy import select
from app.database.session import AsyncSessionLocal
from app.models.user import User, UserRole
from app.security.passwords import get_password_hash

async def main():
    admin_email = "cloudlostfound.admin@gmail.com"
    new_password = "Bheda15@"

    async with AsyncSessionLocal() as session:
        result = await session.execute(select(User).where(User.email == admin_email))
        admin = result.scalars().first()
        
        if not admin:
            result = await session.execute(select(User).where(User.role == UserRole.ADMIN_OWNER))
            admin = result.scalars().first()

        if admin:
            admin.email = admin_email
            admin.hashed_password = get_password_hash(new_password)
            admin.is_active = True
            admin.is_verified = True
            admin.mfa_enabled = False
            admin.mfa_secret = None
            await session.commit()
            print(f"Updated password and reset MFA for admin {admin_email}")
        else:
            admin = User(
                email=admin_email,
                full_name="Admin Owner",
                hashed_password=get_password_hash(new_password),
                role=UserRole.ADMIN_OWNER,
                permissions={},
                is_active=True,
                is_verified=True,
                mfa_enabled=False,
                mfa_secret=None
            )
            session.add(admin)
            await session.commit()
            print(f"Created admin user {admin_email} with specified password")

if __name__ == "__main__":
    asyncio.run(main())
