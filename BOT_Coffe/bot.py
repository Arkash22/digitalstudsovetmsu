import telebot
import re
from telebot import types
import settings
import validation
import home

from users import valid_reg
from users import users_msg
from users import anketa
from users.models import User
from users.models import Meeting

# from settings import conn, cursor


bot = telebot.TeleBot(settings.BotToken)  # бот API


@bot.message_handler(commands=['start'])
def starter(message):
    chat_id = message.chat.id
    name = message.chat.username
    first_name = message.chat.first_name
    if first_name is None:
        first_name = 'Пользователь'
    print(chat_id)

    # bot.send_message(chat_id,
    #                  'В Боте ведуться технические работы \U000026A0 \n\n <i>Приносим свои извинения за предоставленные неудобства, скоро будет только лучше!</i> ',
    #                  parse_mode='html', disable_web_page_preview=True)

    if valid_reg.is_reg(chat_id) == 404:  # эта функция проверяет есть ли этот chatid в бд
        if name is None:
            msg = users_msg.first_for_no_user(first_name)

            bot.send_message(chat_id, msg[1], parse_mode='html',
                             disable_web_page_preview=True)
            bot.send_message(chat_id, msg[2], parse_mode='html',
                             disable_web_page_preview=True, reply_markup=msg[0])

        else:
            user = User(chat_id)
            user.create_user(name)
            msg = users_msg.first(first_name)

            bot.send_message(chat_id, msg[1], parse_mode='html',
                             disable_web_page_preview=True)
            bot.send_message(chat_id, msg[2], parse_mode='html',
                             disable_web_page_preview=True)
            bot.send_message(chat_id, msg[3],
                             reply_markup=msg[0], parse_mode='html')

    elif valid_reg.is_reg(chat_id) == 0:  # эта функция проверяет закончил ли этот chatid регистрацию
        if name is None:
            msg = users_msg.first_for_no_user(first_name)
            bot.send_message(chat_id, msg[2], parse_mode='html',
                             disable_web_page_preview=True, reply_markup=msg[0])
        else:
            user = User(chat_id)
            user.update_tg_username(name)
            msg = users_msg.not_full_reg(first_name)
            bot.send_message(chat_id, msg[1],
                             reply_markup=msg[0], parse_mode='html')


    else:
        if name is None:
            msg = users_msg.first_for_no_user(first_name)
            bot.send_message(chat_id, msg[2], parse_mode='html',
                             disable_web_page_preview=True, reply_markup=msg[0])
        else:
            user = User(chat_id)
            user.update_tg_username(name)
            bot.send_message(chat_id, f'Рад тебя видеть, {first_name}!', reply_markup=home.home(), parse_mode='html',
                             disable_web_page_preview=True)


def ask_change_username(message):
    user = User(message.chat.id)
    text = message.text
    print(text)
    val = validation.validFIO(text)  # проверка валидационная
    if val == 200:
        first_name = re.sub(";.*", "", message.text)
        bot.send_message(message.chat.id, f"Теперь твои новые ФИ - <b>{first_name}</b>",
                         reply_markup=types.ReplyKeyboardRemove(),
                         parse_mode='html')

        user.update_firstname(first_name)
        all_info = user.all_information()
        if valid_reg.is_reg(message.chat.id) == 1:
            msg = anketa.my_anketa(all_info[0], all_info[1], all_info[2], all_info[3], all_info[4], all_info[5])
        else:
            msg = anketa.anketa(all_info[0], all_info[1], all_info[2], all_info[3], all_info[4], all_info[5])
        bot.send_message(message.chat.id, msg[1],
                         reply_markup=msg[0], parse_mode='html', disable_web_page_preview=True)
        bot.clear_step_handler_by_chat_id(chat_id=message.chat.id)
    else:  # если не прошла валидацию, то ещё раз можно ввести
        msg = val
        msg2 = bot.send_message(message.chat.id, msg, parse_mode='html')
        bot.clear_step_handler_by_chat_id(chat_id=message.chat.id)
        bot.register_next_step_handler(msg2, ask_change_username)


