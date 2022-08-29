import json 

import inputt

n = inputt.New_Dist(inputt.dist1, inputt.User_Data)
def Safe_FIO(n):
    with open ('FIO.json', "w", encoding = 'utf-8') as file:
        file.write(json.dums(n, ensure_ascii = False))

def Safe_otdel(n):
    with open ('Otdel.json', "w", encoding = 'utf-8') as file:
        file.write(json.dums(n, ensure_ascii = False))

def Safe_post(n):
    with open ('Post.json', "w", encoding = 'utf-8') as file:
        file.write(json.dums(n, ensure_ascii = False))