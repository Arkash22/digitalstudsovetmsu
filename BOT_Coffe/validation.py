import re
import settings
from settings import conn

def validFIO(text):
    with conn.cursor() as cursor:
        cursor.execute("SELECT COUNT (*) FROM users_all WHERE first_name = %(first_name)s",{'first_name':text})
        conn.commit()
        count = cursor.fetchone()[0]
        result = re.findall(r'\d', text)

        if not re.findall(r"drop table", text.lower()) == []:
            # print(re.findall(r"drop table", text.lower()))
            msg = 'Неплохо-неплохо, ломай меня полностью:)'
            return msg

        if not re.findall(r"users_all", text.lower()) == []:
            # print(re.findall(r"drop table", text.lower()))
            msg = 'Неплохо-неплохо, ломай меня полностью:)'
            return msg

        if result != []:
            msg = 'Числа писать нельзя!'
            return msg

        if len(text) > 30:
            msg = 'Слишком много символов!'
            return msg

    # if not 1 < len(text.split(' ')) < 4:
    #     msg = 'Укажите и Имя и Фамилию'
    #     return msg

    if not count == 0:
        msg = 'Данные ФИО уже заняты, возможно, ты регистрировался на другой платформе!'
        return msg

    else:
        msg = 200
        return msg


# print(validFIO('Алексей'))


def validGender(text):
    t = text.split()
    result = re.findall(r'\d', text)

    if not re.findall(r"drop table", text.lower()) == []:
        print(re.findall(r"drop table", text.lower()))
        msg = 'Неплохо-неплохо, ломай меня полностью:)'
        return msg

    if not re.findall(r"users_all", text.lower()) == []:
        # print(re.findall(r"drop table", text.lower()))
        msg = 'Неплохо-неплохо, ломай меня полностью:)'
        return msg

    if t[0] == 'Мужской' or t[0] == 'Женский' or t[0] == 'Деревянный':
        msg = 200
        return msg

    if len(text) > 30:
        msg = 'Слишком много символов!'
        return msg

    if result != []:
        msg = 'Числа писать нельзя!'
        return msg

    else:
        msg = 201
        return msg


# print(validGender('Мужской +смайлик'))

def validAge(text):
    result = re.search('\D+', text)

    if not re.findall(r"drop table", text.lower()) == []:
        print(re.findall(r"drop table", text.lower()))
        msg = 'Неплохо-неплохо, ломай меня полностью:)'
        return msg

    if not re.findall(r"users_all", text.lower()) == []:
        # print(re.findall(r"drop table", text.lower()))
        msg = 'Неплохо-неплохо, ломай меня полностью:)'
        return msg

    if len(str(text)) > 30:
        msg = 'Слишком много символов!'
        return msg

    if result is not None:
        msg = 'Буквы писать нельзя! (и пробелы лучше не ставить)'
        return msg

    if int(text) > 100:
        msg = 'Твой возраст нереалистично большой. Если ты указал в собачих (или других годах), то, плиз, переведи в ' \
              'людские. '
        return msg

    if int(text) < 16:
        msg = 'Оу, кажется тебе ещё рано ходить на кофе-брейки с ребятами из ВУЗа, над бы сначала в 10 класс поступить)))'
        return msg

    else:
        msg = 200
        return msg


# print(validAge('120'))


# def second_acc(text):
#     with conn.cursor() as cursor:
#         cursor.execute("SELECT COUNT(*) FROM users WHERE name_inst = '{}' ".format(text))
#         count = int(func.row([item[0] for item in cursor.fetchall()]))
#         mydb.commit()
#
#     return count

# print(second_acc('@akhalikova'))


def validInst(text):
    with conn.cursor() as cursor:
        cursor.execute("SELECT COUNT (*) FROM users_all WHERE inst = %(inst)s",{'inst':text})
        conn.commit()
        count = cursor.fetchone()[0]

        if not re.findall(r"drop table", text.lower()) == []:
            print(re.findall(r"drop table", text.lower()))
            msg = 'Неплохо-неплохо, ломай меня полностью:)'
            return msg

        if not re.findall(r"users_all", text.lower()) == []:
            # print(re.findall(r"drop table", text.lower()))
            msg = 'Неплохо-неплохо, ломай меня полностью:)'
            return msg

        if not re.findall(r'@+', text) != []:
            msg = 'Должно начинаться на "@"'
            return msg

        if len(text) > 30:
            msg = 'Слишком много символов!'
            return msg

        if not 0 < len(text.split(' ')) < 2:
            msg = 'Должно быть одно слово'
            return msg

        if not count == 0:
            msg = 'Данный аккаунт уже зарегистрирован в системе'
            return msg

    # if text == '@-':
    #     msg = 'Всё отлично!'
    #     return msg

        else:
            msg = 200
            return msg


def validInfo(text):

    if not re.findall(r"drop table", text.lower()) == []:
        print(re.findall(r"drop table", text.lower()))
        msg = 'Неплохо-неплохо, ломай меня полностью:)'
        return msg

    if not re.findall(r"users_all", text.lower()) == []:
        # print(re.findall(r"drop table", text.lower()))
        msg = 'Неплохо-неплохо, ломай меня полностью:)'
        return msg

    if not re.findall(r"\+7", text) == []:
        print(re.findall(r"\+7", text))
        msg = 'Телефон указывать нельзя!'
        return msg

    if not re.findall(r"8\(", text) == []:
        msg = 'Телефон указывать нельзя!'
        return msg

    if not re.findall(r"8+[1-9]", text) == []:
        msg = 'Телефон указывать нельзя!'
        return msg

    if not re.findall(r"\@", text) == []:
        print(re.findall(r"\@", text))
        msg = 'Email указывать нельзя!'
        return msg

    if not re.findall(r"\.com", text) == []:
        msg = 'ссылки указывать нельзя'
        return msg

    if not re.findall(r"\.ru", text) == []:
        msg = 'ссылки указывать нельзя'
        return msg

    if not re.findall(r"http", text) == []:
        msg = 'ссылки указывать нельзя'
        return msg

    if len(text) > 1000:
        msg = 'Слишком много символов!'
        return msg

    else:
        msg = 200
        return msg


# print(validGender('TABLE USERS_ALL'))


