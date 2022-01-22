import telebot
from telebot import types
import settings
import threading

from users import valid_reg
from users import users_msg
from users.models import User
import datetime

from users.models import Meeting
from users.models import User

bot = telebot.TeleBot(settings.BotToken)  # бот API


# def find_coffee(chatid):
#     bot.send_message(chatid, 'отправил сообщение')


# 323739054

# print(datetime.datetime.today().strftime("%m/%d/%Y"))
# print(datetime.datetime.today())

# print(datetime.datetime.now().strftime("%H"))

def rating_1(id):
    keyboard = types.InlineKeyboardMarkup()

    key_1 = types.InlineKeyboardButton(text='\U00002B50', callback_data=f'1_star_{id}_chatid1')
    key_2 = types.InlineKeyboardButton(text='\U00002B50\U00002B50', callback_data=f'2_star_{id}_chatid1')
    key_3 = types.InlineKeyboardButton(text='\U00002B50\U00002B50\U00002B50', callback_data=f'3_star_{id}_chatid1')
    key_4 = types.InlineKeyboardButton(text='\U00002B50\U00002B50\U00002B50\U00002B50',
                                       callback_data=f'4_star_{id}_chatid1')
    key_5 = types.InlineKeyboardButton(text='\U00002B50\U00002B50\U00002B50\U00002B50\U00002B50',
                                       callback_data=f'5_star_{id}_chatid1')
    key_back = types.InlineKeyboardButton(text='\U00002B05', callback_data='back_home')

    keyboard.add(key_5)
    keyboard.add(key_4)
    keyboard.add(key_3)
    keyboard.add(key_2)
    keyboard.add(key_1)
    keyboard.add(key_back)

    return keyboard


def rating_2(id):
    keyboard = types.InlineKeyboardMarkup()

    key_1 = types.InlineKeyboardButton(text='\U00002B50', callback_data=f'1_star_{id}_chatid2')
    key_2 = types.InlineKeyboardButton(text='\U00002B50\U00002B50', callback_data=f'2_star_{id}_chatid2')
    key_3 = types.InlineKeyboardButton(text='\U00002B50\U00002B50\U00002B50', callback_data=f'3_star_{id}_chatid2')
    key_4 = types.InlineKeyboardButton(text='\U00002B50\U00002B50\U00002B50\U00002B50',
                                       callback_data=f'4_star_{id}_chatid2')
    key_5 = types.InlineKeyboardButton(text='\U00002B50\U00002B50\U00002B50\U00002B50\U00002B50',
                                       callback_data=f'5_star_{id}_chatid2')
    key_back = types.InlineKeyboardButton(text='\U00002B05', callback_data='back_home')

    keyboard.add(key_5)
    keyboard.add(key_4)
    keyboard.add(key_3)
    keyboard.add(key_2)
    keyboard.add(key_1)
    keyboard.add(key_back)

    return keyboard


def rassilka2(list_id, list_chatid, i):
    global el

    try:
        for el in list(range(i + 1, len(list_chatid), 1)):  # для всех чисел в списке от 0 до кол-ва переданных el
            id_el = list_id[el]
            chatid_1_el = list_chatid[el][0]  # chatid первого
            chatid_2_el = list_chatid[el][1]  # chatid второго

            user1 = User(chatid_1_el)
            user2 = User(chatid_2_el)  # пользоваетль, который ищет партнёра

            info_1 = user1.all_information()
            info_2 = user2.all_information()

            bot.send_message(chatid_1_el, f"Недавно, я предлагал тебе встретиться с"
                                          f" <a href='https://t.me/{info_2[6]}/'>{info_2[0]}</a>", parse_mode='html',
                             disable_web_page_preview=True)
            bot.send_message(chatid_1_el, f'Оцении Вашу встречу: ', reply_markup=rating_1(id_el),
                             parse_mode='html', disable_web_page_preview=True)
            bot.send_message(chatid_2_el, f"Недавно, я предлагал тебе встретиться с"
                                          f" <a href='https://t.me/{info_1[6]}/'>{info_1[0]}</a>", parse_mode='html',
                             disable_web_page_preview=True)
            bot.send_message(chatid_2_el, f'Оцении Вашу встречу: ', reply_markup=rating_2(id_el),
                             parse_mode='html', disable_web_page_preview=True)
    except Exception:
        rassilka2(list_id, list_chatid, i=el)


def check_time():
    threading.Timer(3600.0, check_time).start()  # раз в час (3600 секунд) он делает проверку
    if datetime.datetime.now().strftime("%H") == '2':  # если сейчас кол-во часов равно 2 (2 часа ночи), то ...
        Meeting.update_time_notice()  # убираем дни до напоминания
    if datetime.datetime.now().strftime("%H") == '12':  # если сейчас кол-во часов равно 12 (12 часа дня), то ...
        list_meeting = Meeting.time_notice()
        list_id_meeting = Meeting.id_time_notice()
        rassilka2(list_id_meeting, list_meeting, -1)


check_time()
