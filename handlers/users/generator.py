from aiogram import types
from states.states import MainState
from loader import dp
import re
from aiogram.dispatcher import FSMContext
from keyboards.inline import inline
from keyboards.default import main_menu
from handlers.users.start import bot_start


async def replace_russian_with_english(text):
    russian_letters = {'у': 'y', 'р': 'p', 'о': 'o', 'н': 'n', 'е': 'e', 'к': 'k', 'а': 'a', 'т': 't', 'и': 'i', 'с': 'c', 'в': 'b', 'м': 'm', 'х': 'x'}
    for russian, english in russian_letters.items():
        text = text.replace(russian, english)
    return text


def check_def(car_number):
    pattern = r'^[А-Я]{1}\d{3}[А-Я]{2}\d{2,3}$'

    if re.match(pattern, car_number):
        return True
    else:
        return False


def check_cop(car_number):
    pattern = r'^[А-Я]\d{4}[А-Я]{2}\d{2,3}$'

    if re.match(pattern, car_number):
        return True
    else:
        return False


@dp.message_handler(state=MainState.type)
async def typemsg(message: types.Message, state: FSMContext):
    type = message.text
    if type == '‍👨‍💼Стандартный':
        await message.answer("Отлично, теперь отправьте автономер в виде текста\n\n<b><i>Пример:</i></b> А001МР97", reply_markup=main_menu.cancel)
        await MainState.number_def.set()
    if type == '👮‍♂️Полиция':
        await message.answer("Отлично, теперь отправьте автономер в виде текста\n\n<b><i>Пример:</i></b> А000177", reply_markup=main_menu.cancel)
        await MainState.number_cop.set()
    if type == '💼Дипломаты':
        await message.answer("Отлично, теперь отправьте автономер в виде текста\n\n<b><i>Пример:</i></b> 001CD177", reply_markup=main_menu.cancel)
        await MainState.number_dip.set()
    if type == '🎖Военные':
        await message.answer("Отлично, теперь отправьте автономер в виде текста\n\n<b><i>Пример:</i></b> 0001мо77", reply_markup=main_menu.cancel)
        await MainState.number_voe.set()


@dp.message_handler(text="❌ Отменить", state="*")
async def cancelo(message: types.Message, state: FSMContext):
    await state.finish()
    await bot_start(message)


@dp.message_handler(state=MainState.number_def)
async def numsg(message: types.Message, state: FSMContext):
    num = message.text
    correct = check_def(num)
    try:
        num = message.text.lower()
        num = await replace_russian_with_english(num)
        link = f'https://migalki.net/informer/1/800/{num}.png'
        await message.answer_photo(link, caption="<b><i>🤙Результат!\n\n😇Готово! Вот сгенерированный автономер. Оцените результат!</i></b>", reply_markup=inline.rate)
        await state.finish()
    except:
        await message.answer("Неправильный формат автономера! Следуйте формату: А001МР97")


@dp.message_handler(state=MainState.number_cop)
async def numsg(message: types.Message, state: FSMContext):
    num = message.text
    correct = check_cop(num)
    try:
        num = message.text.lower()
        num = await replace_russian_with_english(num)
        link = f'https://migalki.net/informer/2/800/{num}.png'
        await message.answer_photo(link, caption="<b><i>🤙Результат!\n\n😇Готово! Вот сгенерированный автономер. Оцените результат!</i></b>", reply_markup=inline.rate)
        await state.finish()
    except:
        await message.answer("Неправильный формат автономера! Следуйте формату: А000177")


@dp.message_handler(state=MainState.number_dip)
async def numsg(message: types.Message, state: FSMContext):
    try:
        num = message.text.lower()
        link = f'https://migalki.net/informer/3/800/{num}.png'
        await message.answer_photo(link, caption="<b><i>🤙Результат!\n\n😇Готово! Вот сгенерированный автономер. Оцените результат!</i></b>", reply_markup=inline.rate)
        await state.finish()
    except:
        await message.answer("Неправильный формат автономера! Следуйте формату: 001CD177")


@dp.message_handler(state=MainState.number_voe)
async def numsg(message: types.Message, state: FSMContext):
    try:
        num = message.text.lower()
        num = await replace_russian_with_english(num)
        link = f'https://migalki.net/informer/4/800/{num}.png'
        await message.answer_photo(link, caption="<b><i>🤙Результат!\n\n😇Готово! Вот сгенерированный автономер. Оцените результат!</i></b>", reply_markup=inline.rate)
        await state.finish()
    except:
        await message.answer("Неправильный формат автономера! Следуйте формату: 0001мо77")

