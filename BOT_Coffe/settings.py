import psycopg2
import os, sys
import datetime

conn = psycopg2.connect(dbname='', user='',
                        password='', host='')
# cursor = conn.cursor()  # обращаться будем через курсор

BotToken = ''  # @coffee_friend_bot

# BotToken = ''  # @softu_test_bot:

text_help = '<b>Контакты поддержки:</b>\n\n' \
            '\U0001F310"Наш сайт - <a href="https://vk.link/digitalstudsovetmsu">сайт сообщества в ВК</a> \n' \
            '\U0000260EТелефон: +7(964)723-56-82\n\U0001F4E7' \
            'Email: digital@studsovet.msu.ru\n' \
            '\U0001F468\U0000200D\U0001F4BBТехнический директор - @AVFroym'

text_info = '\U00002139<b> Немного о Coffee Friend!</b>' \
            '\n\n Этот бот был разработан и запущен командой <a href="https://vk.link/digitalstudsovetmsu">Комитета ' \
            'по цифровому развитию</a>, чтобы ты мог(ла) найти себе интересного собеседника, который учится/учился/будет учиться в МГУ.' \
            ' Мы понимаем важность окружения в нашей жизни, поэтому надеемся, что данный бот станет крутым ' \
            'инструментом нетворкинга для тебя и ещё множетсва людей из экосистемы нашей Alma Mater. \n\n' \
            '<i>Кофе — это просто счастье… и это счастье можно пить… (Иммануил Кант) </i> \n' \
            '<i>Кофе - это удивительный напиток, который согревает весь мир. (Дэвид Юм) </i>\n' \
            '<i>Кофе укрепляет чрево, способствует желудку в варении пищи, засорившуюся внутренность очищает, согревает живот. (Карл Линней) </i>\n' \
            '<i>А когда ей становилось грустно, она пила крепкий кофе и вспоминала его улыбку. (Иммануил Кант)</i> \n' \
            '<i>Дайте мне достаточное количество кофе, и я смогу управлять миром. (Ричард Брэнсон) </i>\n\n' \
            ' <i>- Но когда же вы спите? </i>\n' \
            '<i> - Да уж, сплю! Спать я буду когда окончу образование. А пока я пью чёрный кофе. (Франц Кафка)</i>\n\n' \
            '<code>P.s. Пользуйтесь ботом и оставляйте свои коментарии/замечания/благодарности в нашей группе в ВК.</code>'


def go_coffee(chatid_1):
    with conn.cursor() as cursor:
        cursor.execute(f"SELECT ALL chatid FROM users_all WHERE NOT chatid ={chatid_1} AND in_search = TRUE")
        chatid_2 = cursor.fetchone()
        conn.commit()

    if not chatid_2 is None:
        return chatid_2[0]
    else:
        return 404


# print(go_coffee(323739054))
#
#
# cursor.execute(
#     "SELECT chatid_1, chatid_2 FROM meetings GROUP BY chatid_1, chatid_2 HAVING chatid_1 =1 or  chatid_2 =1;")
# result = cursor.fetchall()
# conn.commit()
# print(result)
# new_res = []
# for x in result:
#     for i in x:
#         if i != 1:
#             new_res.append(i)
# print(tuple(new_res))

def go_coffee(chatid_1):
    with conn.cursor() as cursor:
        cursor.execute(
            f"SELECT chatid_1, chatid_2 FROM meetings GROUP BY chatid_1, chatid_2 HAVING chatid_1 = {chatid_1} or  chatid_2 ={chatid_1};")
        last_pars = cursor.fetchall()  # находит все пары где был задействован первый пользователь
        conn.commit()

        last_partners = [chatid_1]

        for users in last_pars:
            for i in users:
                if i != chatid_1:
                    last_partners.append(i)
        bd_last_partners = tuple(last_partners)
        print(bd_last_partners)

        if len(bd_last_partners) == 1:
            cursor.execute(
                f"SELECT ALL chatid FROM users_all WHERE NOT chatid = {bd_last_partners[0]} AND in_search = TRUE ")
            chatid_2 = cursor.fetchone()
            conn.commit()

            if not chatid_2 is None:
                chatid_2_new = []
                chatid_2_new.append(chatid_2[0])
                return chatid_2_new
            else:
                return 404
        else:

            cursor.execute(
                f"SELECT ALL chatid FROM users_all WHERE NOT chatid in {bd_last_partners} AND in_search = TRUE")
            chatid_2 = cursor.fetchall()
            conn.commit()

            if not chatid_2 is None:
                chatid_2_new = []
                for i in chatid_2:
                    chatid_2_new.append(i[0])
                return chatid_2_new

            else:
                return 404


def block_time(chatid):
    with conn.cursor() as cursor:
        cursor.execute("SELECT time_block FROM block_time WHERE chatid = %(chatid)s", {'chatid': chatid})
        time = cursor.fetchone()
        conn.commit()

        if time[0] is None:
            return True
        else:
            time_delta = datetime.datetime.now() - time[0]
            # print(time_delta.days)
            if time_delta.days >= 3:
                return True
            else:
                return False

# print(block_time(323739054))

# #
# print(go_coffee(323739054))
