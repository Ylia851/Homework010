import inputt

n = inputt.New_Dist(inputt.dist1, inputt.User_Data)

def Seach_Name():
    print('Введите данные для поиска (ФИО)')
    element = update.message()
    for i in n:
        if n[i]['FIO'] == element:
            print(n[i])
        else:
            print('Элемент не найден')