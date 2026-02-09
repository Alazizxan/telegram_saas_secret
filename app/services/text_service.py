from sqlalchemy import select
from app.db.database import SessionLocal
from app.db.models import Bot, BotText, TemplateText


async def get_text(bot_id: int, key: str):
    async with SessionLocal() as db:

        # 1. Avval botning o‘z textini tekshiramiz
        result = await db.execute(
            select(BotText.text).where(
                BotText.botId == bot_id,
                BotText.key == key
            )
        )
        bot_text = result.scalar()

        if bot_text:
            return bot_text

        # 2. Botdan templateId olamiz
        result = await db.execute(
            select(Bot.templateId).where(Bot.id == bot_id)
        )
        template_id = result.scalar()

        if not template_id:
            return "Text not set"

        # 3. Template textni olamiz
        result = await db.execute(
            select(TemplateText.text).where(
                TemplateText.templateId == template_id,
                TemplateText.key == key
            )
        )
        template_text = result.scalar()

        return template_text or "Text not set"
