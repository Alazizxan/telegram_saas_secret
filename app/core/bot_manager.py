import asyncio
from aiogram import Bot, Dispatcher
from sqlalchemy import select
from app.db.database import SessionLocal
from app.db.models import Bot as BotModel
from app.core.supervisor import supervise

async def load_bots():
    async with SessionLocal() as session:
        result = await session.execute(
            select(BotModel).where(BotModel.is_active == True)
        )
        return result.scalars().all()

async def start_bot(bot):
    bot_obj = Bot(bot.token)
    dp = Dispatcher()

    from app.handlers.auth import register_handlers
    register_handlers(dp, bot.id, bot.owner_id)

    await dp.start_polling(bot_obj)

async def start_all_bots():
    bots = await load_bots()
    tasks = [supervise(lambda b=bot: start_bot(b)) for bot in bots]
    await asyncio.gather(*tasks)
