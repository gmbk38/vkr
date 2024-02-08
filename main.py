from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, state
from aiogram.types import BotCommand

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types.message import ContentType

import asyncio
from config import BOT_TOKEN

# Создаем экземпляр класса бота
bot = Bot(token=BOT_TOKEN)
# Создаем экземпляр класса диспетчера
dp = Dispatcher(bot, storage=MemoryStorage())
 
# Состояния FSM
class UserState(state.StatesGroup):
    value = state.State()
    companies = state.State()

# Обработчик команды /start
@dp.message_handler(Command('start'))
async def start(message: types.Message, state: FSMContext):
    # Получаем уникальный идентификатор пользователя
    user_id = message.from_user.id

    async with state.proxy() as data:
        # Получаем значение из состояния
        value = data.get('value', 'Значение не установлено')

    await bot.send_message(user_id, f"Текущее значение: {value}")

# Обработчик команды /value
@dp.message_handler(Command('value'))
async def set_value(message: types.Message, state: FSMContext):
    # Получаем уникальный идентификатор пользователя
    user_id = message.from_user.id

    # Устанавливаем состояние value
    await UserState.value.set()

    # Сохраняем идентификатор пользователя и состояние value
    async with state.proxy() as data:
        data['user'] = user_id

    await message.reply("Пожалуйста, введите новое значение.")

# Обработчик числовых сообщений
@dp.message_handler(state=UserState.value, content_types=types.ContentTypes.TEXT)
async def process_value(message: types.Message, state: FSMContext):
    # Получаем уникальный идентификатор пользователя
    user_id = message.from_user.id

    async with state.proxy() as data:
        # Сохраняем введенное значение в состоянии
        data['value'] = message.text

    await state.finish()
    await message.reply("Значение успешно установлено.")

# Запускаем бота
if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, reset_webhook=True)
