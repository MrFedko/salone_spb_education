from aiogram.types import CallbackQuery, Message
from typing import Union
from data.lexicon import lexicon
from .keyboards import start_keyboard


async def list_start_menu(message: Union[CallbackQuery, Message], **kwargs):
    text = lexicon["/start"].format(name=message.from_user.first_name)
    markup = start_keyboard()

    if isinstance(message, Message):
        await message.answer(text, reply_markup=markup)

    elif isinstance(message, CallbackQuery):
        call = message
        await call.message.edit_text(text, reply_markup=markup)
