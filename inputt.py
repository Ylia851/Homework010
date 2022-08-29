import outputt
import sqlite3
from telegram import Update
from telegram.ext import ContextTypes

def User_Data():
    print("Введите ФИО сотрудника: ")
    FIO = update.message()
    print("Введите дату рождения: ")
    age = update.message()
    print("Введите страховой номер: ")
    str_number = update.message()
    print("Введите контактный телефон: ")
    phone = update.message()
    print("Выберите должность: ")
    post = outputt.Print_Data(post)
    #post = open('post.json', 'r')?
    print('Выберите отдел: ')
    otdel = outputt.Print_Data(otdel)
    return [FIO, age, str_number, phone, post, otdel]

dist1 = {}

def Unput_post():
    print('Введите порядковый номер должности')
    id_post = int(update.message())
    print('Введите наименование должности: ')
    post = update.message()
    return [id_post, post]

def Unput_otd():
    print('Введите порядковый номер отдела')
    id_otd = int(update.message())
    print('Введите наименование отдела: ')
    otdel = update.message()
    return [id_otd, otdel]

def New_Dist(dist1, data):
    if len(dist1) == 0: id == 1
    else: id = max(dist1.keys())+1
    dist1[id] = data

FIO = updater.dispatcher.add_handler(CommandHandler('FIO', New_Dist(dist1, User_Data)))
#FIO = New_Dist(dist1, User_Data)
Otdel = updater.dispatcher.add_handler(CommandHandler('otdel'. New_Dist(dist1, Unput_otd)))
#Otdel = New_Dist(dist1, Unput_otd)
Post = updater.dispatcher.add_handler(CommandHandler('Post', New_Dist(dist1, Unput_post)))
#Post = New_Dist(dist1, Unput_post)

def Control():
    con = sqlite3.connect("test.db")
    cur = con.cursor
    with con:
        cur.execute("""
        CREATE TABLE user_post (
            id INT,
            post_id INT,
            otdel_id INT)
            PRIMARY KEY(id, post_id, otdel_id,
            FOREIGN KEY(id) REFERENCES user(id),
            FOREIGN KEY(post_id, otdel_id) REFERENCES post(id) REFERENCES otdel(id)
               );
    """)