from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
from data.config import settings


class menu_cd(CallbackData, prefix="show_menu"):
    level: int = 0
    sheet_id: int = 0
    category: str = ""
    row_id: int = 0


def start_keyboard() -> InlineKeyboardMarkup:
    markup = InlineKeyboardBuilder()
    list_buttons = list(settings.worksheet_ids.keys())
    buttons = []
    for name in list_buttons:
        buttons.append(
            InlineKeyboardButton(
                text=name,
                callback_data=menu_cd(
                    level=1,
                    sheet_id=settings.worksheet_ids[name][0]
                ).pack()
            )
        )
    markup.row(*buttons, width=1)
    return markup.as_markup()
