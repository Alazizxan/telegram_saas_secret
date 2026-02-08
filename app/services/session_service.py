from app.db.database import SessionLocal
from app.db.models import Session

async def save_session(bot_id, user_id, path):
    async with SessionLocal() as db:
        db.add(Session(bot_id=bot_id, user_id=user_id, path=path))
        await db.commit()
