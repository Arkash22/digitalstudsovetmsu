import os, sys
from os.path import dirname, join, abspath

sys.path.insert(0, abspath(join(dirname(__file__), '..')))
import settings
from settings import conn
import datetime


class User:
    def __init__(self, chatid):
        self.chatid = chatid

    def create_user(self, telename):
        with conn.cursor() as cursor:
            if telename is None:
                cursor.execute(
                    "INSERT INTO users_all (chatid, status, tg_name, first_name, photo_id, inst, info, gender, age, in_search, is_reg) VALUES (%(chatid)s, 404, 'User', null, null, null, null ,null ,null, FALSE ,0)",
                    {'chatid': self.chatid, })
                conn.commit()
            else:
                cursor.execute(
                    "INSERT INTO users_all (chatid, status, tg_name, first_name, photo_id, inst, info, gender, age, in_search, is_reg) VALUES (%(chatid)s, 404, %(tg_name)s, null,  null, null, null ,null ,null, FALSE ,0)",
                    {'chatid': self.chatid, 'tg_name': telename})
                conn.commit()

    def create_block_time(self):
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO block_time (chatid, time_block) VALUES (%(chatid)s, null)",  {'chatid': self.chatid})
            conn.commit()

    def update_block_time(self):
        with conn.cursor() as cursor:
            # print(datetime.datetime.now())
            cursor.execute("UPDATE block_time SET time_block = %(time)s where chatid = %(chatid)s",
                           {'time': datetime.datetime.now(), 'chatid': self.chatid})
            conn.commit()


    def tg_username(self):
        with conn.cursor() as cursor:
            cursor.execute("SELECT tg_name FROM users_all WHERE chatid = %(chatid)s", {'chatid': self.chatid})
            tg_username = cursor.fetchone()
            conn.commit()
            if tg_username[0] is None:
                return 'User'
            else:
                return tg_username[0]

    def update_tg_username(self, tg_name):
        with conn.cursor() as cursor:
            cursor.execute("UPDATE users_all SET tg_name = %(tg_name)s where chatid = %(chatid)s",
                           {'tg_name': tg_name, 'chatid': self.chatid})
            conn.commit()

    def firstname(self):
        with conn.cursor() as cursor:
            cursor.execute("SELECT first_name FROM users_all WHERE chatid = %(chatid)s", {'chatid': self.chatid})
            firstname = cursor.fetchone()
            conn.commit()
            if firstname[0] is None:
                return 'Пользователь'
            else:
                return firstname[0]

    def update_firstname(self, firstname):
        with conn.cursor() as cursor:
            cursor.execute("UPDATE users_all SET first_name = %(first_name)s where chatid = %(chatid)s",
                           {'first_name': firstname, 'chatid': self.chatid})
            conn.commit()

    def gender(self):
        with conn.cursor() as cursor:
            cursor.execute("SELECT gender FROM users_all WHERE chatid = %(chatid)s", {'chatid': self.chatid})
            gender = cursor.fetchone()
            conn.commit()
            return gender[0]

    def update_gender(self, gender):
        with conn.cursor() as cursor:
            cursor.execute("UPDATE users_all SET gender = %(gender)s where chatid = %(chatid)s",
                           {'chatid': self.chatid, 'gender': gender})
            conn.commit()

    def age(self):
        with conn.cursor() as cursor:
            cursor.execute("SELECT age FROM users_all WHERE chatid = %(chatid)s", {'chatid': self.chatid})
            age = cursor.fetchone()
            conn.commit()

        return age[0]

    def update_age(self, age):
        with conn.cursor() as cursor:
            cursor.execute("UPDATE users_all SET age = %(age)s where chatid = %(chatid)s",
                           {'age': age, 'chatid': self.chatid})
            conn.commit()

    def status(self):
        with conn.cursor() as cursor:
            cursor.execute("SELECT status FROM users_all WHERE chatid = %(chatid)s", {'chatid': self.chatid})
            status = cursor.fetchone()
            conn.commit()

        if status[0] == 1:
            user_status = 'Студент'
        elif status[0] == 2:
            user_status = 'Аспирант/преподаватель'
        elif status[0] == 3:
            user_status = 'Абитуриент/школьник'
        elif status[0] == 404:
            user_status = 404

        return user_status

    def update_status(self, status):
        with conn.cursor() as cursor:
            cursor.execute("UPDATE users_all SET status = %(status)s  where chatid = %(chatid)s",
                           {'status': status, 'chatid': self.chatid})
            conn.commit()

    def photo_id(self):
        with conn.cursor() as cursor:
            cursor.execute("SELECT photo_id FROM users_all WHERE chatid = %(chatid)s", {'chatid': self.chatid})
            photo_id = cursor.fetchone()
            conn.commit()
            return photo_id[0]

    def update_photo_id(self, photo_id):
        with conn.cursor() as cursor:
            cursor.execute("UPDATE users_all SET photo_id = %(photo_id)s where chatid = %(chatid)s",
                           {'chatid': self.chatid})
            conn.commit()

    def instagram(self):
        with conn.cursor() as cursor:
            cursor.execute("SELECT inst FROM users_all WHERE chatid = %(chatid)s", {'chatid': self.chatid})
            instagram = cursor.fetchone()
            conn.commit()

        return instagram[0]

    def update_instagram(self, inst):
        with conn.cursor() as cursor:
            cursor.execute("UPDATE users_all SET inst = %(inst)s where chatid = %(chatid)s",
                           {'inst': inst, 'chatid': self.chatid})
            conn.commit()

    def info(self):
        with conn.cursor() as cursor:
            cursor.execute("SELECT info FROM users_all WHERE chatid = %(chatid)s", {'chatid': self.chatid})
            info = cursor.fetchone()
            conn.commit()

        return info[0]

    def update_info(self, info):
        with conn.cursor() as cursor:
            cursor.execute("UPDATE users_all SET info = %(info)s where chatid = %(chatid)s",
                           {'info': info, 'chatid': self.chatid})
            conn.commit()

    def in_search(self):
        with conn.cursor() as cursor:
            cursor.execute("SELECT in_search FROM users_all WHERE chatid = %(chatid)s", {'chatid': self.chatid})
            in_search = cursor.fetchone()
            conn.commit()
            return in_search[0]

    def update_in_search(self, in_search):
        with conn.cursor() as cursor:
            cursor.execute("UPDATE users_all SET in_search = %(in_search)s where chatid = %(chatid)s",
                           {'in_search': in_search, 'chatid': self.chatid})
            conn.commit()

    def update_reg(self):
        with conn.cursor() as cursor:
            cursor.execute("UPDATE users_all SET is_reg = 1 where chatid = %(chatid)s", {'chatid': self.chatid})
            conn.commit()

    def all_information(self):
        firstname = self.firstname()
        status = self.status()
        instagram = self.instagram()
        info = self.info()
        gender = self.gender()
        age = self.age()
        tg_username = self.tg_username()

        return firstname, gender, age, status, instagram, info, tg_username



