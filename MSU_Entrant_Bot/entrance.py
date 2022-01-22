import math
import sys
from os.path import dirname, join, abspath
from telebot import types
from settings import conn, cursor

# from . import  EmojiAlphabet

sys.path.insert(0, abspath(join(dirname(__file__), '..')))


def tenure(program_id):
    cursor.execute("SELECT budget FROM faculty_programs WHERE id = '{}'".format(program_id))
    budget = cursor.fetchone()
    conn.commit()

    cursor.execute("SELECT paid  FROM faculty_programs WHERE id = '{}'".format(program_id))
    paid = cursor.fetchone()
    conn.commit()

    cursor.execute("SELECT extra_quota FROM faculty_programs WHERE id = '{}'".format(program_id))
    extra_quota = cursor.fetchone()
    conn.commit()

    cursor.execute("SELECT cel_quota FROM faculty_programs WHERE id = '{}'".format(program_id))
    cel_quota = cursor.fetchone()
    conn.commit()

    summa = int(budget[0]) + int(paid[0])
    keyboard = types.InlineKeyboardMarkup()

    key_1 = types.InlineKeyboardButton(text='\U0001F381 Бюджет', callback_data='budget')
    key_2 = types.InlineKeyboardButton(text='\U0001F4B0 Платка', callback_data='paid')
    key_back = types.InlineKeyboardButton(text='\U00002B05', callback_data='entrance')

    keyboard.add(key_1, key_2)
    keyboard.add(key_back)

    msg = 'Всего мест в этом году - <b>{}</b>. Из них:\n\n' \
          '\U0001F4B0 На платку - <b>{}</b>\n' \
          '\U0001F381 На бюджет - <b>{}</b>\n' \
          '  -По особой квоте (информация будет обновляться) - <b>{}</b>\n' \
          '  -По целевой квоте (информация будет обновляться) - <b>{}</b>\n\n' \
          '<b>Выбирай, куда хочешь поступить?</b>'.format(summa, paid[0], budget[0], extra_quota[0], cel_quota[0])

    return keyboard, msg


def budget(program_id):
    cursor.execute("SELECT budget FROM faculty_programs WHERE id = '{}'".format(program_id))
    budget_people = [item[0] for item in cursor.fetchall()][0]
    conn.commit()
    keyboard = types.InlineKeyboardMarkup()

    if not int(budget_people) == 0:
        key_1 = types.InlineKeyboardButton(text='\U0000203C Проходные баллы', callback_data='passing_score')
        key_2 = types.InlineKeyboardButton(text='\U0001F38E Человек на место', callback_data='people-seat')
        key_back = types.InlineKeyboardButton(text='\U00002B05', callback_data='tenure')

        keyboard.add(key_1, key_2)
        keyboard.add(key_back)

        msg = 'Что именно тебя интересует?'

        return keyboard, msg
    else:
        key_back = types.InlineKeyboardButton(text='\U00002B05', callback_data='tenure')
        keyboard.add(key_back)
        msg = 'Не существует бюджетных мест на выбранной программе'

        return keyboard, msg


def paid(program_id):
    cursor.execute("SELECT paid FROM faculty_programs WHERE id = '{}'".format(program_id))
    paid_people = [item[0] for item in cursor.fetchall()][0]
    conn.commit()
    keyboard = types.InlineKeyboardMarkup()

    if not int(paid_people) == 0:

        key_1 = types.InlineKeyboardButton(text='\U0001F4C9 Минимальный балл', callback_data='minimal_score')
        key_2 = types.InlineKeyboardButton(text='\U0001F4B5 Стоимость обучения \U0001F4B6', callback_data='price')
        key_back = types.InlineKeyboardButton(text='\U00002B05', callback_data='tenure')

        keyboard.add(key_1, key_2)
        keyboard.add(key_back)

        msg = 'Что именно тебя интересует?'

        return keyboard, msg

    else:
        key_back = types.InlineKeyboardButton(text='\U00002B05', callback_data='tenure')
        keyboard.add(key_back)
        msg = 'Не существует платных мест на выбранной программе'

        return keyboard, msg


