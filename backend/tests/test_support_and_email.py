import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app
from app.core.validators import validate_realistic_email

# --- Email Validation Tests ---

def test_valid_email_accepted():
    email = "valid.student@gmail.com"
    result = validate_realistic_email(email)
    assert result == "valid.student@gmail.com"

def test_oversized_gibberish_gmail_rejected():
    gibberish = "asdfaalsdfhajshdfklahjalkshdfklhadfhcjhdf2138646192364912639746asdgfgwq@gmail.com"
    with pytest.raises(ValueError) as excinfo:
        validate_realistic_email(gibberish)
    assert "Gmail" in str(excinfo.value) or "too long" in str(excinfo.value)

def test_short_gmail_username_rejected():
    short_email = "ab@gmail.com"
    with pytest.raises(ValueError) as excinfo:
        validate_realistic_email(short_email)
    assert "at least 6 characters" in str(excinfo.value)

def test_nonexistent_domain_rejected():
    fake_domain_email = "student@nonexistentfake123domain456.xyz"
    with pytest.raises(ValueError) as excinfo:
        validate_realistic_email(fake_domain_email)
    assert "undeliverable" in str(excinfo.value) or "does not exist" in str(excinfo.value)

def test_disposable_email_rejected():
    temp_email = "throwaway@mailinator.com"
    with pytest.raises(ValueError) as excinfo:
        validate_realistic_email(temp_email)
    assert "Disposable" in str(excinfo.value)

# --- Support Ticket API Tests ---

@pytest.mark.asyncio
async def test_submit_valid_support_ticket():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        payload = {
            "name": "Jane Doe",
            "email": "jane.student@gmail.com",
            "subject": "Inquiry regarding lost ID card",
            "message": "I lost my ID card yesterday near the cafeteria. Has it been handed in?"
        }
        response = await ac.post("/api/v1/support", json=payload)
        assert response.status_code == 201
        data = response.json()
        assert "ticket_id" in data
        assert data["ticket_id"].startswith("SUP-")
        assert data["message"] == "Support ticket submitted successfully."

@pytest.mark.asyncio
async def test_submit_support_ticket_invalid_email():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        payload = {
            "name": "Jane Doe",
            "email": "asdfaalsdfhajshdfklahjalkshdfklhadfhcjhdf2138646192364912639746asdgfgwq@gmail.com",
            "subject": "Testing gibberish email",
            "message": "This should be rejected because the email is invalid."
        }
        response = await ac.post("/api/v1/support", json=payload)
        assert response.status_code == 422

@pytest.mark.asyncio
async def test_submit_support_ticket_missing_fields():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        payload = {
            "name": "Jane Doe",
            "email": "jane.student@gmail.com"
            # Missing subject and message
        }
        response = await ac.post("/api/v1/support", json=payload)
        assert response.status_code == 422
