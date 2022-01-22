#
#
# в этом файле храняться все сообщения от бота и все клавиатуры
import math
import sys
from os.path import dirname, join, abspath
from telebot import types

# from . import  EmojiAlphabet

sys.path.insert(0, abspath(join(dirname(__file__), '..')))
from settings import conn, cursor
import settings


# ------------------------------------------------
def home():  # первое сообщение при отсутсвии регистрации
    keyboard_register = types.InlineKeyboardMarkup()

    key_1 = types.InlineKeyboardButton(text='\U0001F6AA Войти', callback_data='go_login')
    key_2 = types.InlineKeyboardButton(text='\U0000260E Контакты', callback_data='contacts')
    key_3 = types.InlineKeyboardButton(text='\U00002139 О Боте', callback_data='info_no_reg')

    keyboard_register.add(key_1)
    keyboard_register.add(key_2, key_3)

    msg = 'Мы с тобой ещё не знакомы, щёлкай "ВОЙТИ"!'

    return keyboard_register, msg


# ------------------------------------------------
def status():  # выбор учитель или ученик при регистрации
    keyboard_teacher_student = types.InlineKeyboardMarkup()

    key_1 = types.InlineKeyboardButton(text='\U0001F60E Подал документы', callback_data='entrant')
    key_2 = types.InlineKeyboardButton(text='\U0001F937\U0000200D\U00002642\U0000FE0F Обдумываю поступление',
                                       callback_data='not_entrant')
    key_3 = types.InlineKeyboardButton(text='\U0001F468\U0000200D\U0001F393 Уже студент МГУ',
                                       callback_data='student')
    key_back = types.InlineKeyboardButton(text='\U00002B05', callback_data='back_home')

    keyboard_teacher_student.add(key_1)
    keyboard_teacher_student.add(key_2)
    keyboard_teacher_student.add(key_3)

    keyboard_teacher_student.add(key_back)

    msg = 'Теперь укажи, на какой ты стадии?'

    return keyboard_teacher_student, msg


# ------------------------------------------------
def home_back():  # клавиатура "назад"
    keyboard_reg_back = types.InlineKeyboardMarkup()

    key_back = types.InlineKeyboardButton(text='\U00002B05', callback_data='back_home')

    keyboard_reg_back.add(key_back)

    return keyboard_reg_back


# ------------------------------------------------