def last_year_dvi(program_id):
    keyboard = types.InlineKeyboardMarkup()

    cursor.execute("SELECT dvi_list FROM faculty_programs WHERE id = '{}'".format(program_id))
    dvi_list = [item[0] for item in cursor.fetchall()]
    conn.commit()

    try:
        ege_subjects = dvi_list[0].split(';')
        length = len(ege_subjects)
        if length == 1:
            key = types.InlineKeyboardButton(text=dvi_list[0], callback_data='dvi_subject')
            keyboard.add(key)
        else:
            key = types.InlineKeyboardButton(text='Не найдено', callback_data='entrance')
            keyboard.add(key)

    except Exception:
        key = types.InlineKeyboardButton(text='Не найдено', callback_data='entrance')
        keyboard.add(key)

    key_back = types.InlineKeyboardButton(text='\U00002B05', callback_data='entrance')
    keyboard.add(key_back)

    msg = 'К какой дисциплине вы готовитесь?'

    return keyboard, msg


# print(last_year_dvi('1'))


def dvi_subject(program_id):
    cursor.execute("SELECT dvi_list FROM faculty_programs WHERE id = '{}'".format(program_id))
    subject = [item[0] for item in cursor.fetchall()]
    conn.commit()

    if subject[0].lower() == 'математика':
        keyboard = types.InlineKeyboardMarkup()

        key_1 = types.InlineKeyboardButton(text='ДВИ-2019 Математика ',
                                           url='http://cpk.msu.ru/files/2019/tasks/math.pdf')
        key_2 = types.InlineKeyboardButton(text='Ответы ДВИ-2019',
                                           url='http://cpk.msu.ru/files/2019/tasks/math_solutions.pdf')
        key_3 = types.InlineKeyboardButton(text='ДВИ-2018 Математика',
                                           url='http://cpk.msu.ru/files/2018/tasks/math.pdf')
        key_4 = types.InlineKeyboardButton(text='Ответы ДВИ-2019',
                                           url='http://cpk.msu.ru/files/2018/tasks/math_solutions.pdf')
        key_5 = types.InlineKeyboardButton(text='ДВИ-2017 Математика', url='http://cpk.msu.ru/files/2017/math.pdf')
        key_6 = types.InlineKeyboardButton(text='Ответы ДВИ-2017',
                                           url='http://pk.math.msu.ru/sites/default/files/variants/DVI%20LETO/math-dvi-2017-solutions.pdf')
        key_7 = types.InlineKeyboardButton(text='МНЕ МАЛО', url='http://pk.math.msu.ru/ru/specialist/variant')

        key_back = types.InlineKeyboardButton(text='\U00002B05', callback_data='entrance')

        keyboard.add(key_1, key_2)
        keyboard.add(key_3, key_4)
        keyboard.add(key_5, key_6)
        keyboard.add(key_7)
        keyboard.add(key_back)

        msg = 'Вот варианты ДВИ прошлых лет по <b>Математике:</b>'

    elif subject[0].lower() == 'физика':
        keyboard = types.InlineKeyboardMarkup()

        key_1 = types.InlineKeyboardButton(text='ДВИ-2019 Физика ',
                                           url='http://cpk.msu.ru/files/2019/tasks/physics_01.pdf')
        key_3 = types.InlineKeyboardButton(text='ДВИ-2018 Физика',
                                           url='http://cpk.msu.ru/files/2018/tasks/physics_01.pdf')
        key_4 = types.InlineKeyboardButton(text='С разбором',
                                           url='https://phys.msu.ru/rus/entrants/publications/DVI7.pdf')
        key_5 = types.InlineKeyboardButton(text='ДВИ-2017 Физика', url='http://cpk.msu.ru/files/2017/physics_01.pdf')

        key_7 = types.InlineKeyboardButton(text='МНЕ МАЛО', url='https://phys.msu.ru/rus/entrants/publications/')

        key_back = types.InlineKeyboardButton(text='\U00002B05', callback_data='entrance')

        keyboard.add(key_1)
        keyboard.add(key_3, key_4)
        keyboard.add(key_5)
        keyboard.add(key_7)
        keyboard.add(key_back)

        msg = 'Вот варианты ДВИ прошлых лет по <b>Физике:</b>'

    elif subject[0].lower() == 'биология':
        keyboard = types.InlineKeyboardMarkup()

        key_1 = types.InlineKeyboardButton(text='ДВИ-2019 Биология',
                                           url='http://cpk.msu.ru/files/2019/tasks/biology_01.pdf')
        key_3 = types.InlineKeyboardButton(text='ДВИ-2018 Биология',
                                           url='http://cpk.msu.ru/files/2018/tasks/biology_01.pdf')
        key_5 = types.InlineKeyboardButton(text='ДВИ-2017 Биология', url='http://cpk.msu.ru/files/2017/biology_01.pdf')

        key_7 = types.InlineKeyboardButton(text='Программа', url='https://www.msu.ru/entrance/program/biol.html')

        key_back = types.InlineKeyboardButton(text='\U00002B05', callback_data='entrance')

        keyboard.add(key_1)
        keyboard.add(key_3)
        keyboard.add(key_5)
        keyboard.add(key_7)
        keyboard.add(key_back)

        msg = 'Вот варианты ДВИ прошлых лет по <b>Биологии:</b>'

    elif subject[0].lower() == 'история':
        keyboard = types.InlineKeyboardMarkup()

        key_1 = types.InlineKeyboardButton(text='ДВИ-2019 История',
                                           url='http://cpk.msu.ru/files/2019/tasks/biology_01.pdf')
        key_3 = types.InlineKeyboardButton(text='ДВИ-2018 История',
                                           url='http://cpk.msu.ru/files/2018/tasks/biology_01.pdf')
        key_5 = types.InlineKeyboardButton(text='ДВИ-2017 История', url='http://cpk.msu.ru/files/2017/biology_01.pdf')

        key_7 = types.InlineKeyboardButton(text='Программа', url='https://www.msu.ru/entrance/program/hist.html')

        key_back = types.InlineKeyboardButton(text='\U00002B05', callback_data='entrance')

        keyboard.add(key_1)
        keyboard.add(key_3)
        keyboard.add(key_5)
        keyboard.add(key_7)
        keyboard.add(key_back)

        msg = 'Вот варианты ДВИ прошлых лет по <b>Истории:</b>'

    elif subject[0].lower() == 'литература':
        keyboard = types.InlineKeyboardMarkup()

        key_1 = types.InlineKeyboardButton(text='ДВИ-2019 Литература',
                                           url='http://cpk.msu.ru/files/2019/tasks/literature.pdf')
        key_2 = types.InlineKeyboardButton(text='Видео: разбор ДВИ',
                                           url='https: // www.youtube.com / watch?v = zWwLSYNByLE')

        key_7 = types.InlineKeyboardButton(text='Программа', url='https://www.msu.ru/entrance/program/liter.html')

        key_back = types.InlineKeyboardButton(text='\U00002B05', callback_data='entrance')

        keyboard.add(key_1)
        keyboard.add(key_2)
        keyboard.add(key_7)
        keyboard.add(key_back)

        msg = 'Вот варианты ДВИ прошлых лет по <b>Литературе:</b>'

    elif subject[0].lower() == 'английский язык':
        keyboard = types.InlineKeyboardMarkup()

        key_1 = types.InlineKeyboardButton(text='ДВИ-2019 Английский',
                                           url='http://cpk.msu.ru/files/2019/tasks/english_01.pdf')
        key_3 = types.InlineKeyboardButton(text='ДВИ-2018 Английский',
                                           url='http://cpk.msu.ru/files/2018/tasks/english_01.pdf')

        key_5 = types.InlineKeyboardButton(text='ДВИ-2017 Английский',
                                           url='http://cpk.msu.ru/files/2017/english_01.pdf')

        key_7 = types.InlineKeyboardButton(text='Программа', url='https://www.msu.ru/entrance/program/forlang.html')

        key_back = types.InlineKeyboardButton(text='\U00002B05', callback_data='entrance')

        keyboard.add(key_1)
        keyboard.add(key_3)
        keyboard.add(key_5)
        keyboard.add(key_7)
        keyboard.add(key_back)

        msg = 'Вот варианты ДВИ прошлых лет по <b>Англискому Языку:</b>'

    elif subject[0].lower() == 'обществознание':
        keyboard = types.InlineKeyboardMarkup()

        key_1 = types.InlineKeyboardButton(text='ДВИ-2019 Обществознание',
                                           url='http://cpk.msu.ru/files/2019/tasks/society_01.pdf')
        key_3 = types.InlineKeyboardButton(text='ДВИ-2018 Обществознание',
                                           url='http://cpk.msu.ru/files/2018/tasks/society_01.pdf')

        key_5 = types.InlineKeyboardButton(text='ДВИ-2017 Обществознание',
                                           url='http://cpk.msu.ru/files/2017/society_01.pdf')

        key_7 = types.InlineKeyboardButton(text='Программа', url='https://www.msu.ru/entrance/program/ss.html')

        key_8 = types.InlineKeyboardButton(text='Видео: разбор', url='https://www.youtube.com/watch?v=9GL8ddJ2tlI')

        key_back = types.InlineKeyboardButton(text='\U00002B05', callback_data='entrance')

        keyboard.add(key_1)
        keyboard.add(key_3)
        keyboard.add(key_5)
        keyboard.add(key_7, key_8)
        keyboard.add(key_back)

        msg = 'Вот варианты ДВИ прошлых лет по <b>Обществознаниюу:</b>'

    elif subject[0].lower() == 'химия':
        keyboard = types.InlineKeyboardMarkup()

        key_1 = types.InlineKeyboardButton(text='ДВИ-2019 Химия',
                                           url='http://cpk.msu.ru/files/2019/tasks/chemistry_01.pdf')
        key_3 = types.InlineKeyboardButton(text='ДВИ-2018 Химия',
                                           url='http://cpk.msu.ru/files/2018/tasks/chemistry_01.pdf')

        key_5 = types.InlineKeyboardButton(text='ДВИ-2017 Химия',
                                           url='http://cpk.msu.ru/files/2017/chemistry_01.pdf')

        key_7 = types.InlineKeyboardButton(text='МНЕ МАЛО',
                                           url='http://chembaby.com/uchebnye-materialy-dlya-abiturientov/')

        key_back = types.InlineKeyboardButton(text='\U00002B05', callback_data='entrance')

        keyboard.add(key_1)
        keyboard.add(key_3)
        keyboard.add(key_5)
        keyboard.add(key_7)
        keyboard.add(key_back)

        msg = 'Вот варианты ДВИ прошлых лет по <b>Химии:</b>'

    elif subject[0].lower() == 'география':
        keyboard = types.InlineKeyboardMarkup()

        key_1 = types.InlineKeyboardButton(text='ДВИ-2019 География',
                                           url='http://cpk.msu.ru/files/2019/tasks/geography_01.pdf')
        key_3 = types.InlineKeyboardButton(text='ДВИ-2018 География',
                                           url='http://cpk.msu.ru/files/2018/tasks/geography_01.pdf')

        key_5 = types.InlineKeyboardButton(text='ДВИ-2017 География',
                                           url='http://cpk.msu.ru/files/2017/geography_01.pdf')

        key_7 = types.InlineKeyboardButton(text='Программа',
                                           url='https://www.msu.ru/entrance/program/geogr.html')

        key_back = types.InlineKeyboardButton(text='\U00002B05', callback_data='entrance')

        keyboard.add(key_1)
        keyboard.add(key_3)
        keyboard.add(key_5)
        keyboard.add(key_7)
        keyboard.add(key_back)

        msg = 'Вот варианты ДВИ прошлых лет по <b>Географии:</b>'


    else:
        keyboard = types.InlineKeyboardMarkup()
        key_back = types.InlineKeyboardButton(text='\U00002B05', callback_data='entrance')
        keyboard.add(key_back)

        msg = 'Варианты прошлых лет отсутствуют('

    return keyboard, msg