# user = User(777)
# print(user.update_block_time())


# print(user.all_information())
# user = User(775199948)
# print(user.telename())
# print(user.telename(), user.instagram(), user.info(), user.gender(), user.status())
# print(user.in_search())
# user.update_gender(3)
# print(user.gender())


class Meeting:
    def __init__(self, id):
        self.id = id

    def create_meeting(chatid1, tg_name_1, chatid2, tg_name_2):
        with conn.cursor() as cursor:
            today = datetime.datetime.today().strftime('%Y-%m-%d')
            cursor.execute(
                f"INSERT INTO meetings (chatid_1, tg_name_1, rating_1, chatid_2, tg_name_2, rating_2, comment_1, comment_2, time_create, time_notice) "
                f"VALUES ({chatid1}, '{tg_name_1}' ,null, {chatid2}, '{tg_name_2}' ,null,  null, null, '{today}', 3)")
            conn.commit()

    def update_rating_1(self, rating):
        with conn.cursor() as cursor:
            cursor.execute("UPDATE meetings SET rating_1= %(rating_1)s where id = %(id)s",
                           {'rating_1': rating, 'chatid': self.id})
            conn.commit()

    def update_rating_2(self, rating):
        with conn.cursor() as cursor:
            cursor.execute("UPDATE meetings SET rating_2= %(rating_2)s where id = %(id)s",
                           {'rating_2': rating, 'chatid': self.id})
            conn.commit()

    def update_comment_1(self, comment):
        with conn.cursor() as cursor:
            cursor.execute("UPDATE meetings SET comment_1= %(comment)s where id = %(id)s",
                           {'comment': comment, 'chatid': self.id})
            conn.commit()

    def update_comment_2(self, comment):
        with conn.cursor() as cursor:
            cursor.execute("UPDATE meetings SET comment_2= %(comment)s where id = %(id)s",
                           {'comment': comment, 'chatid': self.id})
            conn.commit()

    def update_time_notice():
        with conn.cursor() as cursor:
            cursor.execute("SELECT id FROM meetings ")
            all_id = cursor.fetchall()
            conn.commit()
            id_list = []
            print(all_id)
            for el in all_id:
                id_list.append(el[0])
            print(id_list)

            for id in id_list:
                cursor.execute("SELECT time_notice FROM meetings where id = {}".format(id))
                time_notice = cursor.fetchone()
                conn.commit()
                if time_notice[0] > -1:
                    update_time_notice = time_notice[0] - 1
                    cursor.execute("UPDATE meetings SET time_notice = %(time)s where id = %(id)s",
                                   {'time': update_time_notice, 'id': id})
                    conn.commit()

    def time_notice():
        with conn.cursor() as cursor:
            cursor.execute("SELECT id FROM meetings where time_notice = 1 ")
            all_id = cursor.fetchall()
            conn.commit()
            id_list = []
            for el in all_id:
                id_list.append(el[0])
            meeting_id = []
            for id in id_list:
                cursor.execute("SELECT chatid_1, chatid_2 FROM meetings where id = %(id)s", {'id': id})
                chat_id_meeting = cursor.fetchone()
                conn.commit()
                meeting_id.append(chat_id_meeting)

            return meeting_id

    def id_time_notice():
        with conn.cursor() as cursor:
            cursor.execute("SELECT id FROM meetings where time_notice = 1 ")
            all_id = cursor.fetchall()
            conn.commit()
            id_list = []
            for el in all_id:
                id_list.append(el[0])

            return id_list

#
# m = Meeting(4)
# print(Meeting.id_time_notice())
# print(Meeting.time_notice())
# m.update_rating_1(3)
# m.create_meeting(2323, 565465)

# print(datetime.datetime.today().strftime('%Y-%m-%d'))
