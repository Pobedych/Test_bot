from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def start_kb():
    kb_list = [
        [KeyboardButton(text="Услуги")]
    ]
    kb = ReplyKeyboardMarkup(keyboard=kb_list, resize_keyboard=True, one_time_keyboard=True)
    return kb


def service_kb():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Разработка Telegram-ботов под ключ")],
            [KeyboardButton(text="Создание Mini Apps")],
            [KeyboardButton(text="Сопровождение и доработка ботов")],
            [KeyboardButton(text="Консультации и проектирование")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )

def bid():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Получить услугу")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )