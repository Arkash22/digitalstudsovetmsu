#
#
# в этом файле храняться все модели

import os, sys
from os.path import dirname, join, abspath

sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from settings import conn, cursor


class User:
    def __init__(self, chatid):
        self.chatid = chatid

    def faculty(self):
        cursor.execute("SELECT faculty_id FROM users_all WHERE chatid = {}".format(self.chatid))
        faculty_id = cursor.fetchone()
        conn.commit()

        cursor.execute("SELECT name FROM faculty WHERE id = {}".format(faculty_id[0]))
        faculty_name = [item[0] for item in cursor.fetchall()]
        conn.commit()

        return faculty_name[0]

    def faculty_id(self):
        try:
            cursor.execute("SELECT faculty_id FROM users_all WHERE chatid = {}".format(self.chatid))
            faculty_id = cursor.fetchone()
            conn.commit()
            return faculty_id[0]
        except:
            pass

    def program(self):

        cursor.execute("SELECT program_id FROM users_all WHERE chatid = {}".format(self.chatid))
        program_id = cursor.fetchone()
        conn.commit()

        cursor.execute("SELECT name FROM faculty_programs WHERE id = {}".format(program_id[0]))
        program_name = cursor.fetchone()
        conn.commit()

        return program_name[0]

    def program_id(self):
        try:
            cursor.execute("SELECT \"program_id\" FROM users_all WHERE chatid = {}".format(self.chatid))
            program_id = cursor.fetchone()
            conn.commit()
            return program_id[0]

        except:
            cursor.execute("SELECT program_id FROM users_all WHERE chatid = {}".format(self.chatid))
            program_id = cursor.fetchone()
            conn.commit()
            return program_id[0]

    def username(self):
        cursor.execute("SELECT username FROM users_all WHERE chatid = {}".format(self.chatid))
        username = cursor.fetchone()
        conn.commit()

        return username[0]

    def is_teacher(self):
        cursor.execute("SELECT is_teacher FROM users_all WHERE chatid = {}".format(self.chatid))
        is_teacher = cursor.fetchone()
        conn.commit()

        return is_teacher[0]

    def create_user(self, telename):
        cursor.execute(
            "INSERT INTO users_all (chatid, username, is_student, is_entrant, tg_name,is_teacher) VALUES ({}, null, null, null, '{}',null)".format(
                self.chatid, telename))
        conn.commit()

    def update_faculty_id(self, faculty_id):
        cursor.execute("UPDATE users_all SET faculty_id = {} where chatid = {}".format(faculty_id, self.chatid))
        conn.commit()

    def update_program_id(self, program_id):
        cursor.execute("UPDATE users_all SET \"program_id\" = '{}' where chatid = {}".format(program_id, self.chatid))
        conn.commit()

    def update_username(self, username):
        cursor.execute("UPDATE users_all SET username = '{}' where chatid = {}".format(username, self.chatid))
        conn.commit()

    def update_student(self):
        cursor.execute("UPDATE users_all SET is_student = TRUE where chatid = {}".format(self.chatid))
        conn.commit()
        cursor.execute("UPDATE users_all SET is_entrant = FALSE where chatid = {}".format(self.chatid))
        conn.commit()

    def update_entrant(self):
        cursor.execute("UPDATE users_all SET is_entrant = TRUE where chatid = {}".format(self.chatid))
        conn.commit()
        cursor.execute("UPDATE users_all SET is_student = FALSE where chatid = {}".format(self.chatid))
        conn.commit()

    def update_not_entrant(self):
        cursor.execute("UPDATE users_all SET is_entrant = FALSE where chatid = {}".format(self.chatid))
        conn.commit()
        cursor.execute("UPDATE users_all SET is_student = FALSE where chatid = {}".format(self.chatid))
        conn.commit()

    def update_reg(self):
        cursor.execute("UPDATE users_all SET is_reg = TRUE where chatid = {}".format(self.chatid))
        conn.commit()


#
user = User(323739054)
# # # user.create_user('ffff')
# # user.update_faculty_id('2')
print(user.faculty_id())
# print(user.program())
# print(user.username())
