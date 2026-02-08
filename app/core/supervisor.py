import asyncio

async def supervise(coro):
    while True:
        try:
            await coro()
        except Exception:
            await asyncio.sleep(3)
