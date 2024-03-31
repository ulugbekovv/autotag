from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.row("‍👨‍💼Стандартный", "👮‍♂️Полиция").row("💼Дипломаты", "🎖Военные")


cancel = ReplyKeyboardMarkup(resize_keyboard=True)
cancel.row("❌ Отменить")