from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def gender():
    keyboard = InlineKeyboardMarkup(row_width=2)
    male_button = InlineKeyboardButton(text="Мужской", callback_data="c_gender_male")
    female_button = InlineKeyboardButton(text="Женский", callback_data="c_gender_female")
    keyboard.add(male_button, female_button)
    return keyboard