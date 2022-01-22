from telebot import types
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
import settings


def start_menu():
    keyboard = InlineKeyboardMarkup()
    key_1 = InlineKeyboardButton('\U0001F50E Узнать дату', callback_data='date')
    key_2 = InlineKeyboardButton('\U0001F4DA Подготовка к ДВИ', callback_data='preparation')
    key_3 = InlineKeyboardButton('\U0001F4DC Регламент ДВИ', url='http://cpk.msu.ru/files/2021/regulations_dvi.pdf')
    key_4 = InlineKeyboardButton('\U0001F4C4 Списки',  callback_data='spiski')

    key_5 = types.InlineKeyboardButton(text='\U00002699', callback_data='help')
    key_6 = InlineKeyboardButton('ЧАТ', url='https://t.me/entrant_msu')
    key_7 = InlineKeyboardButton('\U00002139', callback_data='about')

    keyboard.add(key_1)
    keyboard.add(key_2)
    keyboard.add(key_3, key_4)
    keyboard.add(key_5, key_6, key_7)


    return keyboard


def keyboard_back_to_menu():
    keyboard = InlineKeyboardMarkup()
    key_1 = InlineKeyboardButton('<<<', callback_data='back_main_menu')
    keyboard.add(key_1)

    return keyboard


def keyboard_back_to_dvi():
    keyboard = InlineKeyboardMarkup()
    key_1 = InlineKeyboardButton('<<<', callback_data='back_dvi')
    keyboard.add(key_1)

    return keyboard
