import sys
from os.path import dirname, join, abspath
from telebot import types

sys.path.insert(0, abspath(join(dirname(__file__), '..')))
# from settings import conn, cursor
import settings


# ------------------------------------------------

def anketa(firstname, gender, age, status, instagram, info):
    keyboard = types.InlineKeyboardMarkup()
    key_1 = types.InlineKeyboardButton(text=' Изменить ФИ', callback_data='re_name')
    key_2 = types.InlineKeyboardButton(text=' Изменить Пол', callback_data='re_gender')
    key_3 = types.InlineKeyboardButton(text=' Изменить Возраст', callback_data='re_age')
    key_4 = types.InlineKeyboardButton(text=' Изменить Статус', callback_data='re_status')
    key_5 = types.InlineKeyboardButton(text=' Изменить Инстаграм', callback_data='re_inst')
    key_6 = types.InlineKeyboardButton(text=' Изменить "О себе"', callback_data='re_info')
    key_7 = types.InlineKeyboardButton(text='\U00002705 Отправить данные', callback_data='done_1')

    keyboard.add(key_1, key_2)
    keyboard.add(key_3, key_4)
    keyboard.add(key_5)
    keyboard.add(key_6)
    keyboard.add(key_7)

    if firstname is None:
        firstname = '\U0001F6AB'
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

    msg = '<code>\U000000AE Coffee Friend MSU</code>     \U00002615\n\n<i>Твоя анкета:</i>\n\n' \
          f'<i><b>\U0001F538 Имя:  </b></i>{firstname}\n' \
          f'<i><b>\U0001F538 Пол:  </b></i>{gender}\n' \
          f'<i><b>\U0001F538 Возраст:  </b></i>{age}\n' \
          f'<i><b>\U0001F538 Статус:  </b></i>{status}\n' \
          f'<i><b>\U0001F538 Инстаграм:  </b></i>{inst}\n' \
          f'<i><b>\U0001F538 Информация о себе:  </b></i> {info}\n\n\n\n\n' \
          f'<code>Если ты закончил изменять данные в свой анкете, то нажимай "Отправить данные". \nМы не просим ' \
          f'заполнять анкету полностью, ты сам(а) вправе решать, что указать в ней.</code> '

    return keyboard, msg


# print(anketa('Аркадий', 'мужской', '21', 'Студент', 'f.a.v.orite', 'ААААААА тут расскажу о себеееееееееееееееееееееееееееееееее'))

def done():
    keyboard = types.InlineKeyboardMarkup()
    key_1 = types.InlineKeyboardButton(text='\U00002705 Отправить данные', callback_data='done_2')
    key_back = types.InlineKeyboardButton(text=' << Назад', callback_data='back_anketa')
    keyboard.add(key_1, key_back)

    msg = '<i>Нажимая кнопку <b>"Отправить данные"</b>, вы принимаете соглашение, написанное в статье - <a href="https://telegra.ph/Soglashenie-ob-obrabotke-personalnyh-dannyh-05-07">Соглашение об обработке персональных данных</a></i>'

    return keyboard, msg


def my_anketa(firstname, gender, age, status, instagram, info):
    keyboard = types.InlineKeyboardMarkup()
    key_1 = types.InlineKeyboardButton(text=' Изменить ФИ', callback_data='re_name')
    key_2 = types.InlineKeyboardButton(text=' Изменить Пол', callback_data='re_gender')
    key_3 = types.InlineKeyboardButton(text=' Изменить Возраст', callback_data='re_age')
    key_4 = types.InlineKeyboardButton(text=' Изменить Статус', callback_data='re_status')
    key_5 = types.InlineKeyboardButton(text=' Изменить Инстаграм', callback_data='re_inst')
    key_6 = types.InlineKeyboardButton(text=' Изменить "О себе"', callback_data='re_info')
    key_back = types.InlineKeyboardButton(text='<< Назад', callback_data='back_home')

    keyboard.add(key_1, key_2)
    keyboard.add(key_3, key_4)
    keyboard.add(key_5)
    keyboard.add(key_6)
    keyboard.add(key_back)

    if firstname is None:
        firstname = '\U0001F6AB'
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

    msg = '<code>\U000000AE Coffee Friend MSU</code>     \U00002615\n\n\n\n' \
          f'<i><b>\U0001F538 Имя:  </b></i>{firstname}\n' \
          f'<i><b>\U0001F538 Пол:  </b></i>{gender}\n' \
          f'<i><b>\U0001F538 Возраст:  </b></i>{age}\n' \
          f'<i><b>\U0001F538 Статус:  </b></i>{status}\n' \
          f'<i><b>\U0001F538 Инстаграм:  </b></i>{inst}\n' \
          f'<i><b>\U0001F538 Информация о себе:  </b></i> {info}\n\n\n\n\n' \
          f'<code>Если ты закончил изменять данные в свой анкете, то просто вернись в главное меню по кнопке " Назад".' \
          f' \nМы не просим ' \
          f'заполнять анкету полностью, ты сам(а) вправе решать, что указать в ней.</code> '

    return keyboard, msg


