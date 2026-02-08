from telethon import TelegramClient
from app.config import API_ID, API_HASH
from app.utils.paths import session_path


async def create_client(owner_id, bot_id, user_id):
    session = session_path(owner_id, bot_id, user_id)
    client = TelegramClient(session, API_ID, API_HASH)
    await client.connect()
    return client, session
