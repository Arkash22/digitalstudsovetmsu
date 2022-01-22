import os, sys
from os.path import dirname, join, abspath

sys.path.insert(0, abspath(join(dirname(__file__), '..')))
import settings
from settings import conn, cursor
import datetime


class User:
    def __init__(self, chatid):
        self.chatid = chatid

    def create_user(self, telename, first_name):
        if telename is None and first_name is None:
            cursor.execute(
                "INSERT INTO users (chatid, tg_name, firstname) VALUES ({}, '@User', 'No_name')".format(
                    self.chatid))
            conn.commit()

        elif telename is None:
            cursor.execute(
                "INSERT INTO users (chatid, tg_name, firstname) VALUES ({}, '@User', '{}')".format(
                    self.chatid, first_name))
            conn.commit()

        elif first_name is None:
            cursor.execute(
                "INSERT INTO users (chatid, tg_name, firstname) VALUES ({}, '{}', 'No_name')".format(
                    self.chatid, telename))
            conn.commit()

        else:
            cursor.execute(
                "INSERT INTO users (chatid, tg_name, firstname) VALUES ({}, '{}', '{}')".format(
                    self.chatid, telename, first_name))
            conn.commit()

    def tg_username(self):
        cursor.execute("SELECT tg_name FROM users WHERE chatid = {}".format(self.chatid))
        tg_username = cursor.fetchone()
        conn.commit()
        if tg_username[0] is None:
            return 'User'
        else:
            return tg_username[0]

    def firstname(self):
        cursor.execute("SELECT first_name FROM users WHERE chatid = {}".format(self.chatid))
        firstname = cursor.fetchone()
        conn.commit()
        if firstname[0] is None:
            return 'Пользователь'
        else:
            return firstname[0]

    def update_firstname(self, firstname):
        cursor.execute("UPDATE users SET first_name = '{}' where chatid = {}".format(firstname, self.chatid))
        conn.commit()

    def all_information(self):
        firstname = self.firstname()
        tg_username = self.tg_username()
        return firstname, tg_username, telephone, email


class DVI:
    def __init__(self, id):
        self.id = id

    def name(self):
        cursor.execute("SELECT name FROM dvi WHERE id = {}".format(self.id))
        name = cursor.fetchone()
        conn.commit()
        if name[0] is None:
            return 'Не найдено'
        else:
            return name[0]

    def potok_names(self):
        cursor.execute("SELECT name FROM dvi_potok WHERE id_dvi = {} order by time".format(self.id))
        name = [item[0] for item in cursor.fetchall()]
        conn.commit()

        return name

    def potok_ids(self):
        cursor.execute("SELECT id FROM dvi_potok WHERE id_dvi = {} order by time".format(self.id))
        ids = [item[0] for item in cursor.fetchall()]
        conn.commit()

        return ids

    def potok_dates(self):
        cursor.execute("SELECT time FROM dvi_potok WHERE id_dvi = {} order by time".format(self.id))
        date = [item[0] for item in cursor.fetchall()]
        conn.commit()

        return date

    def preparation_links(self):
        cursor.execute("SELECT link FROM preparation WHERE id_dvi = {}".format(self.id))
        links = [item[0] for item in cursor.fetchall()]
        conn.commit()

        return links

    def preparation_links_names(self):
        cursor.execute("SELECT name FROM preparation WHERE id_dvi = {}".format(self.id))
        names = [item[0] for item in cursor.fetchall()]
        conn.commit()

        return names


class Potok:
    def __init__(self, id):
        self.id = id

    def data(self):
        cursor.execute("SELECT time FROM dvi_potok WHERE id = {}".format(self.id))
        date = [item[0] for item in cursor.fetchall()]
        conn.commit()

        day = date[0].day
        month = date[0].month
        time = f'{date[0].hour}:{date[0].minute}0'

        if month == 7:
            month = 'июля'
        elif month == 8:
            month = 'августа'

        return str(day) + ' ' + month + ' ' + time




# dvi_1 = DVI(1)
#
# print(dvi_1.preparation_links())
# print(dvi_1.preparation_links_names())

# potok = Potok(16)
#
# print(potok.data())

# user = User(323739054)
# print(user.all_information())
# user = User(775199948)
# print(user.telename())
# print(user.telename(), user.instagram(), user.info(), user.gender(), user.status())
# print(user.in_search())
# user.update_gender(3)
# print(user.gender())
