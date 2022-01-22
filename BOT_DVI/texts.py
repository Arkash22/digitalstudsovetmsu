import settings
from telebot import types
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from users.models import DVI, Potok


#         ---------------При нажатии команды /start --------------------------
def text_start_first(name):
    text_start = f'Привет, {name}!\n\nЯ - новый бот <a href="https://vk.com/studsovetmsu">Студсовета МГУ</a>, который ' \
                 f'будет подсказывать Вам с расписанием и материалами для подготовки к ДВИ в МГУ.'
    return text_start


def text_start(name):
    text_start = f'Рад Вас снова видеть, {name}'
    return text_start


#         ---------------При возвращении в главное меню --------------------------
def back_to_main_menu(name):
    text = f'Возвращаю Вас, {name}, в главное меню:'
    return text


#         ---------------О нас --------------------------

text_info = '\U00002139<b> Немного о боте!</b>' \
            '\n\n Этот бот был разработан и запущен командой <a href="https://vk.link/digitalstudsovetmsu">комитета' \
            'по цифровому развитию Студенческого совета МГУ</a> с целью помочь вам, абитуриентам, с поступлением в ' \
            'нашу Alma Mater. Разработчики этого приложения так же, как и вы, совсем недавно поступали в вуз и ' \
            'боялись не сдать ДВИ. В МГУ имени М. В. Ломоносова действительно попасть не так просто. Мы верим, ' \
            'что все ваши усилия, направленне на поступление в Университет, не пройдут зря, и вы очень скоро увидите ' \
            'свою фамилию в приказе о зачислении. \n\n' \
            '<i>P.s. Пользуйтесь ботом и оставляйте свои коментарии/замечания/благодарности в нашей группе в ' \
            'Вконтакте.</i> '

text_help = '<b>Контакты поддержки:</b>\n\n' \
            '\U0001F310 Наш сайт - <a href="https://vk.link/digitalstudsovetmsu">сайт сообщества в ВК</a> \n' \
            '\U0000260E Телефон: +7(964)723-56-82\n' \
            '\U0001F4E7 Email: digital@studsovet.msu.ru\n' \
            '\U0001F468\U0000200D\U0001F4BB По техническим вопросам - @AVFroym'

#         ---------------Узнать дату --------------------------

date = 'Выберете предмет ДВИ:'

date_potok = 'Выберете поток:'


def dvi_dates(id):
    global text
    dvi = DVI(id)
    result_id = dvi.potok_ids()
    result_name = dvi.potok_names()
    dates = []

    for i in result_id:
        potok = Potok(i)
        dates.append(potok.data())

    result = ''

    for i in list(range(0, len(result_id))):
        result = result + '{} - {} \n'.format(result_name[i], dates[i])

        text = '<b>Выберите интересующий Вас поток :</b>\n\n' + result

    return text


def data_potok(id_potok):
    potok = Potok(id_potok)
    data = potok.data()

    text = f'Вы будете сдавать - {data} .'

    return text


#         ---------------Подготовка --------------------------

preparation = 'К какому предмету вы хотите подготовиться?'

preparation_links = 'Варианты прошлого года:'

#         ---------------Cписки --------------------------

spiski = '<i>Распределение поступающих по дням и потокам для сдачи дополнительного вступительного испытания (ДВИ) ' \
         'осуществляется Центральной приёмной комиссией МГУ с учётом даты приема документов и часовых поясов ' \
         'поступающих.</i> \n\n' \
         '<b> С 12 июля начнёт формироваться распределение по потокам.</b> \n\n' \
         'Вся актуальная информация постоянно обновляется на сайте: http://cpk.msu.ru/2021/exams'
