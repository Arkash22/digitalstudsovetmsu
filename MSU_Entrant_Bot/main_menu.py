import math
import sys
from os.path import dirname, join, abspath
from telebot import types
from settings import conn, cursor

# from . import  EmojiAlphabet

sys.path.insert(0, abspath(join(dirname(__file__), '..')))


def menu():  # первое сообщение при отсутсвии регистрации
    keyboard_menu = types.InlineKeyboardMarkup()
    key_1 = types.InlineKeyboardButton(text='\U0001F393 Поступление \U0001F4DA', callback_data='entrance')
    # key_2 = types.InlineKeyboardButton(text='ДВИ \U0001F4DD', callback_data='dvi')
    # key_3 = types.InlineKeyboardButton(text='ЕГЭ \U0001F4C4', callback_data='ege')
    key_4 = types.InlineKeyboardButton(text='Ссылки на нас \U0001F50A', callback_data='links')
    key_5 = types.InlineKeyboardButton(text='\U0001F4CD Как добраться? \U0001F5FA ', callback_data='location')
    key_6 = types.InlineKeyboardButton(text='\U00002139 Приёмная Комиссия \U0001F6C2',
                                       callback_data='selection_сommittee')
    key_7 = types.InlineKeyboardButton(text='Мои данные \U0001F464', callback_data='lk')

    keyboard_menu.add(key_1)
    keyboard_menu.add(key_5)
    keyboard_menu.add(key_6)
    keyboard_menu.add(key_4, key_7)

    msg = 'Вот моё главное меню:'

    return keyboard_menu, msg


def back_to_menu():
    msg = 'Вернуться в меню:'
    keyboard_back = types.InlineKeyboardMarkup()
    key_back = types.InlineKeyboardButton(text='\U00002B05', callback_data='back_to_menu')
    keyboard_back.add(key_back)

    return keyboard_back, msg


def links():
    keyboard = types.InlineKeyboardMarkup()
    key_1 = types.InlineKeyboardButton(
        text='\U0001F64B\U0000200D\U00002640\U0000FE0F Знакомимся \U0001F64B\U0000200D\U00002642\U0000FE0F',
        url='https://t.me/entrant_msu')
    key_2 = types.InlineKeyboardButton(text='\U0001F50A Комитет по цифровому развитию \U0001F50A',
                                       url='https://vk.link/digitalstudsovetmsu')
    key_3 = types.InlineKeyboardButton(text='\U00002699 Техническая поддержка \U0001F527', url='https://t.me/AVFroym')

    key_back = types.InlineKeyboardButton(text='\U00002B05', callback_data='back_to_menu')

    keyboard.add(key_1)
    keyboard.add(key_2)
    keyboard.add(key_3)
    keyboard.add(key_back)

    msg = 'Здесь все наши друзья: '

    return keyboard, msg


def lk(username, faculty, program):
    keyboard = types.InlineKeyboardMarkup()
    key_1 = types.InlineKeyboardButton(text='\U0001F58D Изменить ФИО', callback_data='change_username')
    key_2 = types.InlineKeyboardButton(text='\U0001F393 Изменить факультет', callback_data='change_faculty')
    key_3 = types.InlineKeyboardButton(text='\U0001F4A1 Изменить Направление', callback_data='change_program')

    key_back = types.InlineKeyboardButton(text='\U00002B05', callback_data='back_to_menu')

    keyboard.add(key_1)
    keyboard.add(key_2)
    keyboard.add(key_3)
    keyboard.add(key_back)

    msg = '<b>\U0001F5C3 Вот данные о тебе:</b>\n\n' \
          '<b>ФИО</b> - <i>{}</i>\n\n' \
          '<b>Факультет</b> - <i>{}</i>\n\n' \
          '<b>Направление</b> - <i>{}</i>'.format(username, faculty, program)

    return keyboard, msg


def selection_committee():
    keyboard = types.InlineKeyboardMarkup()

    key_1 = types.InlineKeyboardButton(text='\U0001F4BC Документы', callback_data='documents')
    key_2 = types.InlineKeyboardButton(text='\U0000260E Связаться', callback_data='contacts_sc')
    key_3 = types.InlineKeyboardButton(text='\U0001F4D1 Подать документы Онлайн', url='https://webanketa.msu.ru/')
    key_back = types.InlineKeyboardButton(text='\U00002B05', callback_data='back_to_menu')

    keyboard.add(key_1, key_2)
    keyboard.add(key_3)
    keyboard.add(key_back)

    msg = '<b>Для 2021:</b>\nДаты ДВИ по математике будут опубликованы Центральной приёмной комиссией МГУ на сайте http://cpk.msu.ru ' \
          'не позднее <b>1 июня 2021 года</b>. Все внутренние экзамены в МГУ пройдут ориентировочно в период <b>с 11 июля по ' \
          '26 июля</b>, т.е. после окончания приёма документов до даты публикации ранжированных списков. '

    return keyboard, msg


def entrance():
    keyboard = types.InlineKeyboardMarkup()

    key_1 = types.InlineKeyboardButton(text='\U0001F4DA Предметы ЕГЭ', callback_data='subjects_ege')
    key_2 = types.InlineKeyboardButton(text='\U0001F4D9 Предмет ДВИ', callback_data='subjects_dvi')
    key_3 = types.InlineKeyboardButton(text='\U0001F3C5 Баллы', callback_data='tenure')
    key_4 = types.InlineKeyboardButton(text='\U0001F5C3 Материалы ДВИ', callback_data='last_year_dvi')
    key_back = types.InlineKeyboardButton(text='\U00002B05', callback_data='back_to_menu')

    keyboard.add(key_1, key_2)
    keyboard.add(key_3)
    keyboard.add(key_4)
    keyboard.add(key_back)

    msg = 'Что тебя интересует:'

    return keyboard, msg


def tenure():
    keyboard = types.InlineKeyboardMarkup()

    key_1 = types.InlineKeyboardButton(text='Бюджет', callback_data='budget')
    key_2 = types.InlineKeyboardButton(text='Платка', callback_data='paid')
    key_back = types.InlineKeyboardButton(text='\U00002B05', callback_data='entrance')

    keyboard.add(key_1, key_2)
    keyboard.add(key_back)

    msg = 'Всего мест в этом году - {}\n' \
          'Из них на бюджет - {}\n' \
          'И на платку - {}\n' \
          'Выбирай, куда хочешь поступить?'

    return keyboard, msg


def budget():
    keyboard = types.InlineKeyboardMarkup()

    key_1 = types.InlineKeyboardButton(text='Проходные баллы', callback_data='minimal_score')
    key_2 = types.InlineKeyboardButton(text='Человек на место', callback_data='people/seat')
    key_back = types.InlineKeyboardButton(text='\U00002B05', callback_data='tenure')

    keyboard.add(key_1, key_2)
    keyboard.add(key_back)

    msg = 'Что именно тебя интересует?'

    return keyboard, msg


def paid():
    keyboard = types.InlineKeyboardMarkup()

    key_1 = types.InlineKeyboardButton(text='Минимальный балл', callback_data='minimal_score')
    key_2 = types.InlineKeyboardButton(text='Стоимость обучения', callback_data='price')
    key_back = types.InlineKeyboardButton(text='\U00002B05', callback_data='tenure')

    keyboard.add(key_1, key_2)
    keyboard.add(key_back)

    msg = 'Что именно тебя интересует?'

    return keyboard, msg
