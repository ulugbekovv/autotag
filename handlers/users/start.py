from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default import main_menu
from loader import dp
from states.states import MainState


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message):
    await message.answer("👋")
    await message.answer(f"👋Приветствую! Этот бот поможет вам генерировать картинки автономеров! Это может быть полезно, для вставки картинки вашего автономера в блог, форумы или же просто для интереса!\n\n<b><i>❗️Примечание: В боте пока что поддерживается генерация только Российских автономеров. В дальнейшем планируется добавить и другие страны!🇷🇺</i></b>")
    await message.answer("Выберите тип автономера: ", reply_markup=main_menu.main_menu)
    await MainState.type.set()