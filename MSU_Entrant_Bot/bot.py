import telebot
from telebot import types
import settings
import validation
import main_menu
import selection_committee as sc
import ege
import dvi
import location
import lk
import entrance
from settings import conn, cursor

from users import func_main
from users import users_msg
from users.models import User

bot = telebot.TeleBot(settings.BotToken)  # бот API


@bot.message_handler(commands=['start'])
def starter(message):
    chat_id = message.chat.id
    print(chat_id)

    if not func_main.new_session(chat_id):  # эта функция проверяет есть ли этотт chatid в бд
        user = User(chat_id)
        user.create_user(message.chat.username)
        bot.send_message(chat_id, 'В Боте ведуться технические работы \U000026A0 \n\n <i>Приносим свои извинения за предоставленные неудобства, скоро будет только лучше!</i> ', parse_mode='html', disable_web_page_preview=True)
        # bot.send_message(chat_id, settings.text_starter, parse_mode='html', disable_web_page_preview=True)
        # bot.send_message(chat_id, users_msg.home()[1],
        #                  reply_markup=users_msg.home()[0])

    else:
        if not func_main.check_all_attr(chat_id):
            bot.send_message(chat_id,
                         'В Боте ведуться технические работы \U000026A0 \n\n <i>Приносим свои извинения за предоставленные неудобства, скоро будет только лучше!</i> ',
                         parse_mode='html', disable_web_page_preview=True)
        #     bot.send_message(chat_id, settings.text_starter, parse_mode='html', disable_web_page_preview=True)
            # bot.send_message(chat_id, users_msg.home()[1],
            #                  reply_markup=users_msg.home()[0])

        else:
            bot.send_message(chat_id,
                         'В Боте ведуться технические работы \U000026A0 \n\n <i>Приносим свои извинения за предоставленные неудобства, скоро будет только лучше!</i> ',
                         parse_mode='html', disable_web_page_preview=True)
            # bot.send_message(chat_id, main_menu.menu()[1],
            #                  reply_markup=main_menu.menu()[0])