def passing_score(program_id):
    cursor.execute("SELECT passing_score_1v FROM faculty_programs WHERE id = '{}'".format(program_id))
    passing_score_1 = [item[0] for item in cursor.fetchall()][0]
    conn.commit()

    cursor.execute("SELECT passing_score_2v FROM faculty_programs WHERE id = '{}'".format(program_id))
    passing_score_2 = [item[0] for item in cursor.fetchall()][0]
    conn.commit()

    keyboard = types.InlineKeyboardMarkup()
    key_back = types.InlineKeyboardButton(text='\U00002B05', callback_data='budget')
    keyboard.add(key_back)

    msg = 'В 2020 году <i>проходные баллы на бюджет</i> были следующие:\n\n' \
          '<b>1-я волна: {}\n' \
          '2-я волна: {}</b>'.format(passing_score_1, passing_score_2)

    return keyboard, msg


def people_seat(program_id):
    cursor.execute("SELECT people_seat FROM faculty_programs WHERE id = '{}'".format(program_id))
    total_people = [item[0] for item in cursor.fetchall()][0]
    conn.commit()

    cursor.execute("SELECT budget FROM faculty_programs WHERE id = '{}'".format(program_id))
    budget = [item[0] for item in cursor.fetchall()][0]
    conn.commit()

    all_budget = int(budget)
    people_seat = float(total_people) / (float(budget))

    keyboard = types.InlineKeyboardMarkup()
    key_back = types.InlineKeyboardButton(text='\U00002B05', callback_data='budget')
    keyboard.add(key_back)

    msg = 'В 2020 году даннные были следующие:\n\n' \
          'Подавших заявления: {}\n' \
          'Бюджетных мест (включая места по квоте): {}\n' \
          '<b>Человек на место: {}</b>'.format(total_people, all_budget, round(people_seat, 1))

    return keyboard, msg


