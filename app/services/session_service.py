from sqlalchemy import select
from app.db.database import SessionLocal
from app.db.models import Session


async def save_session(bot_id, user_id, path):
    async with SessionLocal() as db:

        result = await db.execute(
            select(Session).where(
                Session.botId == bot_id,
                Session.userId == user_id
            )
        )
        existing = result.scalar()

        if existing:
            existing.path = path
        else:
            db.add(
                Session(
                    botId=bot_id,
                    userId=user_id,
                    path=path
                )
            )

        await db.commit()