def ask_change_gender(message):
    text = message.text
    print(text)
    val = validation.validGender(text)  # проверка валидационная
    if val == 200:
        gender = message.text
        g = gender.split()[0]
        bot.send_message(message.chat.id, f"Я обновил данные по твоему гендеру!\n\n<i><b>Пол:</b></i>  {gender}",
                         reply_markup=types.ReplyKeyboardRemove(),
                         parse_mode='html')
        user = User(message.chat.id)
        user.update_gender(g)
        all_info = user.all_information()
        if valid_reg.is_reg(message.chat.id) == 1:
            msg = anketa.my_anketa(all_info[0], all_info[1], all_info[2], all_info[3], all_info[4], all_info[5])
        else:
            msg = anketa.anketa(all_info[0], all_info[1], all_info[2], all_info[3], all_info[4], all_info[5])
        bot.send_message(message.chat.id, msg[1],
                         reply_markup=msg[0], parse_mode='html', disable_web_page_preview=True)
        bot.clear_step_handler_by_chat_id(chat_id=message.chat.id)
    elif val == 201:
        gender = re.sub(";.*", "", message.text)
        bot.send_message(message.chat.id, f"Воу, достаточно оригинально! Я обновил твои данные."
                                          f"\n\n<i><b>Пол:</b></i>  {gender}",
                         reply_markup=types.ReplyKeyboardRemove(),
                         parse_mode='html')
        user = User(message.chat.id)
        user.update_gender(gender)
        all_info = user.all_information()
        if valid_reg.is_reg(message.chat.id) == 1:
            msg = anketa.my_anketa(all_info[0], all_info[1], all_info[2], all_info[3], all_info[4], all_info[5])
        else:
            msg = anketa.anketa(all_info[0], all_info[1], all_info[2], all_info[3], all_info[4], all_info[5])
        bot.send_message(message.chat.id, msg[1],
                         reply_markup=msg[0], parse_mode='html', disable_web_page_preview=True)
        bot.clear_step_handler_by_chat_id(chat_id=message.chat.id)
    else:  # если не прошла валидацию, то ещё раз можно ввести
        msg = val
        msg2 = bot.send_message(message.chat.id, msg, parse_mode='html')
        bot.clear_step_handler_by_chat_id(chat_id=message.chat.id)
        bot.register_next_step_handler(msg2, ask_change_gender)


def ask_change_age(message):
    text = message.text
    print(text)
    if text == 'Не скажу \U0001F92B':
        bot.send_message(message.chat.id, "Хорошо, я не стал обновлять твои данные",
                         reply_markup=types.ReplyKeyboardRemove(),
                         parse_mode='html')
        user = User(message.chat.id)
        user.update_age(None)
        all_info = user.all_information()
        if valid_reg.is_reg(message.chat.id) == 1:
            msg = anketa.my_anketa(all_info[0], all_info[1], all_info[2], all_info[3], all_info[4], all_info[5])
        else:
            msg = anketa.anketa(all_info[0], all_info[1], all_info[2], all_info[3], all_info[4], all_info[5])
        bot.send_message(message.chat.id, msg[1],
                         reply_markup=msg[0], parse_mode='html', disable_web_page_preview=True)
        bot.clear_step_handler_by_chat_id(chat_id=message.chat.id)
    else:
        val = validation.validAge(text)  # проверка валидационная
        if val == 200:
            age = re.sub(";.*", "", message.text)
            bot.send_message(message.chat.id, f"Я обновил твой возраст - <b>{age} лет(год)</b>",
                             reply_markup=types.ReplyKeyboardRemove(),
                             parse_mode='html')
            user = User(message.chat.id)
            user.update_age(int(age))
            all_info = user.all_information()
            if valid_reg.is_reg(message.chat.id) == 1:
                msg = anketa.my_anketa(all_info[0], all_info[1], all_info[2], all_info[3], all_info[4], all_info[5])
            else:
                msg = anketa.anketa(all_info[0], all_info[1], all_info[2], all_info[3], all_info[4], all_info[5])
            bot.send_message(message.chat.id, msg[1],
                             reply_markup=msg[0], parse_mode='html', disable_web_page_preview=True)
            bot.clear_step_handler_by_chat_id(chat_id=message.chat.id)
        else:  # если не прошла валидацию, то ещё раз можно ввести
            msg = val
            msg2 = bot.send_message(message.chat.id, msg, parse_mode='html')
            bot.clear_step_handler_by_chat_id(chat_id=message.chat.id)
            bot.register_next_step_handler(msg2, ask_change_age)


