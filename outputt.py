import inputt

n = inputt.New_Dist(inputt.dist1, inputt.User_Data)

def Print_Data():
    print('Режим вывода базы сотрудников запущен')
    for i in n:
        print(n[i])