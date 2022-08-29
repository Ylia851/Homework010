from telegram import Update
from telegram.ext import ContextTypes

import sys
from interface import Interface
import inputt 
import seach
import delll
import change
import outputt
import exp
import inporttt
import safe

def Controler(update: Update, context: ContextTypes):
    regim = int(update.message(Interface()))
    if regim == 1:
        update.message.reply_text('Вы открыли меню для ввода нового сотрудника')
        res = inputt.User_Data()
        return Interface()
    elif regim == 2:
        update.message.reply_text('Вы открыли меню поиска сотрудников')
        res = seach.Seach_Name()
        return Interface()
    elif regim == 3:
        update.message.reply_text('Вы открыли меню удаления сотрудника из базы')
        res = delll.Del()
        return Interface()
    elif regim == 4:
        update.message.reply_text('Меню для поиска и изменения данных сотрудника запущено')
        res = change.Seach_Name()
        return Interface()
    elif regim == 5:
        update.message.reply_text('Режим вывода базы данных на экран запущен')
        res = outputt.Print_Data() 
        return Interface()
    elif regim == 6:
        update.message.reply_text('Вы запустили режим экспорта базы')
        res = exp.export_data() 
        return Interface()
    elif regim == 7:
        update.message.reply_text('Вы запустили режим импорта базы')
        update.message.reply_text('Выберите файл для импорта: 11. Сотрудники; 12. Отдел; 13. Должность')
        im = int(input())
        if im == 11: res = inporttt.Load_FIO()
        elif im == 12: res = inporttt.Load_Otdel()
        elif im == 13: res = inporttt.Load_Post()
        else: update.message.reply_text('Введите корректные данные')
        return Interface()
    elif regim == 8:
        update.message.reply_text('Вы запустили режим сохранения данных')
        update.message.reply_text('Выберите файл для сохранения: 21. Сотрудники; 22. Отдел; 23. Должность')
        im = int(input())
        if im == 21: res = safe.Safe_FIO()
        elif im == 22: res = safe.Safe_otdel
        elif im == 23: res = safe.Safe_post()
        else: update.message.reply_text('Введите корректные данные')
        return Interface()
    elif regim == 9:
        update.message.reply_text('Режим выхода из программы запущен')
        res = sys.exit()
    else:
        update.message.reply_text('Выберите корректный режим работы')
    return 