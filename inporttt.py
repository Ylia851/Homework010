import json

def Load_FIO():
    with open('FIO.json', 'r', encoding = 'utf-8') as ft1:
        return json.Load(ft1)

def Load_Post():
    with open('Post.json', 'r', encoding = 'utf-8') as ft2:
        return json.Load(ft2)

def Load_Otdel():
    with open('Otdel.json', 'r', encoding = 'utf-8') as ft3:
        return json.Load(ft3)