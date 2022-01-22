#
#
# в этом файле храняться все функции

import os, sys

from os.path import dirname, join, abspath

sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from settings import conn, cursor


# --------------- если пользователь не в системе, то сразу отправляет на регистрацию-------
def new_session(chatid):
    cursor.execute("SELECT * FROM users_all WHERE chatid = {}".format(chatid))
    reg = cursor.fetchone()
    conn.commit()
    if reg is None:
        return False  # выводит если пользователя нет в системе
    else:
        return True  # выводит если пользователь есть в системе


# print(new_session(2322))


def check_all_attr(chatid):
    cursor.execute("SELECT COUNT (*) FROM users_all WHERE chatid = {}".format(chatid))
    count_chatid = [item[0] for item in cursor.fetchall()]
    conn.commit()
    # print(count_chatid[0])

    if count_chatid[0] == 1:

        cursor.execute("SELECT username FROM users_all WHERE chatid = {}".format(chatid))
        username = [item[0] for item in cursor.fetchall()]
        # print(username[0])
        conn.commit()

        try:
            if username[0] is None or username[0] == '':
                return False
            else:
                return True  # значит всё заполнено
        except:
            return False

    else:
        return False


# print(check_all_attr(1040880272))

def is_reg(chatid):
    cursor.execute("SELECT is_reg FROM users_all WHERE chatid = {}".format(chatid))
    is_reg = [item[0] for item in cursor.fetchall()]
    conn.commit()
    return is_reg[0]


