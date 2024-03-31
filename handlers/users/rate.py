from loader import dp, bot
from aiogram import types
from keyboards.default.main_menu import main_menu
from states.states import MainState


@dp.callback_query_handler(lambda c: c.data == 'rate_ok')
async def rateok(callback: types.CallbackQuery):
    chat = callback.from_user.id
    main = await bot.send_message(chat_id=chat, text=
        f"👋Приветствую! Этот бот поможет вам генерировать картинки автономеров! Это может быть полезно, для вставки картинки вашего автономера в блог, форумы или же просто для интереса!\n\n<b><i>❗️Примечание: В боте пока что поддерживается генерация только Российских автономеров. В дальнейшем планируется добавить и другие страны!🇷🇺</i></b>")
    await bot.send_message(chat_id=chat, text="Выберите тип автономера: ", reply_markup=main_menu)
    await MainState.type.set()
    edit = main.message_id-1
    await bot.edit_message_caption(chat_id=chat, message_id=edit, caption="<b><i>🥳Рады, что результат вам понравился. Не забудьте посоветовать наш бот своим друзьям!</i></b>")


@dp.callback_query_handler(lambda c: c.data == 'rate_bad')
async def rateok(callback: types.CallbackQuery):
    chat = callback.from_user.id
    main = await bot.send_message(chat_id=chat, text=
        f"👋Приветствую! Этот бот поможет вам генерировать картинки автономеров! Это может быть полезно, для вставки картинки вашего автономера в блог, форумы или же просто для интереса!\n\n<b><i>❗️Примечание: В боте пока что поддерживается генерация только Российских автономеров. В дальнейшем планируется добавить и другие страны!🇷🇺</i></b>")
    await bot.send_message(chat_id=chat, text="Выберите тип автономера: ", reply_markup=main_menu)
    await MainState.type.set()
    edit = main.message_id-1
    await bot.edit_message_caption(chat_id=chat, message_id=edit, caption="<b><i>😕Жаль, что результат вам не понравился. Мы будем работать над этим!</i></b>")