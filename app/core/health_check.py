import asyncio
from app.db.database import engine

async def health_check():
    while True:
        try:
            async with engine.connect():
                pass
        except:
            print("DB error")
        await asyncio.sleep(10)
