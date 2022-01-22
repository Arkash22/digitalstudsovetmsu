import math
import sys
from os.path import dirname, join, abspath
from telebot import types
from settings import conn, cursor
# from . import  EmojiAlphabet

sys.path.insert(0, abspath(join(dirname(__file__), '..')))




def minimal_score(faculty):
    cursor.execute("SELECT ege_min FROM table_faculty WHERE faculty = '{}'".format(faculty))
    ege_min = [item[0] for item in cursor.fetchall()]
    conn.commit()

    cursor.execute("SELECT ege_min_2018 FROM table_faculty WHERE faculty = '{}'".format(faculty))
    ege_min_2018 = [item[0] for item in cursor.fetchall()]
    conn.commit()

    text_contacts = '<b>Сумма <b>минимальных баллов по ЕГЭ</b> составила:</b>\n\n' \
                    'В 2019 году  - <b>{} баллов</b> \n' \
                    'В 2018 году - <b>{} баллов</b>'.format(ege_min[0], ege_min_2018[0])

    keyboard_back = types.InlineKeyboardMarkup()

    key_back = types.InlineKeyboardButton(text='\U00002B05', callback_data='back_to_ege')

    keyboard_back.add(key_back)

    return keyboard_back, text_contacts


def mean_score(faculty):
    cursor.execute("SELECT ege_mean FROM table_faculty WHERE faculty = '{}'".format(faculty))
    ege_mean = [item[0] for item in cursor.fetchall()]
    conn.commit()

    cursor.execute("SELECT ege_mean_2018 FROM table_faculty WHERE faculty = '{}'".format(faculty))
    ege_mean_2018 = [item[0] for item in cursor.fetchall()]
    conn.commit()

    text_contacts = 'Сумма <b>средних баллов по ЕГЭ</b> составила:\n\n' \
                    'В 2019 году  - <b>{} баллов</b> \n' \
                    'В 2018 году - <b>{} баллов</b>'.format(ege_mean[0], ege_mean_2018[0])
    keyboard_back = types.InlineKeyboardMarkup()

    key_back = types.InlineKeyboardButton(text='\U00002B05', callback_data='back_to_ege')

    keyboard_back.add(key_back)

    return keyboard_back, text_contacts


def subjects(program_id):
    cursor.execute("SELECT ege_list FROM faculty_programs WHERE id = {}".format(program_id))
    ege_list = cursor.fetchone()
    conn.commit()

    ege_subjects = ege_list[0].split(';')

    length = len(ege_subjects)

    result = ''

    for i in list(range(length)):
        result = result + '{}. {} \n'.format(i + 1, ege_subjects[i])
        i += 1

    text_contacts = '<b>Вот дисциплины ЕГЭ необходимые для поступления:</b>\n\n' + result

    keyboard_back = types.InlineKeyboardMarkup()

    key_back = types.InlineKeyboardButton(text='\U00002B05', callback_data='entrance')

    keyboard_back.add(key_back)

    return keyboard_back, text_contacts


# print(subjects('1'))
