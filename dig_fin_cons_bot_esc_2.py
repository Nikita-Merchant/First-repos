# Импортируем библиотеку асинхронности - без нее боты не делаются.
import asyncio
# Импортируем нужные запчасти из библиотеки Айограм - на ней пишут ТГ-ботов. Версия Пайтона 3.10. Версия Айограмма 2.25.1. Версии - это важно!
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
# Импортируем запчасти для создания клавиатуры для бота
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Сохраняем токен бота, без него магия управления ботом не случиться. Токен можно получить в Фазер-Боте.
api = 'Токен'
# Создаем сущность нашего бота.
bot = Bot(token=api)
# Создаем сущность Диспетчера, через которого будем управлять ботом.
disp = Dispatcher(bot, storage=MemoryStorage())

# Создаем виртуальную клавиатуру для бота
kl = ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = KeyboardButton(text = 'Описание проекта')
button_2 = KeyboardButton(text = 'Дополнительные материалы')
button_3 = KeyboardButton(text = 'Контакты проекта')
kl.row(button_1, button_2, button_3)  # Добавляем обе кнопки в одну строку

# Прописываем команду старта, закидываем ее в диспетчера, используя декоратор Месседж-хэндлер.
@disp.message_handler(commands=['start'])
async def starter(message):
    await message.answer('Привет! Я - бот, который расскажет о проекте "Цифровой финансовый советник"!\n', reply_markup=kl)

@disp.message_handler(text = ['Описание проекта'])
# Прописываем ответное сообщение по краткой вводной о проекте.
async def giver_def(message):
    await message.answer('Проект "Цифровой финансовый советник" оформился на JPTF 2024.\n'
                         'Это - новое приложение для аналитики в сфере личных финансов.\n'
                         'Стадия готовности:\n'
                         '- сформулирована концепция проекта; \n'
                         '- для продвижения проекта функционирует ТГК - @digital_fin_consiliere;\n'
                         '-  ведётся подготовка к разработке прототипа проекта. '
                         )

@disp.message_handler(text = ['Дополнительные материалы'])
# Прописываем ответное сообщение по доп-материалам о проекте.
async def giver_more(message):
    await message.answer('С презентацией по проекту можно ознакомиться по ссылке: https://t.me/digital_fin_consiliere/17 \n'
                         'С докладом по проекту можно ознакомиться по ссылке: https://t.me/digital_fin_consiliere/19 \n'
                         'С графической архитектурой проекта можно ознакомитсья по ссылке: https://t.me/digital_fin_consiliere/31 \n'
                         'С дизайн-эскизами приложения можно ознакомитсья по ссылке: https://t.me/digital_fin_consiliere/21 \n'
                         'С резюме проекта можно ознакомиться в публикации НСПК (пункт 15): https://t.me/digital_fin_consiliere/3 \n')


@disp.message_handler(text = ['Контакты проекта'])
# Прописываем ответное сообщение по контактам для обратной связи.
async def giver_cont(message):
    await message.answer('Контакты для связи по проекту: '
                         '@N_Mashykov - ответственный за обратную связь в Телеграмме,'
                         'dig_fin_cons@mail.ru - почта для направления материалов.')

@disp.message_handler()
# Прописываем ответное сообщение на нестандартные запросы.
async def butler(message):
    await message.answer('Введите команду /start, чтобы начать общение.')

# Инициируем работу диспетчера нашего бота через объект класса Экзекутор и команды Старт-поллинг к нему.
if __name__ == '__main__':
    executor.start_polling(disp, skip_updates=True)