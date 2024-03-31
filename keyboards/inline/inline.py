from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

rate = InlineKeyboardMarkup(row_width=2)
ok = InlineKeyboardButton(text="👍", callback_data='rate_ok')
bad = InlineKeyboardButton(text="👎", callback_data='rate_bad')
rate.row(ok, bad)