from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_kb():
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="📱 Login")]],
        resize_keyboard=True
    )