def ask_change_inst(message):
    text = re.sub(";.*", "", message.text)
    print(text)
    if text == 'Нет instagram\'a \U0001F645\U0000200D\U00002642\U0000FE0F':
        bot.send_message(message.chat.id, "Хорошо, так и запишу в твоей анкете.",
                         reply_markup=types.ReplyKeyboardRemove(),
                         parse_mode='html')
        user = User(message.chat.id)
        user.update_instagram('Not_user')
        all_info = user.all_information()
        if valid_reg.is_reg(message.chat.id) == 1:
            msg = anketa.my_anketa(all_info[0], all_info[1], all_info[2], all_info[3], all_info[4], all_info[5])
        else:
            msg = anketa.anketa(all_info[0], all_info[1], all_info[2], all_info[3], all_info[4], all_info[5])
        bot.send_message(message.chat.id, msg[1],
                         reply_markup=msg[0], parse_mode='html', disable_web_page_preview=True)
        bot.clear_step_handler_by_chat_id(chat_id=message.chat.id)
    elif text == 'Не скажу \U0001F92B':
        bot.send_message(message.chat.id, "Хорошо, я не стал обновлять твои данные",
                         reply_markup=types.ReplyKeyboardRemove(),
                         parse_mode='html')
        user = User(message.chat.id)
        user.update_instagram('Null')
        all_info = user.all_information()
        if valid_reg.is_reg(message.chat.id) == 1:
            msg = anketa.my_anketa(all_info[0], all_info[1], all_info[2], all_info[3], all_info[4], all_info[5])
        else:
            msg = anketa.anketa(all_info[0], all_info[1], all_info[2], all_info[3], all_info[4], all_info[5])
        bot.send_message(message.chat.id, msg[1],
                         reply_markup=msg[0], parse_mode='html', disable_web_page_preview=True)
        bot.clear_step_handler_by_chat_id(chat_id=message.chat.id)
    else:
        val = validation.validInst(text)  # проверка валидационная
        if val == 200:
            inst = text
            bot.send_message(message.chat.id, f"Я обновил твой Instagram - <b>{inst}</b>",
                             reply_markup=types.ReplyKeyboardRemove(),
                             parse_mode='html')
            user = User(message.chat.id)
            user.update_instagram(inst)
            all_info = user.all_information()
            if valid_reg.is_reg(message.chat.id) == 1:
                msg = anketa.my_anketa(all_info[0], all_info[1], all_info[2], all_info[3], all_info[4], all_info[5])
            else:
                msg = anketa.anketa(all_info[0], all_info[1], all_info[2], all_info[3], all_info[4], all_info[5])
            bot.send_message(message.chat.id, msg[1],
                             reply_markup=msg[0], parse_mode='html', disable_web_page_preview=True)
            bot.clear_step_handler_by_chat_id(chat_id=message.chat.id)
        else:  # если не прошла валидацию, то ещё раз можно ввести
            msg = val
            msg2 = bot.send_message(message.chat.id, msg, parse_mode='html')
            bot.clear_step_handler_by_chat_id(chat_id=message.chat.id)
            bot.register_next_step_handler(msg2, ask_change_inst)


