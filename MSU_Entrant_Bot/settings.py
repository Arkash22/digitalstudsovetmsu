import psycopg2
import os, sys

conn = psycopg2.connect(dbname='', user='',
                        password='', host='')
cursor = conn.cursor()  # обращаться будем через курсор

BotToken = ''  # @msu_entrant_bot

text_starter = "Привет! Меня зовут <b> MSU Entrant Bot </b> \U0001F44B" \
               "\n \nЯ буду твоим личным помощником при поступлении в МГУ. С моей помощью ты сможешь посмотреть " \
               "проходные баллы на интересующий тебя факультет, подготовиться к ДВИ, подать документы/связаться с " \
               "администрацией факультета и найти новые знакомства из числа абитуриентов."

text_help = '<b>Контакты поддержки:</b>\n\n' \
            '\U0001F310"Наш сайт - <a href="https://vk.link/digitalstudsovetmsu">сайт сообщества в ВК</a> \n' \
            '\U0000260EТелефон: +7(964)723-56-82\n\U0001F4E7' \
            'Email: digital@studsovet.msu.ru\n' \
            '\U0001F468\U0000200D\U0001F4BBТехнический директор - @AVFroym'

text_info = '\U00002139<b> Немного о боте!</b>' \
            '\n\n Этот бот был разработан и запущен командой <a href="https://vk.link/digitalstudsovetmsu">Комитета ' \
            'по цифровому развитию</a> с целью помочь ВАМ (абитурентам) с поступлением в нашу Alma Mater. ' \
            'Разработчики этого приложения также как и ВЫ совсем недавно поступали в ВУЗ и боялись провалить ДВИ. В ' \
            'МГУ, и вправду, попасть не так просто, но МЫ верим, что все ВАШИ усилия, направленне на поступление в наш ' \
            'ВУЗ, не пройдут зря, и ВЫ очень скоро увидите свою фамилию в приказе о зачислении. \n\n' \
            '<i>P.s. Пользуйтесь ботом и оставляйте свои коментарии/замечания/благодарности в нашей группе в ВК.</i>'


def all_faculties():
    try:
        with conn:
            with conn.cursor():
                cursor.execute("SELECT name FROM faculty")
                faculties = [item[0] for item in cursor.fetchall()]
                conn.commit()

                cursor.execute("SELECT id FROM faculty")
                faculties_id = [item[0] for item in cursor.fetchall()]
                conn.commit()

                result = list(filter(None, faculties))
                result_2 = list(filter(None, faculties_id))
    except:
        result = 'error'
        result_2 = 'error'

    return result, result_2


#
# print(all_faculties())


def all_program(faculty_id):
    all_names_list = []
    all_id_list = []
    try:
        with conn:
            with conn.cursor():
                cursor.execute("SELECT name , id FROM faculty_programs WHERE faculty_id = {}".format(faculty_id))
                program = cursor.fetchall()
                conn.commit()

                for i in list(range(0, len(program))):
                    all_names_list.append(program[i][0])
                    all_id_list.append(program[i][1])

            return all_names_list, all_id_list
    except:
        program = 'не найдено'
        return program


# print(all_program('2'))


def all_dvi(program_id):
    cursor.execute("SELECT dvi_list FROM faculty_programs WHERE id = {}".format(program_id))
    dvi_list = [item[0] for item in cursor.fetchall()]
    conn.commit()

    try:
        ege_subjects = dvi_list[0].split(';')

        length = len(ege_subjects)

        if length == 1:
            return ege_subjects[0]
        else:
            result = []
            for i in list(range(length)):
                result.append(ege_subjects[i])
            return result

    except Exception:
        return dvi_list


# print(all_faculties())

# print(all_dvi('1'))

# for i in all_dvi('МШЭ'):
#     print(i)


def new_func(faculty_id):
    try:
        with conn:
            with conn.cursor():
                cursor.execute("SELECT name , id FROM faculty_programs WHERE faculty_id = {}".format(faculty_id))
                program = cursor.fetchall()[0]
                conn.commit()

                return program
    except:
        program = 'не найдено'
        return program

# print(all_program(1))

# for i in all_program(1):
#     print(i)
