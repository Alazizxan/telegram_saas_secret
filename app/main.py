import asyncio
from app.core.bot_manager import start_all_bots
from app.core.login_queue import worker
from app.core.health_check import health_check

async def main():
    asyncio.create_task(worker())
    asyncio.create_task(health_check())
    await start_all_bots()

if __name__ == "__main__":
    asyncio.run(main())