def ask_change_info(message):
    text = message.text
    print(text)
    val = validation.validInfo(text)  # проверка валидационная
    if val == 200:
        info = re.sub(";.*", "", message.text)
        bot.send_message(message.chat.id, f"Супер, я обновил твои данные, в графе о себе ты оставил(а):"
                                          f" \n\n <i>{info}</i>",
                         parse_mode='html')
        user = User(message.chat.id)
        user.update_info(info)
        all_info = user.all_information()
        if valid_reg.is_reg(message.chat.id) == 1:
            msg = anketa.my_anketa(all_info[0], all_info[1], all_info[2], all_info[3], all_info[4], all_info[5])
        else:
            msg = anketa.anketa(all_info[0], all_info[1], all_info[2], all_info[3], all_info[4], all_info[5])
        bot.send_message(message.chat.id, msg[1],
                         reply_markup=msg[0], parse_mode='html', disable_web_page_preview=True)
        bot.clear_step_handler_by_chat_id(chat_id=message.chat.id)
    else:  # если не прошла валидацию, то ещё раз можно ввести
        msg = val
        msg2 = bot.send_message(message.chat.id, msg, parse_mode='html')
        bot.clear_step_handler_by_chat_id(chat_id=message.chat.id)
        bot.register_next_step_handler(msg2, ask_change_info)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == 'refresh_start':
        chat_id = call.message.chat.id
        name = call.message.chat.username
        first_name = call.message.chat.first_name
        if first_name is None:
            first_name = 'Пользователь'
        print(chat_id)

        if valid_reg.is_reg(chat_id) == 404:  # эта функция проверяет есть ли этот chatid в бд
            if name is None:
                msg = users_msg.first_for_no_user(first_name)

                bot.send_message(chat_id, msg[1], parse_mode='html',
                                 disable_web_page_preview=True)
                bot.send_message(chat_id, msg[2], parse_mode='html',
                                 disable_web_page_preview=True, reply_markup=msg[0])

            else:
                user = User(chat_id)
                user.create_user(name)
                msg = users_msg.first(first_name)

                bot.send_message(chat_id, msg[1], parse_mode='html',
                                 disable_web_page_preview=True)
                bot.send_message(chat_id, msg[2], parse_mode='html',
                                 disable_web_page_preview=True)
                bot.send_message(chat_id, msg[3],
                                 reply_markup=msg[0], parse_mode='html')

        elif valid_reg.is_reg(chat_id) == 0:  # эта функция проверяет закончил ли этот chatid регистрацию
            if name is None:
                msg = users_msg.first_for_no_user(first_name)
                bot.send_message(chat_id, msg[2], parse_mode='html',
                                 disable_web_page_preview=True, reply_markup=msg[0])
            else:
                user = User(chat_id)
                user.update_tg_username(name)
                msg = users_msg.not_full_reg(first_name)
                bot.send_message(chat_id, msg[1],
                                 reply_markup=msg[0], parse_mode='html')


        else:
            if name is None:
                msg = users_msg.first_for_no_user(first_name)
                bot.send_message(chat_id, msg[2], parse_mode='html',
                                 disable_web_page_preview=True, reply_markup=msg[0])
            else:
                user = User(chat_id)
                user.update_tg_username(name)
                bot.send_message(chat_id, f'Рад тебя видеть, {first_name}!', reply_markup=home.home(),
                                 parse_mode='html',
                                 disable_web_page_preview=True)

    if call.data == 'go_login':  # лежит в  users/user_msgr
        user = User(call.message.chat.id)
        all_info = user.all_information()
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(chat_id=call.message.chat.id,
                         text='Окей, сейчас я о тебе ничего не знаю, давай это исправим \U0001F60E',
                         parse_mode='html')
        msg = anketa.anketa(all_info[0], all_info[1], all_info[2], all_info[3], all_info[4], all_info[5])
        bot.send_message(chat_id=call.message.chat.id, text=msg[1], parse_mode='html', reply_markup=msg[0],
                         disable_web_page_preview=True)

    if call.data == 'go_login_not_all':  # лежит в  users/user_msgr
        user = User(call.message.chat.id)
        all_info = user.all_information()
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        msg = anketa.anketa(all_info[0], all_info[1], all_info[2], all_info[3], all_info[4], all_info[5])
        bot.send_message(chat_id=call.message.chat.id, text=msg[1], parse_mode='html', reply_markup=msg[0],
                         disable_web_page_preview=True)

    if call.data == 'go_coffee_demo':
        msg = anketa.demo_anketa_1()
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(chat_id=call.message.chat.id, text=msg[1], parse_mode='html', reply_markup=msg[0],
                         disable_web_page_preview=True)
    if call.data == '1_page':
        msg = anketa.demo_anketa_1()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=msg[1],
                              reply_markup=msg[0], parse_mode='html', disable_web_page_preview=True)
    if call.data == '2_page':
        msg = anketa.demo_anketa_2()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=msg[1],
                              reply_markup=msg[0], parse_mode='html', disable_web_page_preview=True)
    if call.data == '3_page':
        msg = anketa.demo_anketa_3()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=msg[1],
                              reply_markup=msg[0], parse_mode='html', disable_web_page_preview=True)
        # кнопка контакты
    if call.data == 'contacts':
        if valid_reg.is_reg(call.message.chat.id) == 1:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=settings.text_help,
                                  reply_markup=home.home_back(), parse_mode='html', disable_web_page_preview=True)
    # кнопка "О нас"
    if call.data == 'info_bot':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=settings.text_info,
                              reply_markup=home.home_back(), parse_mode='html', disable_web_page_preview=True)

    if call.data == 'back_home':
        keyboard = home.home()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=f'Вернул тебя в главное меню. {call.message.chat.first_name}, развлекайся)',
                              reply_markup=keyboard, parse_mode='html')

    if call.data == 'back_home_no_edit':
        keyboard = home.home()
        bot.send_message(chat_id=call.message.chat.id,
                         text=f'Вернул тебя в главное меню. {call.message.chat.first_name}, развлекайся)',
                         reply_markup=keyboard, parse_mode='html')
    # ------------------------АНКЕТА-------------------------------------

    if call.data == 're_name':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_1 = types.KeyboardButton(text=str(call.message.chat.first_name))
        button_2 = types.KeyboardButton(text=str(call.message.chat.first_name) + ' ' + str(call.message.chat.last_name))
        keyboard.add(button_1)
        keyboard.add(button_2)
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        msg = bot.send_message(chat_id=call.message.chat.id, text='\U0001F4DD Отлично, напиши мне новые ФИ:',
                               reply_markup=keyboard, parse_mode='html')
        bot.register_next_step_handler(msg, ask_change_username)

    if call.data == 're_gender':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_1 = types.KeyboardButton(text='Мужской \U0001F57A')
        button_2 = types.KeyboardButton(text='Женский \U0001F483')
        button_3 = types.KeyboardButton(text='Деревянный \U0001F464')
        keyboard.add(button_1, button_2)
        keyboard.add(button_3)
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        msg = bot.send_message(chat_id=call.message.chat.id,
                               text='\U0001F4DD Напиши мне свой пол или выбери из существующих:\n\n'
                                    '<i>P.s. если ты не можешь определиться или не хочешь расскрывать его -  '
                                    'выбирай <b>"ДЕРЕВЯННЫЙ"</b></i>',
                               reply_markup=keyboard, parse_mode='html')
        bot.register_next_step_handler(msg, ask_change_gender)

    if call.data == 're_age':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_1 = types.KeyboardButton(text='Не скажу \U0001F92B')
        keyboard.add(button_1)
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        msg = bot.send_message(chat_id=call.message.chat.id,
                               text='\U0001F4DD Напиши мне свой возраст <b>ЦИФРОЙ</b>:\n\n'
                                    '<i>P.s. если ты не хочешь расскрывать свой возраст -  '
                                    'выбирай <b>"Не скажу \U0001F92B"</b></i>',
                               reply_markup=keyboard, parse_mode='html')
        bot.register_next_step_handler(msg, ask_change_age)

    if call.data == 're_status':
        keyboard = types.InlineKeyboardMarkup()
        key_1 = types.InlineKeyboardButton(text='\U0001F468\U0000200D\U0001F393 Студент', callback_data='re_status_1')
        key_2 = types.InlineKeyboardButton(text='\U0001F468\U0000200D\U0001F3EB Аспирант/преподаватель',
                                           callback_data='re_status_2')
        key_3 = types.InlineKeyboardButton(text='\U0001F47C Абитуриент/школьник', callback_data='re_status_3')
        keyboard.add(key_1)
        keyboard.add(key_2)
        keyboard.add(key_3)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='\U0001F5FF Как ты можешь охарактеризовать <b>свой статус</b> в МГУ?',
                              reply_markup=keyboard, parse_mode='html')
    if call.data == 're_status_1':
        user = User(call.message.chat.id)
        user.update_status(1)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=
        f"Я обновил твой статус - <b>\U0001F468\U0000200D\U0001F393 Студент</b> МГУ",
                              parse_mode='html')
        all_info = user.all_information()
        if valid_reg.is_reg(call.message.chat.id) == 1:
            msg = anketa.my_anketa(all_info[0], all_info[1], all_info[2], all_info[3], all_info[4], all_info[5])
        else:
            msg = anketa.anketa(all_info[0], all_info[1], all_info[2], all_info[3], all_info[4], all_info[5])
        bot.send_message(call.message.chat.id,
                         text=msg[1],
                         reply_markup=msg[0], parse_mode='html', disable_web_page_preview=True)
        bot.clear_step_handler_by_chat_id(chat_id=call.message.chat.id)

    if call.data == 're_status_2':
        user = User(call.message.chat.id)
        user.update_status(2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=
        f"Я обновил твой статус - <b>\U0001F468\U0000200D\U0001F3EB Аспирант/преподаватель</b> МГУ",
                              parse_mode='html')
        all_info = user.all_information()
        if valid_reg.is_reg(call.message.chat.id) == 1:
            msg = anketa.my_anketa(all_info[0], all_info[1], all_info[2], all_info[3], all_info[4], all_info[5])
        else:
            msg = anketa.anketa(all_info[0], all_info[1], all_info[2], all_info[3], all_info[4], all_info[5])

        bot.send_message(call.message.chat.id,
                         text=msg[1],
                         reply_markup=msg[0], parse_mode='html', disable_web_page_preview=True)
        bot.clear_step_handler_by_chat_id(chat_id=call.message.chat.id)

    if call.data == 're_status_3':
        user = User(call.message.chat.id)
        user.update_status(3)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=
        f"Я обновил твой статус - <b>\U0001F47C Абитуриент/школьник</b>",
                              parse_mode='html')
        all_info = user.all_information()
        if valid_reg.is_reg(call.message.chat.id) == 1:
            msg = anketa.my_anketa(all_info[0], all_info[1], all_info[2], all_info[3], all_info[4], all_info[5])
        else:
            msg = anketa.anketa(all_info[0], all_info[1], all_info[2], all_info[3], all_info[4], all_info[5])
        bot.send_message(call.message.chat.id,
                         text=msg[1],
                         reply_markup=msg[0], parse_mode='html', disable_web_page_preview=True)
        bot.clear_step_handler_by_chat_id(chat_id=call.message.chat.id)

    if call.data == 're_inst':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_1 = types.KeyboardButton(text='Не скажу \U0001F92B')
        button_2 = types.KeyboardButton(text='Нет instagram\'a \U0001F645\U0000200D\U00002642\U0000FE0F')
        keyboard.add(button_1)
        keyboard.add(button_2)
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        msg = bot.send_message(chat_id=call.message.chat.id,
                               text='\U0001F4F8 Напиши свой Instagram <b>в формате @ник</b>:\n\n'
                                    '<i>P.s. если ты не понял как нужно отправить ник, то приведу пример. '
                                    'Нужно написать "@studsovetmsu". И тогда бот его правильно поймёт.</i>',
                               reply_markup=keyboard, parse_mode='html')
        bot.register_next_step_handler(msg, ask_change_inst)

    if call.data == 're_info':
        msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text='\U0001F4DC Расскажи о себе. Тут можно написать всё что угодно. '
                                         'Можешь написать пару слов, а можешь пару предложений, постарайся расскрыться,'
                                         'но в тоже время не нужно рассказывать всю свою биографию по месяцам '
                                         '\U0001F605 \n\n'
                                         '<i>P.s. слишком много информации я не переварю, так что лучше воздержись от '
                                         'текста на 1к+ символов</i> '
                                    , parse_mode='html')
        bot.register_next_step_handler(msg, ask_change_info)

    if call.data == 'done_1':
        msg = anketa.done()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=msg[1], reply_markup=msg[0]
                              , parse_mode='html', disable_web_page_preview=True)

    if call.data == 'back_anketa':
        user = User(call.message.chat.id)
        all_info = user.all_information()
        msg = anketa.anketa(all_info[0], all_info[1], all_info[2], all_info[3], all_info[4], all_info[5])
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=msg[1], parse_mode='html', reply_markup=msg[0],
                              disable_web_page_preview=True)

    if call.data == 'done_2':
        user = User(call.message.chat.id)
        user.update_reg()

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Супер! Твоя анкета создана, и теперь ты можешь находить себе КофеФрендов по всему '
                                   'МГУ \U00002615 '
                              , parse_mode='html', disable_web_page_preview=True)
        bot.send_message(chat_id=call.message.chat.id,
                         text='<b>Давай я тебе всё быстренько объясню!</b>\n\n'
                              'Сейчас мой функционал максимально практичен и ничем не засорён. '
                              'Ты можешь щёлкнуть по кнопке "\U0001F50E Coffee Friend" и программа '
                              'максимально быстро подберёт тебе КофеФренда,'
                              ' с которым ты сможешь встретиться в удобное для вас время.\n\n'
                              '<i>На данный момент я не умею анализировать интересы КофеФрендов, '
                              'так что тебе может попасться гик или тиктокерша \U0001F602 , но обещаю в будущем '
                              'улучшить алгоритм подбора.</i>', reply_markup=home.home(),
                         parse_mode='html')

    #  -------Главное меню ---------
    if call.data == 'go_coffee':
        chat_id = call.message.chat.id
        name = call.message.chat.username
        first_name = call.message.chat.first_name

        if valid_reg.is_time_block(chat_id) == 404:
            user = User(chat_id)
            user.create_block_time()

        if name is None:
            msg = users_msg.first_for_no_user(first_name)
            bot.send_message(chat_id, msg[2], parse_mode='html',
                             disable_web_page_preview=True, reply_markup=msg[0])
        elif settings.block_time(chat_id) is False:
            msg = home.time_block_text()
            bot.send_message(chat_id, msg[1], parse_mode='html',
                             disable_web_page_preview=True, reply_markup=msg[0])
        else:
            # print(settings.go_coffee(call.message.chat.id))
            if settings.go_coffee(
                    call.message.chat.id) == 404:  # эта функция выдаёт 404 только если нет больше людей в поиске
                user = User(call.message.chat.id)
                user.update_in_search(True)  # обновляем пользовалелю пораментр, что он вступает в поиск

                msg = home.go_coffee()
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=msg[1],
                                      reply_markup=msg[0], parse_mode='html')

            else:  # если есть ещё люди в поиске
                partners = settings.go_coffee(call.message.chat.id)  # id партнёров, которые находится в поиске
                print(partners)

                # number_partners = list(range(0, partners, 1))

                def find_partner(list_id_partners, i):
                    try:
                        partner = list_id_partners[i]

                        user2 = User(partner)  # пользователь, которого подобрала в качестве партнёра программа
                        user = User(call.message.chat.id)  # пользоваетль, который ищет партнёра

                        info_1 = user.all_information()
                        info_2 = user2.all_information()

                        msg = home.msg_random_friend(info_1[0], info_1[1], info_1[2], info_1[3], info_1[4], info_1[5],
                                                     info_1[6])  # текст для партнёра про нас

                        msg2 = home.msg_random_friend(info_2[0], info_2[1], info_2[2], info_2[3], info_2[4], info_2[5],
                                                      info_2[6])  # текст для нас про партнёра

                        bot.send_message(chat_id=partner, text=msg[1], parse_mode='html', disable_web_page_preview=True)
                        bot.send_message(chat_id=partner, text=msg[2], parse_mode='html', disable_web_page_preview=True,
                                         reply_markup=msg[3])

                        bot.send_message(chat_id=call.message.chat.id, text=msg2[0], parse_mode='html',
                                         disable_web_page_preview=True)
                        bot.send_message(chat_id=call.message.chat.id, text=msg2[2], parse_mode='html',
                                         disable_web_page_preview=True, reply_markup=msg2[3])

                        user2.update_in_search(False)  # обновляем пользовалелю пораментр, что он выходит из поиска
                        user.update_in_search(False)

                        user.update_block_time()
                        user2.update_block_time()

                        Meeting.create_meeting(call.message.chat.id, info_1[6], partner, info_2[6])

                    except Exception:
                        if i < len(partners):
                            partner = list_id_partners[i]
                            user2 = User(partner)  # пользователь, которого подобрала в качестве партнёра программа
                            user2.update_in_search(False)  # обновляем пользовалелю пораментр, что он выходит из поиска

                            find_partner(partners, i + 1)
                        else:
                            user = User(call.message.chat.id)
                            user.update_in_search(True)  # обновляем пользовалелю пораментр, что он вступает в поиск
                            msg = home.go_coffee()
                            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                                  text=msg[1],
                                                  reply_markup=msg[0], parse_mode='html')

                find_partner(partners, 0)

    if call.data == 'my_anketa':
        user = User(call.message.chat.id)
        all_info = user.all_information()
        msg = anketa.my_anketa(all_info[0], all_info[1], all_info[2], all_info[3], all_info[4], all_info[5])
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=msg[1], parse_mode='html', reply_markup=msg[0],
                              disable_web_page_preview=True)

    for i in list(range(10000)):

        if call.data == '1_star_{}_chatid1'.format(i):  # вместо i подставляется id встречи
            m = Meeting(i)
            m.update_rating_2(1)

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='Окей, я записал твою оценку! Жестокий(ая) ты конечно, но видимо собеседник '
                                       'заслужил!', parse_mode='html', reply_markup=home.home_back(),
                                  disable_web_page_preview=True)
        if call.data == '2_star_{}_chatid1'.format(i):  # вместо i подставляется id встречи
            m = Meeting(i)
            m.update_rating_2(2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='Окей, я записал твою оценку! Не парься, больше я не предложу тебе с ним(ней) '
                                       'встретиться!', parse_mode='html', reply_markup=home.home_back(),
                                  disable_web_page_preview=True)
        if call.data == '3_star_{}_chatid1'.format(i):  # вместо i подставляется id встречи
            m = Meeting(i)
            m.update_rating_2(3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='Окей, я записал твою оценку! Ну да, встреча ни о чём, но зато у тебя '
                                       'сохранился контакт и ты познакомился с новым человеком!', parse_mode='html',
                                  reply_markup=home.home_back(),
                                  disable_web_page_preview=True)
        if call.data == '4_star_{}_chatid1'.format(i):  # вместо i подставляется id встречи
            m = Meeting(i)
            m.update_rating_2(4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='Окей, я записал твою оценку! Рад, что у тебя была неплохая встреча)',
                                  parse_mode='html',
                                  reply_markup=home.home_back(),
                                  disable_web_page_preview=True)
        if call.data == '5_star_{}_chatid1'.format(i):  # вместо i подставляется id встречи
            m = Meeting(i)
            m.update_rating_2(5)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='Окей, я записал твою оценку! Рад, что тебе понравился собеседник, не забывай, '
                                       'что у тебя сохранились контакты и ты можешь пригласиить её/его ещё попить '
                                       'кофе!',
                                  parse_mode='html',
                                  reply_markup=home.home_back(),
                                  disable_web_page_preview=True)

        if call.data == '1_star_{}_chatid2'.format(i):  # вместо i подставляется id встречи
            m = Meeting(i)
            m.update_rating_1(1)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='Окей, я записал твою оценку! Жестокий(ая) ты конечно, но видимо собеседник '
                                       'заслужил!', parse_mode='html', reply_markup=home.home_back(),
                                  disable_web_page_preview=True)
        if call.data == '2_star_{}_chatid2'.format(i):  # вместо i подставляется id встречи
            m = Meeting(i)
            m.update_rating_1(2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='Окей, я записал твою оценку! Не парься, больше я не предложу тебе с ним(ней) '
                                       'встретиться!', parse_mode='html', reply_markup=home.home_back(),
                                  disable_web_page_preview=True)
        if call.data == '3_star_{}_chatid2'.format(i):  # вместо i подставляется id встречи
            m = Meeting(i)
            m.update_rating_1(3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='Окей, я записал твою оценку! Ну да, встреча ни о чём, но зато у тебя '
                                       'сохранился контакт и ты познакомился с новым человеком!', parse_mode='html',
                                  reply_markup=home.home_back(),
                                  disable_web_page_preview=True)
        if call.data == '4_star_{}_chatid2'.format(i):  # вместо i подставляется id встречи
            m = Meeting(i)
            m.update_rating_1(4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='Окей, я записал твою оценку! Рад, что у тебя была неплохая встреча)',
                                  parse_mode='html',
                                  reply_markup=home.home_back(),
                                  disable_web_page_preview=True)
        if call.data == '5_star_{}_chatid2'.format(i):  # вместо i подставляется id встречи
            m = Meeting(i)
            m.update_rating_1(5)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='Окей, я записал твою оценку! Рад, что тебе понравился собеседник, не забывай, '
                                       'что у тебя сохранились контакты и ты можешь пригласиить её/его ещё попить '
                                       'кофе!',
                                  parse_mode='html',
                                  reply_markup=home.home_back(),
                                  disable_web_page_preview=True)


bot.polling(none_stop=True, interval=1, timeout=10)
