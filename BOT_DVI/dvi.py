import texts
import settings
from telebot import types
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from settings import conn, cursor

from users.models import DVI, Potok


def dvi(page):
    names = []
    ids = []
    cursor.execute("SELECT id, name FROM dvi")
    result = cursor.fetchall()
    conn.commit()
    for i in result:
        ids.append(i[0])
        names.append(i[1])

    keyboard_dvi = InlineKeyboardMarkup(row_width=4)
    if page == 1:
        key_1 = InlineKeyboardButton(names[0], callback_data=f'dvi{ids[0]}')
        key_2 = InlineKeyboardButton(names[1], callback_data=f'dvi{ids[1]}')
        key_3 = InlineKeyboardButton(names[2], callback_data=f'dvi{ids[2]}')
        key_4 = InlineKeyboardButton(names[3], callback_data=f'dvi{ids[3]}')

        key_1_page = InlineKeyboardButton('•1•', callback_data='-')
        key_2_page = InlineKeyboardButton('2', callback_data='page_2')
        key_3_page = InlineKeyboardButton('3', callback_data='page_3')
        key_4_page = InlineKeyboardButton('4', callback_data='page_4')

        keyboard_dvi.add(key_1, key_2)
        keyboard_dvi.add(key_3, key_4)
        keyboard_dvi.add(key_1_page, key_2_page, key_3_page, key_4_page)

    if page == 2:
        key_1 = InlineKeyboardButton(names[4], callback_data=f'dvi{ids[4]}')
        key_2 = InlineKeyboardButton(names[5], callback_data=f'dvi{ids[5]}')
        key_3 = InlineKeyboardButton(names[6], callback_data=f'dvi{ids[6]}')
        key_4 = InlineKeyboardButton(names[7], callback_data=f'dvi{ids[7]}')

        key_1_page = InlineKeyboardButton('1', callback_data='page_1')
        key_2_page = InlineKeyboardButton('•2•', callback_data='-')
        key_3_page = InlineKeyboardButton('3', callback_data='page_3')
        key_4_page = InlineKeyboardButton('4', callback_data='page_4')

        keyboard_dvi.add(key_1, key_2)
        keyboard_dvi.add(key_3, key_4)
        keyboard_dvi.add(key_1_page, key_2_page, key_3_page, key_4_page)

    if page == 3:
        key_1 = InlineKeyboardButton(names[8], callback_data=f'dvi{ids[8]}')
        key_2 = InlineKeyboardButton(names[9], callback_data=f'dvi{ids[9]}')
        key_3 = InlineKeyboardButton(names[10], callback_data=f'dvi{ids[10]}')
        key_4 = InlineKeyboardButton(names[11], callback_data=f'dvi{ids[11]}')

        key_1_page = InlineKeyboardButton('1', callback_data='page_1')
        key_2_page = InlineKeyboardButton('2', callback_data='page_2')
        key_3_page = InlineKeyboardButton('•3•', callback_data='-')
        key_4_page = InlineKeyboardButton('4', callback_data='page_4')

        keyboard_dvi.add(key_1, key_2)
        keyboard_dvi.add(key_3, key_4)
        keyboard_dvi.add(key_1_page, key_2_page, key_3_page, key_4_page)

    if page == 4:
        key_1 = InlineKeyboardButton(names[12], callback_data=f'dvi{ids[12]}')
        key_2 = InlineKeyboardButton(names[13], callback_data=f'dvi{ids[13]}')
        key_3 = InlineKeyboardButton(names[14], callback_data=f'dvi{ids[14]}')
        key_4 = InlineKeyboardButton(names[15], callback_data=f'dvi{ids[15]}')
        key_5 = InlineKeyboardButton(names[16], callback_data=f'dvi{ids[16]}')

        key_1_page = InlineKeyboardButton('1', callback_data='page_1')
        key_2_page = InlineKeyboardButton('2', callback_data='page_2')
        key_3_page = InlineKeyboardButton('3', callback_data='page_3')
        key_4_page = InlineKeyboardButton('•4•', callback_data='-')

        keyboard_dvi.add(key_1, key_2)
        keyboard_dvi.add(key_3, key_4)
        keyboard_dvi.add(key_5)
        keyboard_dvi.add(key_1_page, key_2_page, key_3_page, key_4_page)

    key_back = InlineKeyboardButton('<<<', callback_data='back_main_menu')

    keyboard_dvi.add(key_back)

    return keyboard_dvi


def dvi_potok(id):
    dvi = DVI(id)
    result_id = dvi.potok_ids()
    result_name = dvi.potok_names()

    length = len(result_id)

    keyboard_dvi_potok = InlineKeyboardMarkup(row_width=4)

    for i in list(range(0, length)):
        key = InlineKeyboardButton(result_name[i], callback_data=f'potok{result_id[i]}')
        keyboard_dvi_potok.add(key)

    key_back = InlineKeyboardButton('<<<', callback_data='back_to_dvi')
    keyboard_dvi_potok.add(key_back)

    return keyboard_dvi_potok


def dvi_back():
    keyboard = InlineKeyboardMarkup()
    key_back = InlineKeyboardButton('<<<', callback_data='back_to_dvi')
    # key = types.InlineKeyboardButton(text='Списки',
    #                                  url=link)
    key = types.InlineKeyboardButton(text='Списки', callback_data='spiski')

    keyboard.add(key)
    keyboard.add(key_back)

    return keyboard


