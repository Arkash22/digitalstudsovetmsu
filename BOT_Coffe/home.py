import sys
from os.path import dirname, join, abspath
from telebot import types
import settings


# ------------------------------------------------
def home():  # первое сообщение при неполной регистрации
    keyboard_home = types.InlineKeyboardMarkup()

    key_1 = types.InlineKeyboardButton(text='\U0001F50E Coffee Friend', callback_data='go_coffee')
    key_2 = types.InlineKeyboardButton(text='\U0001F4CB Моя Анкета', callback_data='my_anketa')
    key_3 = types.InlineKeyboardButton(text='\U0000260E Контакты', callback_data='contacts')
    key_4 = types.InlineKeyboardButton(text='\U00002139 О Боте', callback_data='info_bot')

    keyboard_home.add(key_1)
    keyboard_home.add(key_2)
    keyboard_home.add(key_3, key_4)

    return keyboard_home


# ------------------------------------------------
def home_back():  # клавиатура "назад"
    keyboard_reg_back = types.InlineKeyboardMarkup()
    key_back = types.InlineKeyboardButton(text='\U00002B05', callback_data='back_home')
    keyboard_reg_back.add(key_back)

    return keyboard_reg_back


def go_coffee():
    keyboard = types.InlineKeyboardMarkup()
    key_back = types.InlineKeyboardButton(text='\U00002B05', callback_data='back_home')
    keyboard.add(key_back)

    msg = "Я начал искать тебе Coffee Friend'а \U00002615, но это может быть не быстро, так что пока потусуйся в гордом одиночестве, а как только, я кого-нибудь найду -  я дам тебе знать \U0001F609"

    return keyboard, msg


# def msg_coffee(tg_name, inst, info, gender, status):
#     msg = f'Предлагаю тебе встретиться с @{tg_name}\nИнстаграм вот -  @{inst}\nО себе: {info}\nПол: {gender}\nСтатус: {status}'
#     return msg


# print(msg_coffee('', '', '', '', 3))


def msg_random_friend(firstname, gender, age, status, instagram, info, tg_name):
    keyboard_1 = types.InlineKeyboardMarkup()
    key_1 = types.InlineKeyboardButton(text=f'{firstname}',
                                       url='https://t.me/{}'.format(tg_name))
    key_back = types.InlineKeyboardButton(text='\U00002B05', callback_data='back_home_no_edit')
    keyboard_1.add(key_1)
    keyboard_1.add(key_back)

    if firstname is None:
        name = 'Пользователь'
    else:
        name = "<a href='https://t.me/{}/'>{}</a>".format(tg_name, firstname)
    if gender is None or gender == 404:
        gender = 'Деревянный'
    if age is None:
        age = 'между 17 и 39'
    else:
        age = str(age) + ' лет'
    if status is None or status == 404:
        status = '\U0001F6AB'

    if instagram is None or instagram == 'Null':
        inst = '\U0001F6AB'
    elif instagram == 'Not_user':
        inst = 'Нет инстаграмма!'
    else:
        p = instagram.split('@')
        inst = "<a href='https://www.instagram.com/{}/'>{}</a>".format(p[1], instagram)

    if info is None:
        info = '\U0001F6AB'

    msg1 = f'Я нашёл тебе КофеФренда.\nПознакомься, это {name}'
    msg2 = f'Я кое-кого нашёл для тебя\n.\n.\n.\nСходи с {name} на \U00002615\U00002615\U00002615'

    msg3 = '<code>\U000000AE Coffee Friend MSU</code>     \U00002615\n\n\n\n' \
           f'<i><b>\U0001F538 Имя:  </b></i>{name}\n' \
           f'<i><b>\U0001F538 Пол:  </b></i>{gender}\n' \
           f'<i><b>\U0001F538 Возраст:  </b></i>{age}\n' \
           f'<i><b>\U0001F538 Статус:  </b></i>{status}\n' \
           f'<i><b>\U0001F538 Инстаграм:  </b></i>{inst}\n' \
           f'<i><b>\U0001F538 Информация о себе:  </b></i> {info}\n\n\n\n\n' \
           f'<code>Не стоит ждать первого шага от собеседника, напиши первым(ой)!</code> '

    return msg1, msg2, msg3, keyboard_1


def msg_is_not_username():  # cообщение, если у пользователя нет tg_username
    keyboard = types.InlineKeyboardMarkup()

    key_1 = types.InlineKeyboardButton(text='Обновить данные', callback_data='refresh_tg_name')
    # key_2 = types.InlineKeyboardButton(text='Прочитать инструкцию', url='ссылка')
    key_back = types.InlineKeyboardButton(text='\U00002B05', callback_data='back_home')

    keyboard.add(key_1)
    # keyboard.add(key_2)
    keyboard.add(key_back)

    msg = 'У тебя нет Telegram username'

    return keyboard, msg


def time_block_text():
    keyboard = types.InlineKeyboardMarkup()
    key_back = types.InlineKeyboardButton(text='\U00002B05', callback_data='back_home')
    keyboard.add(key_back)

    msg = 'Чтобы искать собеседников нужно немного подождать! Ты можешь искать КофеФренда <b>раз в три дня</b>. Так ' \
          'что ' \
          'советуем не медлить и выпить \U00002615 с предложенным кандидатом.'

    return keyboard, msg
