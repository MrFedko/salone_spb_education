from aiogram import types, F as f, Router
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from .menuLists import list_start_menu

router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message, state: FSMContext):
    await state.clear()
    await list_start_menu(message)
