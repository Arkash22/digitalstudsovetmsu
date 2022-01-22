# import telebot
# from telebot import types
# import settings
# import threading
#
# from users import valid_reg
# from users import users_msg
# from users.models import User
# import datetime
#
# from users.models import Meeting
# from users.models import User
#
# import settings
# from settings import conn, cursor
# import datetime
#
# bot = telebot.TeleBot(settings.BotToken)  # бот API


# def all_id():
#     cursor.execute("SELECT chatid FROM users_all WHERE tg_name = 'User'")
#     list_id = cursor.fetchall()
#     conn.commit()
#
#     new_list = []
#
#     for i in list_id:
#         new_list.append(i[0])
#
#     return new_list
#
#
# print(all_id())
#
#
# def all_names_user(list_id, i):
#     text = 'Важное сообщение\U00002757\n\n Если ты его читаешь, то к тебе обращается напрямую создатель бота, и это ' \
#            'совсем не очередное сообщение) Короче, у тя нет логина в Telegram и из-за этого пользователи не могут ' \
#            'тебе писать в ЛС. Тебе нужно или его создать в настройках, или там же в настройках изменить параметры ' \
#            'конфиденциальности!\n\n Желаю ярких и интересных собеседников, которые могут тебя найти)))'
#     try:
#
#         for el in list(range(i + 1, len(list_id), 1)):
#             print(el)
#             bot.send_message(list_id[el], text, parse_mode='html', disable_web_page_preview=True)
#
#     except Exception:
#         all_names_user(list_id, i=el)
#
#
# all_names_user(all_id(), 0)

# 565457257

# def send_message(chatid):
#     text = 'Чувак ты очень крут\U00002757\n\n Я вижу как ты в БД поменял себе гендер на вертолёт и чуть не слил всю ' \
#            'базу, напиши мне @AVFroym в тг, хочу пообщаться и прокачаться в вопросе безопасности)'
#
#     bot.send_message(chatid, text, parse_mode='html', disable_web_page_preview=True)
#
#
# send_message(565457257)
