# Скачиваем код из последнего домашнего задания 13 модуля
import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

api = 'Токен'
bot = Bot(token=api)
disp = Dispatcher(bot, storage=MemoryStorage())

kv = InlineKeyboardMarkup(resize_keyboard=True)
button_counter = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_formuler = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kv.row(button_counter, button_formuler)

# Создаем новую инлайновую клавиратуру
kl_products = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Product1", callback_data="product_buying"),
        InlineKeyboardButton(text="Product2", callback_data="product_buying"),
        InlineKeyboardButton(text="Product3", callback_data="product_buying"),
        InlineKeyboardButton(text="Product4", callback_data="product_buying")]
    ],
resize_keyboard=True)

# Создаем виртуальную клавиатуру для бота
kl = ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = KeyboardButton(text = 'Рассчитать')
button_2 = KeyboardButton(text = 'Информация')
kl.row(button_1, button_2)

# Добавляем новую кнопку в виртуальную клавиатуру из старого бота
button_buyer = KeyboardButton(text='Купить')
kl.add(button_buyer) # На представленном скриншоте кнопка строкой ниже

# Обновляем блок основной функциональности бота из предыдущего модуля
class UserState(StatesGroup):
    age, growth, weight = State(), State(), State()

@disp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kl)

# Создаем хэндлер для ввода новой инлайновой клавиатуры
@disp.message_handler(text='Купить')
async def get_buying_list(message):
    for number in range(1, 5):
        await message.answer(f'Название: Product{number} | Описание: описание {number} | Цена: {number * 100}')
        with open(f'prod_{number}.jpg', 'rb') as jpg_: # Извлекаем картинки из той же директории, где находится наш бот
            await message.answer_photo(jpg_)
    await message.answer('Выберите продукт для покупки:', reply_markup=kl_products)

# Создаем новый хэндлер для кнопок продуктов
@disp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()

@disp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kv)

@disp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161')
    await call.answer()

@disp.callback_query_handler(text = 'calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await call.answer()
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
    for_woman = sum([(10 * float(data['weight'])), (6.25 * float(data['growth'])), -(5 * int(data['age'])), -161])
    await message.answer(f'Ваша норма составляет - {for_woman} калорий. ')
    await UserState.weight.set()
    await state.finish()

@disp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(disp, skip_updates=True)