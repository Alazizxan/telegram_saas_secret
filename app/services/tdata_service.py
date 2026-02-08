import shutil
from opentele.td import TDesktop
from opentele.api import API, UseCurrentSession
from app.utils.paths import tdata_path, tdata_zip_path


async def to_tdata(client, owner_id, bot_id, user_id):
    path = tdata_path(owner_id, bot_id, user_id)

    tdesk = await TDesktop.FromTelethon(
        client,
        api=API.TelegramDesktop,
        flag=UseCurrentSession
    )

    tdesk.SaveTData(path)

    zip_name = tdata_zip_path(owner_id, bot_id, user_id)
    shutil.make_archive(zip_name.replace(".zip", ""), "zip", path)

    return zip_name
