import os, sys
from os.path import dirname, join, abspath

sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from settings import conn, cursor


def is_reg(chatid):
    cursor.execute("SELECT * FROM users WHERE chatid = {}".format(chatid))
    is_reg = cursor.fetchone()
    conn.commit()
    # print(is_reg)
    if is_reg == None:
        return 404
    else:
        return 0



# print(is_reg(323739054))