def reg_faculty(page, faculty_list, faculty_list_id):
    length = len(faculty_list)  # длина списка всех групп

    max_page = math.ceil(length / 4)  # считаем сколько будет страниц для списка

    keyboard = types.InlineKeyboardMarkup()  # создаём клавиатуру

    if page == 1:  # передали 1-ю страницу
    
        # случай когда передано до 4-х групп
        if length <= 4:

            n = length % 4  # делим с остатком, этот остаток и будет нужное нам число кнопок

            if n == 0:  # делиться с нулевым остатком только число 4, значит 4 кнопки

                key1 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 4],
                                                  callback_data=f'reg_{faculty_list_id[page * 4 - 4]}')
                key2 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 3],
                                                  callback_data=f'reg_{faculty_list_id[page * 4 - 3]}')
                key3 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 2],
                                                  callback_data=f'reg_{faculty_list_id[page * 4 - 2]}')
                key4 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 1],
                                                  callback_data=f'reg_{faculty_list_id[page * 4 - 1]}')

                keyboard.add(key1, key2)
                keyboard.add(key3, key4)

            if n == 1:  # делиться с нулевым остатком только число 1, значит 1 кнопка

                key1 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 4],
                                                  callback_data=f'reg_{faculty_list_id[page * 4 - 4]}')

                keyboard.add(key1)

            if n == 2:  # делиться с нулевым остатком только число 2, значит 2 кнопки

                key1 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 4],
                                                  callback_data=f'reg_{faculty_list_id[page * 4 - 4]}')
                key2 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 3],
                                                  callback_data=f'reg_{faculty_list_id[page * 4 - 3]}')

                keyboard.add(key1, key2)

            if n == 3:  # делиться с нулевым остатком только число 3, значит 3 кнопки

                key1 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 4],
                                                  callback_data=f'reg_{faculty_list_id[page * 4 - 4]}')
                key2 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 3],
                                                  callback_data=f'reg_{faculty_list_id[page * 4 - 3]}')
                key3 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 2],
                                                  callback_data=f'reg_{faculty_list_id[page * 4 - 2]}')

                keyboard.add(key1, key2)
                keyboard.add(key3)
        
        else:

            key1 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 4],
                                              callback_data=f'reg_{faculty_list_id[page * 4 - 4]}')
            key2 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 3],
                                              callback_data=f'reg_{faculty_list_id[page * 4 - 3]}')
            key3 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 2],
                                              callback_data=f'reg_{faculty_list_id[page * 4 - 2]}')
            key4 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 1],
                                              callback_data=f'reg_{faculty_list_id[page * 4 - 1]}')

            key_next = types.InlineKeyboardButton(text='\U000025B6', callback_data='next_page_faculty_{}'.format(page))

            keyboard.add(key1, key2)
            keyboard.add(key3, key4)

            keyboard.add(key_next)

    
    elif max_page > page > 1:

        key1 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 4],
                                          callback_data=f'reg_{faculty_list_id[page * 4 - 4]}')
        key2 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 3],
                                          callback_data=f'reg_{faculty_list_id[page * 4 - 3]}')
        key3 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 2],
                                          callback_data=f'reg_{faculty_list_id[page * 4 - 2]}')
        key4 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 1],
                                          callback_data=f'reg_{faculty_list_id[page * 4 - 1]}')

        key_next = types.InlineKeyboardButton(text='\U000025B6', callback_data='next_page_faculty_{}'.format(page))
        key_back = types.InlineKeyboardButton(text='\U000025C0', callback_data='back_page_faculty_{}'.format(page))

        keyboard.add(key1, key2)
        keyboard.add(key3, key4)

        keyboard.add(key_back, key_next)

    
    else:

        n = length % 4  # делим с остатком, этот остаток и будет нужное нам число кнопок

        if n == 0:  # делиться с нулевым остатком только числа кратные 4-м

            key1 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 4],
                                              callback_data=f'reg_{faculty_list_id[page * 4 - 4]}')
            key2 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 3],
                                              callback_data=f'reg_{faculty_list_id[page * 4 - 3]}')
            key3 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 2],
                                              callback_data=f'reg_{faculty_list_id[page * 4 - 2]}')
            key4 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 1],
                                              callback_data=f'reg_{faculty_list_id[page * 4 - 1]}')

            key_back = types.InlineKeyboardButton(text='\U000025C0', callback_data='back_page_faculty_{}'.format(page))

            keyboard.add(key1, key2)
            keyboard.add(key3, key4)

            keyboard.add(key_back)

        if n == 1:  # делиться с нулевым остатком только число 1, значит 1 кнопка

            key1 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 4],
                                              callback_data=f'reg_{faculty_list_id[page * 4 - 4]}')

            key_back = types.InlineKeyboardButton(text='\U000025C0', callback_data='back_page_faculty_{}'.format(page))

            keyboard.add(key1)
            keyboard.add(key_back)

        if n == 2:  # делиться с нулевым остатком только число 2, значит 2 кнопки

            key1 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 4],
                                              callback_data=f'reg_{faculty_list_id[page * 4 - 4]}')
            key2 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 3],
                                              callback_data=f'reg_{faculty_list_id[page * 4 - 3]}')

            key_back = types.InlineKeyboardButton(text='\U000025C0', callback_data='back_page_faculty_{}'.format(page))

            keyboard.add(key1, key2)
            keyboard.add(key_back)

        if n == 3:  # делиться с нулевым остатком только число 3, значит 3 кнопки

            key1 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 4],
                                              callback_data=f'reg_{faculty_list_id[page * 4 - 4]}')
            key2 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 3],
                                              callback_data=f'reg_{faculty_list_id[page * 4 - 3]}')
            key3 = types.InlineKeyboardButton(text=faculty_list[page * 4 - 2],
                                              callback_data=f'reg_{faculty_list_id[page * 4 - 2]}')

            key_back = types.InlineKeyboardButton(text='\U000025C0', callback_data='back_page_faculty_{}'.format(page))

            keyboard.add(key1, key2)
            keyboard.add(key3)
            keyboard.add(key_back)

    msg = 'Выбирай свой факультет:'

    return keyboard, msg


def reg_program(faculty_id):
    program_list = settings.all_program(faculty_id)

    if program_list == 'не найдено':
        keyboard = types.InlineKeyboardMarkup()
        key_back = types.InlineKeyboardButton(text='\U000025C0', callback_data='back_home')
        keyboard.add(key_back)

        msg = 'К сожалению, я не смог найти ни одной программы на твоём факультете,' \
              ' может быть тебя интересует другой факультет?'

        return keyboard, msg

    else:

        keyboard = types.InlineKeyboardMarkup()
        n = len(program_list[1])

        if n == 1:
            key_1 = types.InlineKeyboardButton(text=program_list[0][0],
                                               callback_data='reg_program_{}'.format(program_list[1][0]))
            key_back = types.InlineKeyboardButton(text='\U000025C0', callback_data='back_home')
            keyboard.add(key_1)
            keyboard.add(key_back)

        elif n % 2 == 0:
            while n > 0:
                key1 = types.InlineKeyboardButton(text=program_list[0][n - 1],
                                                  callback_data='reg_program_{}'.format(program_list[1][n - 1]))
                key2 = types.InlineKeyboardButton(text=program_list[0][n - 2],
                                                  callback_data='reg_program_{}'.format(program_list[1][n - 2]))
                keyboard.add(key1, key2)
                n -= 2

            key_back = types.InlineKeyboardButton(text='\U000025C0', callback_data='back_home')
            keyboard.add(key_back)
        else:
            while n > 1:
                key1 = types.InlineKeyboardButton(text=program_list[0][n - 1],
                                                  callback_data='reg_program_{}'.format(program_list[1][n - 1]))
                key2 = types.InlineKeyboardButton(text=program_list[0][n - 2],
                                                  callback_data='reg_program_{}'.format(program_list[1][n - 2]))
                keyboard.add(key1, key2)
                n -= 2

            key3 = types.InlineKeyboardButton(text=program_list[0][0],
                                              callback_data='reg_program_{}'.format(program_list[1][0]))

            key_back = types.InlineKeyboardButton(text='\U000025C0', callback_data='back_home')
            keyboard.add(key3)
            keyboard.add(key_back)

        msg = 'Выбирай программу:'

        return keyboard, msg

#
# print(reg_program('1'))
