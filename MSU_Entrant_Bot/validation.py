import re
import settings


def validFIO(text):
    settings.cursor.execute("SELECT COUNT (*) FROM users_all WHERE username = '{}'".format(text))
    settings.conn.commit()
    count = settings.cursor.fetchone()[0]
    # print(count)
    # print(text)
    # print(text.split(' '))
    result = re.findall(r'\d', text)
    if result != []:
        msg = 'Числа писать нельзя!'
        return msg

    if len(text) > 30:
        msg = 'Слишком много символов!'
        return msg

    if not 1 < len(text.split(' ')) < 4:
        msg = 'Укажите и Имя и Фамилию'
        return msg

    if not count == 0:
        msg = 'Данные ФИО уже заняты, возможно, ты регистрировался на другой платформе!'
        return msg

    else:
        msg = 'Всё отлично!'
        return msg


def validPassword(text):
    if len(text) > 30:
        msg = 'Слишком много символов!'
        return msg

    if len(text) < 6:
        msg = 'Пароль должен быть длинее 6 символов'
        return msg

    else:
        msg = 'Всё отлично!'
        return msg


#
# print(validFIO(text='Аркадий Фройм'))

def validDeadline_date(text):
    # print(text)
    # print(text.split(' '))
    result = re.findall(r'\d', text)
    if not result != []:
        msg = 'Буквы писать нельзя!'
        return msg

    if len(text) > 6:
        msg = 'Слишком много символов!'
        return msg

    if not re.findall(r'\d{2}\.\d{2}', text) != []:
        msg = 'Должен быть разделительный знак "."'
        return msg

    else:
        list_dead_day = text.split('.')
        day_d = list_dead_day[0]
        month_d = list_dead_day[1]
        if 0 < int(day_d) <= 31 and 0 < int(month_d) <= 12:
            msg = 'Всё отлично!'
        else:
            msg = 'не правильно указана дата!'
        return msg


# print(validDeadline(text='31.12'))

def validDeadline_time(text):
    # print(text)
    # print(text.split(' '))
    result = re.findall(r'\d', text)
    if not result != []:
        msg = 'Буквы писать нельзя!'
        return msg

    if len(text) > 5:
        msg = 'Слишком много символов!'
        return msg

    if not re.findall(r'\d{1,2}:\d{2}', text) != []:
        msg = 'Должен быть разделительный знак ":"'
        return msg

    else:
        list_dead_day = text.split(':')
        hours = list_dead_day[0]
        mins = list_dead_day[1]
        if 0 <= int(hours) < 24 and 00 <= int(mins) < 60:
            msg = 'Всё отлично!'
        else:
            msg = 'не правильно указана дата!'
        return msg

# print(validDeadline_time(text='00:00'))