#
# def ask_username(message):
#     username = message.text
#     val = validation.validFIO(username)  # проверка валидационная
#     if val == 'Всё отлично!':
#         username = message.text
#         user = User(message.chat.id)
#         user.update_username(username)
#         user.update_reg()
#
#         bot.send_message(message.chat.id, 'Рад с тобой познакомиться, <b>{}</b> \U0001F44B'.format(username),
#                          parse_mode='html')
#         bot.send_message(message.chat.id, main_menu.menu()[1],
#                          reply_markup=main_menu.menu()[0])
#         bot.clear_step_handler_by_chat_id(chat_id=message.chat.id)
#
#     else:  # если не прошла валидацию, то ещё раз можно ввести
#         msg = val
#         msg2 = bot.send_message(message.chat.id, msg, parse_mode='html')
#         bot.clear_step_handler_by_chat_id(chat_id=message.chat.id)
#         bot.register_next_step_handler(msg2, ask_username)
#
#
# def ask_change_username(message):
#     username = message.text
#     val = validation.validFIO(username)  # проверка валидационная
#     if val == 'Всё отлично!':
#         username = message.text
#         user = User(message.chat.id)
#         user.update_username(username)
#
#         bot.send_message(message.chat.id, 'Окей, <b>{}</b>, ты изменил(а) ФИО'.format(username), parse_mode='html')
#         msg = main_menu.lk(user.username(), user.faculty(), user.program())
#         bot.send_message(message.chat.id, msg[1],
#                          reply_markup=msg[0], parse_mode='html')
#         bot.clear_step_handler_by_chat_id(chat_id=message.chat.id)
#
#     else:  # если не прошла валидацию, то ещё раз можно ввести
#         msg = val
#         msg2 = bot.send_message(message.chat.id, msg, parse_mode='html')
#         bot.clear_step_handler_by_chat_id(chat_id=message.chat.id)
#         bot.register_next_step_handler(msg2, ask_change_username)
#
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback(call):
#     user = User(call.message.chat.id)
#
#     # ------------ БЛОК РЕГИСТРАЦИИ И АВТОРИЗАЦИИ ---------------------
#     # кнопка зарегистрироваться
#     if call.data == 'go_login':  # лежит в  users/user_msgr
#         user = User(call.message.chat.id)
#         bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
#         bot.send_message(chat_id=call.message.chat.id,
#                          text='Отлично, давай сначала познакомимся и ты немного расскажешь о себе \U0001F609',
#                          parse_mode='html')
#         msg = users_msg.reg_faculty(1, settings.all_faculties()[0], settings.all_faculties()[1])
#         bot.send_message(chat_id=call.message.chat.id, text=msg[1], parse_mode='html', reply_markup=msg[0])
#
#         # кнопка контакты
#     if call.data == 'contacts':
#         user = User(call.message.chat.id)
#         bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                               text=settings.text_help,
#                               reply_markup=users_msg.home_back(), parse_mode='html',  disable_web_page_preview=True)
#     # кнопка "О нас"
#     if call.data == 'info_no_reg':
#         user = User(call.message.chat.id)
#         bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                               text=settings.text_info,
#                               reply_markup=users_msg.home_back(), parse_mode='html', disable_web_page_preview=True)
#
#     # кнопка назад в меню с регитсрацией
#     if call.data == 'back_home':
#         user = User(call.message.chat.id)
#         msg = users_msg.home()[1]
#         bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=msg,
#                               reply_markup=users_msg.home()[0], parse_mode='html')
#
#     for i in list(range(10)):
#         if call.data == 'next_page_faculty_{}'.format(i):  # переход на следующую страницу
#             msg = users_msg.reg_faculty(i + 1, settings.all_faculties()[0], settings.all_faculties()[1])
#             bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                                           reply_markup=msg[0])
#
#         if call.data == 'back_page_faculty_{}'.format(i):  # переход на предидущую страницу
#             msg = users_msg.reg_faculty(i - 1, settings.all_faculties()[0], settings.all_faculties()[1])
#             bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                                           reply_markup=msg[0])
#
#     for i in settings.all_faculties()[1]:
#
#         if call.data == 'reg_{}'.format(i):
#             user = User(call.message.chat.id)
#             user.update_faculty_id(i)
#             msg = users_msg.reg_program(user.faculty_id())
#             bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                                   text=msg[1],
#                                   reply_markup=msg[0], parse_mode='html')
#
#     for i in settings.all_program(user.faculty_id())[1]:
#
#         if call.data == 'reg_program_{}'.format(i):
#             user = User(call.message.chat.id)
#             user.update_program_id(i)
#             bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                                   text=users_msg.status()[1],
#                                   reply_markup=users_msg.status()[0], parse_mode='html')
#
#     if call.data == 'entrant':
#         user = User(call.message.chat.id)
#         user.update_entrant()
#         msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                                     text='Отлично, напиши мне свои ФИО: ')
#         bot.register_next_step_handler(msg, ask_username)
#
#     if call.data == 'not_entrant':
#         user = User(call.message.chat.id)
#         user.update_not_entrant()
#         msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                                     text='Ну может, я смогу тебе что-нибудь подсказать, напиши мне свои ФИО: ')
#         bot.register_next_step_handler(msg, ask_username)
#
#     if call.data == 'student':
#         user = User(call.message.chat.id)
#         user.update_student()
#         msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                                     text='Отлично, укажи своё ФИО и пользуйся: ')
#         bot.register_next_step_handler(msg, ask_username)
#
#         # ------------ БЛОКИ ПОСЛЕ РЕГИСТРАЦИИ И АВТОРИЗАЦИИ ------------------
#     # ----------------------------------------------------
#     if call.data == 'back_to_menu':
#         bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                               text=main_menu.menu()[1],
#                               reply_markup=main_menu.menu()[0])
#
#     # ----------------------------------ЛИЧНЫЙ КАБИНЕТ------------------
#     if call.data == 'lk':
#         user = User(call.message.chat.id)
#         msg = main_menu.lk(user.username(), user.faculty(), user.program())
#         bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                               text=msg[1],
#                               reply_markup=msg[0], parse_mode='html')
#
#     if call.data == 'change_username':
#         msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                                     text='Отлично, напиши мне изменённые ФИО: ')
#         bot.register_next_step_handler(msg, ask_change_username)
#
#     if call.data == 'change_faculty':
#         msg = lk.change_faculty(1, settings.all_faculties()[0], settings.all_faculties()[1])
#         bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                               text=msg[1], parse_mode='html', reply_markup=msg[0])
#
#     if call.data == 'change_program':
#         user = User(call.message.chat.id)
#         msg = lk.change_program(user.faculty_id())
#         bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                               text=msg[1], parse_mode='html', reply_markup=msg[0])
#
#     for i in list(range(10)):
#         if call.data == 'next_page_faculty_{}_change'.format(i):  # переход на следующую страницу
#             msg = lk.change_faculty(i + 1, settings.all_faculties()[0], settings.all_faculties()[1])
#             bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                                           reply_markup=msg[0])
#
#         if call.data == 'back_page_faculty_{}_change'.format(i):  # переход на предидущую страницу
#             msg = lk.change_faculty(i - 1, settings.all_faculties()[0], settings.all_faculties()[1])
#             bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                                           reply_markup=msg[0])
#
#     for i in settings.all_faculties()[1]:
#
#         if call.data == 'change_{}'.format(i):
#             user = User(call.message.chat.id)
#             last_faculty = user.faculty_id()
#             user.update_faculty_id(i)
#             if not settings.all_program(user.faculty_id()) == 'не найдено':
#                 msg = lk.change_program(user.faculty_id())
#                 bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                                       text=msg[1], parse_mode='html', reply_markup=msg[0])
#             else:
#                 msg = lk.change_program(user.faculty_id())
#                 bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                                       text=msg[1], parse_mode='html', reply_markup=msg[0])
#                 user.update_faculty_id(last_faculty)
#
#     for i in settings.all_program(user.faculty_id())[1]:
#         if call.data == 'change_program_{}'.format(i):
#             user = User(call.message.chat.id)
#             user.update_program_id(i)
#             msg = main_menu.lk(user.username(), user.faculty(), user.program())
#             bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                                   text=msg[1],
#                                   reply_markup=msg[0], parse_mode='html')
#
#     if call.data == 'entrance':
#         bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                               text=main_menu.entrance()[1],
#                               reply_markup=main_menu.entrance()[0], parse_mode='html')
#
#     try:
#         if call.data == 'location':
#             user = User(call.message.chat.id)
#             bot.delete_message(call.message.chat.id, call.message.message_id)
#             geo = location.geo_data(user.faculty_id())
#             bot.send_location(call.message.chat.id, geo[0], geo[1])
#             bot.send_message(call.message.chat.id, main_menu.back_to_menu()[1],
#                              reply_markup=main_menu.back_to_menu()[0])
#     except Exception:
#         if call.data == 'location':
#             msg = 'Не могу найти данные по местонахождению факультета!'
#             bot.send_message(chat_id=call.message.chat.id,
#                              text=msg, reply_markup=main_menu.back_to_menu()[0])
#
#     if call.data == 'selection_сommittee':
#         bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                               text=main_menu.selection_committee()[1],
#                               reply_markup=main_menu.selection_committee()[0], parse_mode='html')
#
#     # ----------------------------------selection committee------------------
#     if call.data == 'back_to_sc':
#         bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                               text=main_menu.selection_committee()[1],
#                               reply_markup=main_menu.selection_committee()[0], parse_mode='html')
#
#     if call.data == 'documents':
#         bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                               text=sc.documents()[1],
#                               reply_markup=sc.documents()[0], parse_mode='html')
#
#     if call.data == 'contacts_sc':
#         user = User(call.message.chat.id)
#         msg = sc.contact(user.faculty_id())
#         bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                               text=msg[1],
#                               reply_markup=msg[0], parse_mode='html')
#
#         # ----------------------------------ENTRANCE------------------
#     if call.data == 'tenure':
#         user = User(call.message.chat.id)
#         msg = entrance.tenure(user.program_id())
#         bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                               text=msg[1],
#                               reply_markup=msg[0], parse_mode='html')
#
#     try:
#         if call.data == 'subjects_ege':
#             user = User(call.message.chat.id)
#             msg = ege.subjects(user.program_id())
#             bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                                   text=msg[1],
#                                   reply_markup=msg[0], parse_mode='html')
#     except Exception:
#         if call.data == 'subjects_ege':
#             msg = 'Не могу найти данные по ЕГЭ!'
#             bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                                   text=msg,
#                                   reply_markup=main_menu.back_to_menu()[0], parse_mode='html')
#
#     try:
#         if call.data == 'subjects_dvi':
#             user = User(call.message.chat.id)
#             msg = dvi.subjects(user.program_id())
#             bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                                   text=msg[1],
#                                   reply_markup=msg[0], parse_mode='html')
#
#     except Exception:
#         if call.data == 'subjects_dvi':
#             msg = 'Не могу найти данные по ДВИ!'
#             bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                                   text=msg,
#                                   reply_markup=main_menu.back_to_menu()[0], parse_mode='html')
#
#     try:
#         if call.data == 'last_year_dvi':
#             user = User(call.message.chat.id)
#             msg = entrance.last_year_dvi(user.faculty_id())
#             bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                                   text=msg[1],
#                                   reply_markup=msg[0], parse_mode='html')
#     except Exception:
#         if call.data == 'last_year_dvi':
#             msg = 'Не могу найти данные по ДВИ!'
#             bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                                   text=msg,
#                                   reply_markup=main_menu.back_to_menu()[0], parse_mode='html')
#
#     if call.data == 'dvi_subject':
#         user = User(call.message.chat.id)
#         msg = entrance.dvi_subject(user.program_id())
#         bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                               text=msg[1],
#                               reply_markup=msg[0], parse_mode='html')
#
#     # ----------------   МЕСТА    ---------------
#     if call.data == 'budget':
#         user = User(call.message.chat.id)
#         msg = entrance.budget(user.program_id())
#         bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                               text=msg[1],
#                               reply_markup=msg[0], parse_mode='html')
#
#     if call.data == 'paid':
#         user = User(call.message.chat.id)
#         msg = entrance.paid(user.program_id())
#         bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                               text=msg[1],
#                               reply_markup=msg[0], parse_mode='html')
#
#     # ----------------   БЮДЖЕТ    ------------------
#     if call.data == 'passing_score':
#         user = User(call.message.chat.id)
#         msg = entrance.passing_score(user.program_id())
#         bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                               text=msg[1],
#                               reply_markup=msg[0], parse_mode='html')
#
#     if call.data == 'people-seat':
#         user = User(call.message.chat.id)
#         msg = entrance.people_seat(user.program_id())
#         bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                               text=msg[1],
#                               reply_markup=msg[0], parse_mode='html')
#
#     # ----------------   ПЛАТКА    ------------------
#     if call.data == 'minimal_score':
#         user = User(call.message.chat.id)
#         msg = entrance.min_score(user.program_id())
#         bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                               text=msg[1],
#                               reply_markup=msg[0], parse_mode='html')
#
#     if call.data == 'price':
#         user = User(call.message.chat.id)
#         msg = entrance.price(user.program_id())
#         bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                               text=msg[1],
#                               reply_markup=msg[0], parse_mode='html')
#
#     # ----------------------------------ССЫЛКИ------------------
#     if call.data == 'links':
#         bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                               text=main_menu.links()[1],
#                               reply_markup=main_menu.links()[0], parse_mode='html')



bot.polling(none_stop=True, interval=1, timeout=10)
