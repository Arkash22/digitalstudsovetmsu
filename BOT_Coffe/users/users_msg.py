import sys
from os.path import dirname, join, abspath
from telebot import types

sys.path.insert(0, abspath(join(dirname(__file__), '..')))
# from settings import conn, cursor
import settings


# ------------------------------------------------
def first(name):  # первое сообщение при первом входе
    keyboard_register = types.InlineKeyboardMarkup()

    key_1 = types.InlineKeyboardButton(text='\U00002615 COFFEE FRIEND DEMO', callback_data='go_coffee_demo')
    key_2 = types.InlineKeyboardButton(text='\U0001F6AA Зарегистрироваться', callback_data='go_login')

    keyboard_register.add(key_1)
    keyboard_register.add(key_2)

    msg = f'Привет, {name}!\n\nЯ - новый бот <a href="https://t.me/studsovetmsu">Студсовета МГУ</a>, который будет ' \
          f'помогать тебе заводить новые знакомства, общаться с МГУшниками и прокачивать друг друга.'

    msg2 = '\U0001F64B\U0000200D\U00002642\U0000FE0F У нас тут принято не стесняться и кратко рассказывать о себе до ' \
           'встречи, поэтому пожалуйста пройди ' \
           '<b>"Регистрацию"</b>\n\n<i>Пс...Пока ты не зарегистрирован(а), у тебя будет ограниченная ' \
           'функциональность, сори\U0001F937\U0000200D\U00002642\U0000FE0F</i> '
    msg3 = 'Если совсем ничего не понятно, то для тебя мы подготовили демо-версию из анкет, которые могут тебе ' \
           'попасться в Coffee Friend после РЕГИСТРАЦИИ, пощёлкай там вправо-влево и мб тебе в будущем попадётся ' \
           'именно этот собеседник \U0001F609'

    return keyboard_register, msg, msg2, msg3


def first_for_no_user(name):  # первое сообщение при первом входе
    keyboard_register = types.InlineKeyboardMarkup()

    key_1 = types.InlineKeyboardButton(text='\U0001F501 Обновиться', callback_data='refresh_start')

    keyboard_register.add(key_1)

    msg = f'Привет, {name}!\n\nЯ - новый бот <a href="https://t.me/studsovetmsu">Студсовета МГУ</a>, который будет ' \
          f'помогать тебе заводить новые знакомства, общаться с МГУшниками и прокачивать друг друга.'

    msg2 = '\U000026A0 Чтобы пользоваться моим функционалом тебе необходимо иметь логин в Telegram (Username), ' \
           'пожалуйста поставь его и нажми кнопку "Обновиться"'

    return keyboard_register, msg, msg2


# ------------------------------------------------
def not_full_reg(name):  # сообщение при неполной регистрации
    keyboard = types.InlineKeyboardMarkup()

    key_1 = types.InlineKeyboardButton(text='\U0001F6AA Продолжить регистрацию', callback_data='go_login_not_all')

    keyboard.add(key_1)

    msg = f' Ооо, снова, привет, {name}!\n\nВ прошлый раз ты не закончил(а) регистрацию, так что всё ещё не можешь ' \
          f'воспользоваться всем функционалом. Думаю, тебе осталось совсем немного... '

    return keyboard, msg
