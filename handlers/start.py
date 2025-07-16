from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from keyboards.reply_kb import start_kb, service_kb, bid
from aiogram.fsm.context import FSMContext
from filters.fsm_filters import Bid

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет! Это твой личный ассистент. "
                         "\nЯ помогу тебе выбрать услугу и передам заявку нашей команде. "
                         "\nНажми «Услуги», чтобы посмотреть, что мы предлагаем или выбери действие из меню ниже.",
                         reply_markup=start_kb())

@router.message(F.text == "Услуги")
async def cmd_services(message: Message):
    await message.answer("<b>Разработка Telegram-ботов под ключ:</b>"
                         "\n– Автоматизация заявок, рассылок, FAQ, квизов"
                         "\n– Воронки, формы, CRM-интеграции"
                         "\n<b>Создание Mini Apps (встроенных приложений в Telegram):</b>"
                         "\n– Интерфейс с кнопками, формами, каталогами"
                         "\n– Подключение к API, базам данных, платёжным системам"
                         "\n<b>Сопровождение и доработка ботов:</b>"
                         "\n– Поддержка существующих решений"
                         "\n– Рефакторинг, добавление новых функций"
                         "\n– Оптимизация скорости "
                         "\n<b>Консультации и проектирование:</b>"
                         "\n– Поможем спроектировать логику бота от А до Я под вашу задачу"
                         "\n– Оценим сложность, сроки, подскажем лучшие практики", parse_mode="html", reply_markup=bid())


@router.message(F.text == "Получить услугу")
async def get_service(message: Message, state: FSMContext):
    await state.set_state(Bid.service)
    await message.answer("<b>Выберите услугу:</b>",parse_mode="html", reply_markup=service_kb())

@router.message(Bid.service)
async def leave_leave_request(message: Message, state: FSMContext):
    await state.update_data(service=message.text)
    await state.set_state(Bid.name)
    await message.answer(text="Напишите ваше имя")

@router.message(Bid.name)
async def bid_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Bid.phone_number)
    await message.answer(text="Напишите ваш номер телефона")


@router.message(Bid.phone_number)
async def bid_phone(message: Message, state: FSMContext):
    await state.update_data(phone_number=message.text)
    data = await state.get_data()
    await message.answer(text=f"Услуга: {data['service']}\n"
                             f"Ваш номер телефона: {data['phone_number']}\n"
                             f"Ваше имя: {data['name']}", reply_markup=start_kb())
    await state.clear()
