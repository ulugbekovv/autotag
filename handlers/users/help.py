from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    await message.answer(f"👋Приветствую! Этот бот поможет вам генерировать картинки автономеров! Это может быть полезно, для вставки картинки вашего автономера в блог, форумы или же просто для интереса!\n\n<b><i>❗️Примечание: В боте пока что поддерживается генерация только Российских автономеров. В дальнейшем планируется дрбавить и другие страны!🇷🇺</i></b>")
