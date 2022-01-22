import math
import sys
from os.path import dirname, join, abspath
from telebot import types
from settings import conn, cursor
# from . import  EmojiAlphabet

sys.path.insert(0, abspath(join(dirname(__file__), '..')))



def minimal_score(program_id):
    cursor.execute("SELECT dvi_min_n FROM faculty_programs WHERE faculty_id = '{}'".format(program_id))
    dvi_min_n = [item[0] for item in cursor.fetchall()]
    conn.commit()

    cursor.execute("SELECT dvi_min_p FROM faculty_programs WHERE faculty_id = '{}'".format(program_id))
    dvi_min_p = [item[0] for item in cursor.fetchall()]
    conn.commit()

    text_contacts = '<b>Сумма <b>минимальных баллов по ДВИ</b> составила:</b>\n\n' \
                    'В 2019 году  - <b>{} баллов</b> \n' \
                    'В 2018 году - <b>{} баллов</b>'.format(dvi_min_n[0], dvi_min_p[0])

    keyboard_back = types.InlineKeyboardMarkup()

    key_back = types.InlineKeyboardButton(text='\U00002B05', callback_data='back_to_dvi')

    keyboard_back.add(key_back)

    return keyboard_back, text_contacts




def mean_score(program_id):
    cursor.execute("SELECT dvi_mean_n FROM table_faculty WHERE faculty = '{}'".format(program_id))
    dvi_mean_n = [item[0] for item in cursor.fetchall()]
    conn.commit()

    cursor.execute("SELECT dvi_mean_p FROM table_faculty WHERE faculty = '{}'".format(program_id))
    dvi_mean_p = [item[0] for item in cursor.fetchall()]
    conn.commit()

    text_contacts = 'Сумма <b>средних баллов по ДВИ</b> составила:\n\n' \
                    'В 2019 году  - <b>{} баллов</b> \n' \
                    'В 2018 году - <b>{} баллов</b>'.format(dvi_mean_n[0], dvi_mean_p[0])

    keyboard_back = types.InlineKeyboardMarkup()

    key_back = types.InlineKeyboardButton(text='\U00002B05', callback_data='back_to_dvi')

    keyboard_back.add(key_back)

    return keyboard_back, text_contacts


def subjects(program_id):
    cursor.execute("SELECT dvi_list FROM faculty_programs WHERE id = {}".format(program_id))
    dvi_list = [item[0] for item in cursor.fetchall()]
    conn.commit()
    try:
        ege_subjects = dvi_list[0].split(';')

        length = len(ege_subjects)

        if length == 1:
            text = 'Ты сдаёшь ДВИ только по дисциплине <b>"{}"</b>'.format(dvi_list[0])
        else:
            result = ''
            for i in list(range(length)):
                result = result + '{}. {} \n'.format(i + 1, ege_subjects[i])

            text = '<b>Вот дисциплины ЕГЭ необходимые для поступления:</b>\n\n' + result

    except Exception:
        text = 'Ты сдаёшь ДВИ только по дисциплине <b>"{}"</b>'.format(dvi_list[0])

    keyboard_back = types.InlineKeyboardMarkup()

    key_back = types.InlineKeyboardButton(text='\U00002B05', callback_data='entrance')

    keyboard_back.add(key_back)

    return keyboard_back, text

# print(subjects('МехМат', 'Механика'))



