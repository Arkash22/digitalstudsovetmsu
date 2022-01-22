import math
import sys
from os.path import dirname, join, abspath
from telebot import types
from settings import conn, cursor
import settings
# from . import  EmojiAlphabet

sys.path.insert(0, abspath(join(dirname(__file__), '..')))



def change_faculty(page, faculty_list, faculty_list_id):
    length = len(faculty_list)  # длина списка всех групп

    max_page = math.ceil(length / 4)  # считаем сколько будет страниц для списка

    keyboard = types.InlineKeyboardMarkup()  # создаём клавиатуру

    if page == 1:  # передали 1-ю страницу

        # случай когда передано до 4-х групп
        if length <= 4:

            n = length % 4  # делим с остатком, этот остаток и будет нужное нам число кнопок

            if n == 0:  # делиться с нулевым остатком только число 4, значит 4 кнопки

                key1 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 4],
                                                  callback_data=f'change_{faculty_list_id[page * 4 - 4]}')
                key2 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 3],
                                                  callback_data=f'change_{faculty_list_id[page * 4 - 3]}')
                key3 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 2],
                                                  callback_data=f'change_{faculty_list_id[page * 4 - 2]}')
                key4 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 1],
                                                  callback_data=f'change_{faculty_list_id[page * 4 - 1]}')

                keyboard.add(key1, key2)
                keyboard.add(key3, key4)

            if n == 1:  # делиться с нулевым остатком только число 1, значит 1 кнопка

                key1 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 4],
                                                  callback_data=f'change_{faculty_list_id[page * 4 - 4]}')

                keyboard.add(key1)

            if n == 2:  # делиться с нулевым остатком только число 2, значит 2 кнопки

                key1 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 4],
                                                  callback_data=f'change_{faculty_list_id[page * 4 - 4]}')
                key2 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 3],
                                                  callback_data=f'change_{faculty_list_id[page * 4 - 3]}')

                keyboard.add(key1, key2)

            if n == 3:  # делиться с нулевым остатком только число 3, значит 3 кнопки

                key1 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 4],
                                                  callback_data=f'change_{faculty_list_id[page * 4 - 4]}')
                key2 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 3],
                                                  callback_data=f'change_{faculty_list_id[page * 4 - 3]}')
                key3 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 2],
                                                  callback_data=f'change_{faculty_list_id[page * 4 - 2]}')

                keyboard.add(key1, key2)
                keyboard.add(key3)

        else:

            key1 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 4],
                                              callback_data=f'change_{faculty_list_id[page * 4 - 4]}')
            key2 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 3],
                                              callback_data=f'change_{faculty_list_id[page * 4 - 3]}')
            key3 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 2],
                                              callback_data=f'change_{faculty_list_id[page * 4 - 2]}')
            key4 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 1],
                                              callback_data=f'change_{faculty_list_id[page * 4 - 1]}')

            key_next = types.InlineKeyboardButton(text='\U000025B6', callback_data='next_page_faculty_{}_change'.format(page))

            keyboard.add(key1, key2)
            keyboard.add(key3, key4)

            keyboard.add(key_next)


    elif max_page > page > 1:

        key1 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 4],
                                          callback_data=f'change_{faculty_list_id[page * 4 - 4]}')
        key2 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 3],
                                          callback_data=f'change_{faculty_list_id[page * 4 - 3]}')
        key3 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 2],
                                          callback_data=f'change_{faculty_list_id[page * 4 - 2]}')
        key4 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 1],
                                          callback_data=f'change_{faculty_list_id[page * 4 - 1]}')

        key_next = types.InlineKeyboardButton(text='\U000025B6', callback_data='next_page_faculty_{}_change'.format(page))
        key_back = types.InlineKeyboardButton(text='\U000025C0', callback_data='back_page_faculty_{}_change'.format(page))

        keyboard.add(key1, key2)
        keyboard.add(key3, key4)

        keyboard.add(key_back, key_next)


    else:

        n = length % 4  # делим с остатком, этот остаток и будет нужное нам число кнопок

        if n == 0:  # делиться с нулевым остатком только числа кратные 4-м

            key1 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 4],
                                              callback_data=f'change_{faculty_list_id[page * 4 - 4]}')
            key2 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 3],
                                              callback_data=f'change_{faculty_list_id[page * 4 - 3]}')
            key3 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 2],
                                              callback_data=f'change_{faculty_list_id[page * 4 - 2]}')
            key4 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 1],
                                              callback_data=f'change_{faculty_list_id[page * 4 - 1]}')

            key_back = types.InlineKeyboardButton(text='\U000025C0', callback_data='back_page_faculty_{}_change'.format(page))

            keyboard.add(key1, key2)
            keyboard.add(key3, key4)

            keyboard.add(key_back)

        if n == 1:  # делиться с нулевым остатком только число 1, значит 1 кнопка

            key1 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 4],
                                              callback_data=f'change_{faculty_list_id[page * 4 - 4]}')

            key_back = types.InlineKeyboardButton(text='\U000025C0', callback_data='back_page_faculty_{}_change'.format(page))

            keyboard.add(key1)
            keyboard.add(key_back)

        if n == 2:  # делиться с нулевым остатком только число 2, значит 2 кнопки

            key1 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 4],
                                              callback_data=f'change_{faculty_list_id[page * 4 - 4]}')
            key2 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 3],
                                              callback_data=f'change_{faculty_list_id[page * 4 - 3]}')

            key_back = types.InlineKeyboardButton(text='\U000025C0', callback_data='back_page_faculty_{}_change'.format(page))

            keyboard.add(key1, key2)
            keyboard.add(key_back)

        if n == 3:  # делиться с нулевым остатком только число 3, значит 3 кнопки

            key1 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 4],
                                              callback_data=f'change_{faculty_list_id[page * 4 - 4]}')
            key2 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 3],
                                              callback_data=f'change_{faculty_list_id[page * 4 - 3]}')
            key3 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 2],
                                              callback_data=f'change_{faculty_list_id[page * 4 - 2]}')

            key_back = types.InlineKeyboardButton(text='\U000025C0', callback_data='back_page_faculty_{}_change'.format(page))

            keyboard.add(key1, key2)
            keyboard.add(key3)
            keyboard.add(key_back)

    msg = 'Выбирай другой факультет:'

    return keyboard, msg

