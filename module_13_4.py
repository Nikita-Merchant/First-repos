import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

api = 'TOKEN'
bot = Bot(token=api)
disp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age, growth, weight = State(), State(), State()

@disp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')

@disp.message_handler(text = 'Calories')
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()

@disp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(age = message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@disp.message_handler(state = UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth = message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@disp.message_handler(state = UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight = message.text)
    data = await state.get_data()
    for_man = sum([(10 * float(data['weight'])), (6.25 * float(data['growth'])), -(5 * int(data['age'])), 5])
    for_woman = sum([(10 * float(data['weight'])), (6.25 * float(data['growth'])), -(5 * int(data['age'])), -161])
    await message.answer(f'Если вы мужчина, то ваша норма составляет - {for_man} калорий.\n'
                         f'Если вы женщина, то ваша норма составляет - {for_woman} калорий. ')
    await UserState.weight.set()
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(disp, skip_updates=True)
