import os


BASE_STORAGE = "storage"


def ensure_dir(path: str):
    """
    Papkani tekshiradi, bo‘lmasa yaratadi.
    """
    os.makedirs(path, exist_ok=True)
    return path


def owner_base(owner_id: int):
    """
    Owner uchun asosiy papka.
    """
    path = os.path.join(BASE_STORAGE, f"owner_{owner_id}")
    return ensure_dir(path)


def bot_base(owner_id: int, bot_id: int):
    """
    Bot uchun asosiy papka.
    """
    path = os.path.join(
        BASE_STORAGE,
        "sessions",
        f"owner_{owner_id}",
        f"bot_{bot_id}"
    )
    return ensure_dir(path)


def tdata_base(owner_id: int, bot_id: int):
    """
    Bot t_data asosiy papkasi.
    """
    path = os.path.join(
        BASE_STORAGE,
        "tdata",
        f"owner_{owner_id}",
        f"bot_{bot_id}"
    )
    return ensure_dir(path)


def session_path(owner_id: int, bot_id: int, user_id: int):
    """
    Session fayl yo‘li.
    """
    base = bot_base(owner_id, bot_id)
    return os.path.join(base, f"user_{user_id}")


def tdata_path(owner_id: int, bot_id: int, user_id: int):
    """
    t_data papkasi yo‘li.
    """
    base = tdata_base(owner_id, bot_id)
    return os.path.join(base, f"user_{user_id}")


def tdata_zip_path(owner_id: int, bot_id: int, user_id: int):
    """
    t_data zip fayl yo‘li.
    """
    base = tdata_base(owner_id, bot_id)
    return os.path.join(base, f"user_{user_id}.zip")
