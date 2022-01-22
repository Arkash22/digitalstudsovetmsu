import os, sys
from os.path import dirname, join, abspath

sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from settings import conn


def is_reg(chatid):
    with conn.cursor() as cursor:
        cursor.execute("SELECT is_reg FROM users_all WHERE chatid = %(chatid)s", {'chatid': chatid})
        is_reg = cursor.fetchone()
        conn.commit()
        # print(is_reg)
    if is_reg == None:
        return 404
    elif is_reg == (0,):
        return 0
    elif is_reg == (1,):
        return 1


#
# print(is_reg(323739051))


def is_time_block(chatid):
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM block_time WHERE chatid = %(chatid)s", {'chatid': chatid})
        time_block = cursor.fetchone()
        conn.commit()

    if time_block == None:
        return 404
    else:
        return 200

# print(is_time_block(323739051))