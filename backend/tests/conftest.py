import pytest
import asyncio
from app.database.session import engine
from app.database.base import Base
import app.models  # Ensures all models are registered

@pytest.fixture(scope="session", autouse=True)
def initialize_test_database():
    """Initializes tables in the SQLite database before running tests."""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    async def _create_tables():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
            
    loop.run_until_complete(_create_tables())
    yield
    loop.close()