# print(change_faculty(1, settings.all_faculties()[0], settings.all_faculties()[1]))


def change_program(faculty_id):
    program_list = settings.all_program(faculty_id)

    if program_list == 'не найдено':
        keyboard = types.InlineKeyboardMarkup()
        key_back = types.InlineKeyboardButton(text='\U000025C0', callback_data='lk')
        keyboard.add(key_back)

        msg = 'К сожалению, я не смог найти ни одной программы на твоём факультете'

        return keyboard, msg

    else:

        keyboard = types.InlineKeyboardMarkup()
        n = len(program_list[1])

        if n == 1:
            key_1 = types.InlineKeyboardButton(text=program_list[0][0],
                                               callback_data='change_program_{}'.format(program_list[1][0]))
            # key_back = types.InlineKeyboardButton(text='\U000025C0', callback_data='lk')
            keyboard.add(key_1)
            # keyboard.add(key_back)

        elif n % 2 == 0:
            while n > 0:
                key1 = types.InlineKeyboardButton(text=program_list[0][n - 1],
                                                  callback_data='change_program_{}'.format(program_list[1][n - 1]))
                key2 = types.InlineKeyboardButton(text=program_list[0][n - 2],
                                                  callback_data='change_program_{}'.format(program_list[1][n - 2]))
                keyboard.add(key1, key2)
                n -= 2

            # key_back = types.InlineKeyboardButton(text='\U000025C0', callback_data='lk')
            # keyboard.add(key_back)
        else:
            while n > 1:
                key1 = types.InlineKeyboardButton(text=program_list[0][n - 1],
                                                  callback_data='change_program_{}'.format(program_list[1][n - 1]))
                key2 = types.InlineKeyboardButton(text=program_list[0][n - 2],
                                                  callback_data='change_program_{}'.format(program_list[1][n - 2]))
                keyboard.add(key1, key2)
                n -= 2

            key3 = types.InlineKeyboardButton(text=program_list[0][0],
                                              callback_data='change_program_{}'.format(program_list[1][0]))

            # key_back = types.InlineKeyboardButton(text='\U000025C0', callback_data='lk')
            keyboard.add(key3)
            # keyboard.add(key_back)

        msg = 'Выбирай другое направление и программу:'

        return keyboard, msg

# print(change_program('2'))


# print(settings.all_program('2')[0][0])