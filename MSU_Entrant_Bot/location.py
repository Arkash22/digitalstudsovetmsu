import math
import sys
from os.path import dirname, join, abspath
from telebot import types
from settings import conn, cursor
# from . import  EmojiAlphabet

sys.path.insert(0, abspath(join(dirname(__file__), '..')))



def geo_data(faculty_id):
    cursor.execute("SELECT latitude FROM faculty WHERE id = '{}'".format(faculty_id))
    latitude = [item[0] for item in cursor.fetchall()]
    conn.commit()

    cursor.execute("SELECT longitude FROM faculty WHERE id = '{}'".format(faculty_id))
    longitude = [item[0] for item in cursor.fetchall()]
    conn.commit()

    return latitude[0], longitude[0]

# print(geo_data('1'))