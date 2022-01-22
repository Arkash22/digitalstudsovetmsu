import psycopg2
import os, sys

conn = psycopg2.connect(dbname='msu_dvi_bot', user='mrkrap',
                        password='5170', host='89.108.64.97')
cursor = conn.cursor()  # обращаться будем через курсор

BotToken = '1700612569:AAGdmn_bIN0lxRY5AOB_ns3EV4MCJGeHpc8' # @test_drafer_bot
# pic_folder = 'C:/Users/Mark/OneDrive - msu.ru/Рабочий стол/drafter_bot/photo/'