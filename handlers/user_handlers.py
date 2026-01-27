from aiogram import types, F as f, Router
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from magic_filter import F as MF

from loader import dataBase
from .keyboards import menu_cd
from .menuLists import list_start_menu, list_sheet_categories_menu, list_dishes_by_category_menu
from data.config import settings

router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message, state: FSMContext):
    await state.clear()
    await list_start_menu(message)

@router.callback_query(
    menu_cd.filter(MF.level == 0), flags={"chat_action": "typing"}
)
async def start_menu_callback(
    call: types.CallbackQuery,
    callback_data: menu_cd,
    state: FSMContext,
):
    await state.clear()
    await list_start_menu(call)
@router.callback_query(
    menu_cd.filter(MF.level == 1), flags={"chat_action": "typing"}
)
async def sheet_categories_callback(
    call: types.CallbackQuery,
    callback_data: menu_cd,
    state: FSMContext,
):
    await state.update_data(sheet_id=callback_data.sheet_id)
    categories = dataBase.get_categories(settings.db_tables[callback_data.sheet_id])
    await state.update_data(categories=categories)
    """сохраняем лист категорий в состояние, а индекс категории в callback_data"""
    await list_sheet_categories_menu(call, categories, callback_data)

@router.callback_query(
    menu_cd.filter(MF.level == 2), flags={"chat_action": "typing"}
)
async def dishes_by_category_callback(
    call: types.CallbackQuery,
    callback_data: menu_cd,
    state: FSMContext,
):
    data = await state.get_data()
    sheet_id = data.get("sheet_id")
    categories = data.get("categories")
    category_index = callback_data.category_index
    category_name = categories[category_index]
    dishes = dataBase.get_dishes_by_category(
        settings.db_tables[sheet_id], category_name
    )
    await state.update_data(dishes=dishes)
    """сохраняем лист блюд в состоянии, а индекс блюда в callback_data"""
    await list_dishes_by_category_menu(call, dishes, callback_data)
