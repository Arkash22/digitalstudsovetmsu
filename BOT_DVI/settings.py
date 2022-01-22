import psycopg2
import os, sys

conn = psycopg2.connect(dbname='---', user='user',
                        password='-', host='--.---.--.--')
cursor = conn.cursor()  # обращаться будем через курсор

BotToken = '' # @msu_dvi_bot