def dvi_preparation(page):
    names = []
    ids = []
    cursor.execute("SELECT id, name FROM dvi")
    result = cursor.fetchall()
    conn.commit()
    for i in result:
        ids.append(i[0])
        names.append(i[1])

    keyboard_dvi = InlineKeyboardMarkup(row_width=4)
    if page == 1:
        key_1 = InlineKeyboardButton(names[0], callback_data=f'dvi_preparation{ids[0]}')
        key_2 = InlineKeyboardButton(names[1], callback_data=f'dvi_preparation{ids[1]}')
        key_3 = InlineKeyboardButton(names[2], callback_data=f'dvi_preparation{ids[2]}')
        key_4 = InlineKeyboardButton(names[3], callback_data=f'dvi_preparation{ids[3]}')

        key_1_page = InlineKeyboardButton('•1•', callback_data='-')
        key_2_page = InlineKeyboardButton('2', callback_data='page_2_preparation')
        key_3_page = InlineKeyboardButton('3', callback_data='page_3_preparation')
        key_4_page = InlineKeyboardButton('4', callback_data='page_4_preparation')

        keyboard_dvi.add(key_1, key_2)
        keyboard_dvi.add(key_3, key_4)
        keyboard_dvi.add(key_1_page, key_2_page, key_3_page, key_4_page)

    if page == 2:
        key_1 = InlineKeyboardButton(names[4], callback_data=f'dvi_preparation{ids[4]}')
        key_2 = InlineKeyboardButton(names[5], callback_data=f'dvi_preparation{ids[5]}')
        key_3 = InlineKeyboardButton(names[6], callback_data=f'dvi_preparation{ids[6]}')
        key_4 = InlineKeyboardButton(names[7], callback_data=f'dvi_preparation{ids[7]}')

        key_1_page = InlineKeyboardButton('1', callback_data='page_1_preparation')
        key_2_page = InlineKeyboardButton('•2•', callback_data='-')
        key_3_page = InlineKeyboardButton('3', callback_data='page_3_preparation')
        key_4_page = InlineKeyboardButton('4', callback_data='page_4_preparation')

        keyboard_dvi.add(key_1, key_2)
        keyboard_dvi.add(key_3, key_4)
        keyboard_dvi.add(key_1_page, key_2_page, key_3_page, key_4_page)

    if page == 3:
        key_1 = InlineKeyboardButton(names[8], callback_data=f'dvi_preparation{ids[8]}')
        key_2 = InlineKeyboardButton(names[9], callback_data=f'dvi_preparation{ids[9]}')
        key_3 = InlineKeyboardButton(names[10], callback_data=f'dvi_preparation{ids[10]}')
        key_4 = InlineKeyboardButton(names[11], callback_data=f'dvi_preparation{ids[11]}')

        key_1_page = InlineKeyboardButton('1', callback_data='page_1_preparation')
        key_2_page = InlineKeyboardButton('2', callback_data='page_2_preparation')
        key_3_page = InlineKeyboardButton('•3•', callback_data='-')
        key_4_page = InlineKeyboardButton('4', callback_data='page_4_preparation')

        keyboard_dvi.add(key_1, key_2)
        keyboard_dvi.add(key_3, key_4)
        keyboard_dvi.add(key_1_page, key_2_page, key_3_page, key_4_page)

    if page == 4:
        key_1 = InlineKeyboardButton(names[12], callback_data=f'dvi_preparation{ids[12]}')
        key_2 = InlineKeyboardButton(names[13], callback_data=f'dvi_preparation{ids[13]}')
        key_3 = InlineKeyboardButton(names[14], callback_data=f'dvi_preparation{ids[14]}')
        key_4 = InlineKeyboardButton(names[15], callback_data=f'dvi_preparation{ids[15]}')
        key_5 = InlineKeyboardButton(names[16], callback_data=f'dvi_preparation{ids[16]}')

        key_1_page = InlineKeyboardButton('1', callback_data='page_1_preparation')
        key_2_page = InlineKeyboardButton('2', callback_data='page_2_preparation')
        key_3_page = InlineKeyboardButton('3', callback_data='page_3_preparation')
        key_4_page = InlineKeyboardButton('•4•', callback_data='-')

        keyboard_dvi.add(key_1, key_2)
        keyboard_dvi.add(key_3, key_4)
        keyboard_dvi.add(key_5)
        keyboard_dvi.add(key_1_page, key_2_page, key_3_page, key_4_page)

    key_back = InlineKeyboardButton('<<<', callback_data='back_main_menu')

    keyboard_dvi.add(key_back)

    return keyboard_dvi


def dvi_preparation_links(id):
    dvi = DVI(id)

    result_links = dvi.preparation_links()
    result_name = dvi.preparation_links_names()

    length = len(result_links)

    keyboard_dvi_potok = InlineKeyboardMarkup(row_width=4)

    for i in list(range(0, length)):
        # print(result_name[i])
        # print(result_links[i])
        key = types.InlineKeyboardButton(text=result_name[i], url=result_links[i])
        keyboard_dvi_potok.add(key)

    key_back = InlineKeyboardButton('<<<', callback_data='back_to_preparation')
    keyboard_dvi_potok.add(key_back)

    return keyboard_dvi_potok


dvi_preparation_links(1)
