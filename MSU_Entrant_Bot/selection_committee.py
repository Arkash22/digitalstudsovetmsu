import math
import sys
from os.path import dirname, join, abspath
from telebot import types
from settings import conn, cursor

# from . import  EmojiAlphabet

sys.path.insert(0, abspath(join(dirname(__file__), '..')))



def documents():
    text_docs = '<b>Вот список всех необходимых документов:</b>\n\n' \
                '1. Паспорт, копия паспорта;\n' \
                '2. Оригинал или копия документа об образовании;\n' \
                '3. 6 фотографий размером 3х4\n' \
                '4. Заявление (заполняется в Приемной комиссии);\n' \
                '5. СНИЛС;\n' \
                '6. Результаты ЕГЭ заносятся со слов абитуриента \n'

    keyboard_back = types.InlineKeyboardMarkup()

    key_back = types.InlineKeyboardButton(text='\U00002B05', callback_data='back_to_sc')

    keyboard_back.add(key_back)

    return keyboard_back, text_docs


def contact(faculty_id):
    cursor.execute("SELECT tel FROM faculty WHERE id = '{}'".format(faculty_id))
    tel = [item[0] for item in cursor.fetchall()]
    conn.commit()

    cursor.execute("SELECT mail_sc FROM faculty WHERE id = '{}'".format(faculty_id))
    mail = [item[0] for item in cursor.fetchall()]
    conn.commit()

    text_contacts = '<b>Вот так можно связаться с приёмной комиссией:</b>\n\n' \
                    '1. Телефон: {} \n' \
                    '2. Почта: {} \n'.format(tel[0], mail[0])

    keyboard_back = types.InlineKeyboardMarkup()

    key_back = types.InlineKeyboardButton(text='\U00002B05', callback_data='back_to_sc')

    keyboard_back.add(key_back)

    return keyboard_back, text_contacts

# print(contact('1'))
