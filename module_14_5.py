# Скачиваем код телеграмм-бота из предыдущего модуля
import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# Импортируем функцию для лобавления юзеров и проверки наличия в базе данных, а также извлечения информации из базы данных
from n_crud_functions import get_all_products, add_user, is_included

base_products = get_all_products()

api = 'Токен'
bot = Bot(token=api)
disp = Dispatcher(bot, storage=MemoryStorage())

kv = InlineKeyboardMarkup(resize_keyboard=True)
button_counter = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_formuler = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kv.row(button_counter, button_formuler)

# Апгрейдим инлайновую клавиратуру, завязывая названия кнопок на названия из каталога
kl_products = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=base_products[0][1], callback_data="product_buying"),
        InlineKeyboardButton(text=base_products[1][1], callback_data="product_buying"),
        InlineKeyboardButton(text=base_products[2][1], callback_data="product_buying"),
        InlineKeyboardButton(text=base_products[3][1], callback_data="product_buying")]
    ],
resize_keyboard=True)

kl = ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = KeyboardButton(text = 'Рассчитать')
button_2 = KeyboardButton(text = 'Информация')
kl.row(button_1, button_2)

button_buyer = KeyboardButton(text='Купить')
kl.add(button_buyer)

button_users = KeyboardButton(text='Регистрация')
kl.add(button_users)

class UserState(StatesGroup):
    age, growth, weight = State(), State(), State()

# Вводим новый класс объектов для регистрации пользователей
class RegistrationState(StatesGroup):
    username, email, age, balance = State(), State(), State(), State()

@disp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.', reply_markup=kl)

# Создаем цепочку состояний для регистрации пользователей
@disp.message_handler(text = 'Регистрация')
async def sing_up(message):
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    await RegistrationState.username.set()

@disp.message_handler(state = RegistrationState.username)
async def set_username(message, state):
    if is_included(message.text) == True:
        await message.answer('Пользователь существует, введите другое имя')
        await RegistrationState.username.set()
    else:
        await state.update_data(username = message.text)
        await message.answer('Введите свой email:')
        await RegistrationState.email.set()

@disp.message_handler(state = RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email = message.text)
    await message.answer('Введите свой возраст:')
    await RegistrationState.age.set()

@disp.message_handler(state = RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age = message.text)
    data = await state.get_data()
    add_user(data['username'], data['email'], data['age'])
    await message.answer('Регистрация прошла успешно!')
    await state.finish()

# Апгрейдим хэндлер для ввода новой инлайновой клавиатуры, завязывая сообщения на базу данных Рroducts
@disp.message_handler(text='Купить')
async def get_buying_list(message):
    for num in range(4):
        await message.answer(f'Название: {base_products[num][1]} | Описание: {base_products[num][2]} | Цена: {base_products[num][3]}')
        with open(f'prod_{base_products[num][0]}.jpg', 'rb') as jpg_: # Извлекаем картинки из той же директории, где находится наш бот
            await message.answer_photo(jpg_)
    await message.answer('Выберите продукт для покупки:', reply_markup=kl_products)

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