def demo_anketa_1():
    keyboard = types.InlineKeyboardMarkup()
    key_1 = types.InlineKeyboardButton(text='•1•', callback_data='1_page')
    key_2 = types.InlineKeyboardButton(text='2', callback_data='2_page')
    key_3 = types.InlineKeyboardButton(text='3', callback_data='3_page')
    key_login = types.InlineKeyboardButton(text='\U0001F6AA Зарегистрироваться', callback_data='go_login')
    keyboard.add(key_1, key_2, key_3)
    keyboard.add(key_login)

    msg = '<code>\U000000AE Coffee Friend MSU</code>     \U00002615\n\n\n\n' \
          f'<i><b>\U0001F538 Имя:  </b></i> Василий Громов\n' \
          f'<i><b>\U0001F538 Пол:  </b></i> Мужской\n' \
          f'<i><b>\U0001F538 Возраст:  </b></i> 24\n' \
          f'<i><b>\U0001F538 Статус:  </b></i> Аспирант\n' \
          f'<i><b>\U0001F538 Инстаграм:  </b></i>\U0001F6AB\n' \
          f'<i><b>\U0001F538 Информация о себе:  </b></i> Я похоже самый последнйи посмотрел сериал "Игра престолов", но зато нам будет, что обсудить. Учусь на Журфаке, увлекаюсь большим тенисом.\n\n\n\n\n' \
          f'<code> Данная анкета носит исключительно демонстрационный характер, все совпадения носят случайный характер и не несут цели оскорбить автора</code> '

    return keyboard, msg

def demo_anketa_2():
    keyboard = types.InlineKeyboardMarkup()
    key_1 = types.InlineKeyboardButton(text='1', callback_data='1_page')
    key_2 = types.InlineKeyboardButton(text='•2•', callback_data='2_page')
    key_3 = types.InlineKeyboardButton(text='3', callback_data='3_page')
    key_login = types.InlineKeyboardButton(text='\U0001F6AA Зарегистрироваться', callback_data='go_login')
    keyboard.add(key_1, key_2, key_3)
    keyboard.add(key_login)

    msg = '<code>\U000000AE Coffee Friend MSU</code>     \U00002615\n\n\n\n' \
          f'<i><b>\U0001F538 Имя:  </b></i> Арина Сорокина\n' \
          f'<i><b>\U0001F538 Пол:  </b></i> Женский\n' \
          f'<i><b>\U0001F538 Возраст:  </b></i> 21\n' \
          f'<i><b>\U0001F538 Статус:  </b></i> Студентка\n' \
          f'<i><b>\U0001F538 Инстаграм:  </b></i>\U0001F6AB\n' \
          f'<i><b>\U0001F538 Информация о себе:  </b></i> По гороскопу овен, но для тебя могу стать раком \U0001F61C \n\n\n\n\n' \
          f'<code> Данная анкета носит исключительно демонстрационный характер, все совпадения носят случайный характер и не несут цели оскорбить автора</code> '

    return keyboard, msg

def demo_anketa_3():
    keyboard = types.InlineKeyboardMarkup()
    key_1 = types.InlineKeyboardButton(text='1', callback_data='1_page')
    key_2 = types.InlineKeyboardButton(text='2', callback_data='2_page')
    key_3 = types.InlineKeyboardButton(text='•3•', callback_data='3_page')
    key_login = types.InlineKeyboardButton(text='\U0001F6AA Зарегистрироваться', callback_data='go_login')
    keyboard.add(key_1, key_2, key_3)
    keyboard.add(key_login)

    msg = '<code>\U000000AE Coffee Friend MSU</code>     \U00002615\n\n\n\n' \
          f'<i><b>\U0001F538 Имя:  </b></i> Аркадий Фроймчук\n' \
          f'<i><b>\U0001F538 Пол:  </b></i> Мужской\n' \
          f'<i><b>\U0001F538 Возраст:  </b></i> 20\n' \
          f'<i><b>\U0001F538 Статус:  </b></i> Студент\n' \
          f'<i><b>\U0001F538 Инстаграм:  </b></i> <a href="https://www.instagram.com/f.a.v.orite/">@f.a.v.orite</a> \n' \
          f'<i><b>\U0001F538 Информация о себе:  </b></i> Создатель этого замечательного бота, поэтому, конечно же, не мог упустить возможность пропиарить свою инсут, кстати подпишись \U0001F446 \n\n\n\n\n' \
          f'<code> Данная анкета носит исключительно демонстрационный характер, все совпадения носят случайный характер и не несут цели оскорбить автора</code> '

    return keyboard, msg