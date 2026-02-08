from sqlalchemy import select
from app.db.database import SessionLocal
from app.db.models import BotText

async def get_text(bot_id, key):
    async with SessionLocal() as session:
        result = await session.execute(
            select(BotText.text)
            .where(BotText.bot_id == bot_id)
            .where(BotText.key == key)
        )
        text = result.scalar()
        return text or "Text not set"