def price(program_id):
    cursor.execute("SELECT price FROM faculty_programs WHERE id = '{}'".format(program_id))
    price = [item[0] for item in cursor.fetchall()][0]
    conn.commit()

    cursor.execute("SELECT paid FROM faculty_programs WHERE id = '{}'".format(program_id))
    paid_people = [item[0] for item in cursor.fetchall()][0]
    conn.commit()

    keyboard = types.InlineKeyboardMarkup()
    key_back = types.InlineKeyboardButton(text='\U00002B05', callback_data='paid')
    keyboard.add(key_back)

    msg = 'В 2019 году даннные были следующие:\n\n' \
          'Всего платников на направлении:  {}\n' \
          '<b>Стоимость года обучения: {} рублей\n</b>'.format(paid_people, price)

    return keyboard, msg


def min_score(program_id):
    cursor.execute("SELECT min_score FROM faculty_programs WHERE id = '{}'".format(program_id))
    min_score = [item[0] for item in cursor.fetchall()][0]
    conn.commit()

    cursor.execute("SELECT paid FROM faculty_programs WHERE id = '{}'".format(program_id))
    paid_people = [item[0] for item in cursor.fetchall()][0]
    conn.commit()

    keyboard = types.InlineKeyboardMarkup()
    key_back = types.InlineKeyboardButton(text='\U00002B05', callback_data='paid')
    keyboard.add(key_back)

    msg = 'В 2019 году даннные были следующие:\n\n' \
          'Всего платников на направлении:  {}\n' \
          '<b>Минимальные баллы по спискам: {}\n</b>'.format(paid_people, min_score)

    return keyboard, msg
