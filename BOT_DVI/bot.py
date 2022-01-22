import telebot
from PIL import Image
from telebot import types
import settings
import validation

from users import valid_reg

import texts
import main_menu
import dvi

from users.models import User, DVI, Potok

bot = telebot.TeleBot(settings.BotToken)  # бот API


@bot.message_handler(commands=['start'])
def starter(message):
    chat_id = message.chat.id
    tg_name = message.chat.username
    first_name = message.chat.first_name
    if first_name is None:
        first_name = 'Пользователь'
    print(chat_id)

    if valid_reg.is_reg(chat_id) == 404:  # эта функция проверяет есть ли этотт chatid в бд
        user = User(chat_id)
        user.create_user(tg_name, first_name)

        bot.send_message(chat_id, texts.text_start_first(first_name), parse_mode='html',
                         disable_web_page_preview=True, reply_markup=main_menu.start_menu())

    else:
        bot.send_message(chat_id, texts.text_start(first_name), parse_mode='html',
                         disable_web_page_preview=True, reply_markup=main_menu.start_menu())


#
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == 'back_main_menu':
        keyboard = main_menu.start_menu()
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(chat_id=call.message.chat.id,
                         text=texts.back_to_main_menu(call.message.chat.first_name),
                         reply_markup=keyboard, parse_mode='html')

    if call.data == 'date' or call.data == 'back_to_dvi':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=texts.date,
                              reply_markup=dvi.dvi(1), parse_mode='html')

    if call.data == 'preparation' or call.data == 'back_to_preparation':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=texts.preparation,
                              reply_markup=dvi.dvi_preparation(1), parse_mode='html')

    if call.data == 'about':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=texts.text_info,
                              reply_markup=main_menu.keyboard_back_to_menu(),
                              parse_mode='html', disable_web_page_preview=True)
    if call.data == 'help':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=texts.text_help,
                              reply_markup=main_menu.keyboard_back_to_menu(),
                              parse_mode='html', disable_web_page_preview=True)

    if call.data == 'spiski':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=texts.spiski,
                              reply_markup=main_menu.keyboard_back_to_menu(),
                              parse_mode='html', disable_web_page_preview=True)



    for i in list(range(100)):
        if call.data == 'page_{}'.format(i):  # переход на следующую страницу
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=texts.date,
                                  reply_markup=dvi.dvi(i), parse_mode='html')

        if call.data == 'dvi{}'.format(i):
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=texts.dvi_dates(i),
                                  reply_markup=dvi.dvi_potok(i), parse_mode='html')

        if call.data == 'potok{}'.format(i):
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=texts.data_potok(i), parse_mode='html', reply_markup=dvi.dvi_back())

        if call.data == 'page_{}_preparation'.format(i):  # переход на следующую страницу
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=texts.preparation,
                                  reply_markup=dvi.dvi_preparation(i), parse_mode='html')

        if call.data == 'dvi_preparation{}'.format(i):
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=texts.preparation_links,
                                  reply_markup=dvi.dvi_preparation_links(i), parse_mode='html')


bot.polling(none_stop=True, interval=1, timeout=10)
