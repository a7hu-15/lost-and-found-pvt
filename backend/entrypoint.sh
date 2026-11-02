#!/bin/sh
set -e

echo "=== Starting ReFynd Backend Initialization ==="

# Wait for PostgreSQL database if configured
if [ -n "$DATABASE_URL" ] && echo "$DATABASE_URL" | grep -q "postgres"; then
    echo "Waiting for PostgreSQL database to be reachable..."
    python -c "
import asyncio, sys
from sqlalchemy.ext.asyncio import create_async_engine
from app.core.config import settings

async def wait_for_db():
    engine = create_async_engine(settings.DATABASE_URL)
    for attempt in range(1, 31):
        try:
            async with engine.connect() as conn:
                print('Database connection established successfully!')
                return
        except Exception as e:
            print(f'Attempt {attempt}/30: Database not ready yet ({e}). Retrying in 2 seconds...')
            await asyncio.sleep(2)
    print('Error: Database connection timed out.')
    sys.exit(1)

asyncio.run(wait_for_db())
"
fi

echo "Running database schema initialization (init_db.py)..."
python init_db.py

echo "Verifying / Seeding Admin Account (update_admin.py)..."
python update_admin.py || true

echo "=== Starting FastAPI Server (uvicorn) on 0.0.0.0:8000 ==="
exec uvicorn app.main:app --host 0.0.0.0 --port 8000

