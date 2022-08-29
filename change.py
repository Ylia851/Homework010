import inputt
import outputt

n = inputt.New_Dist(inputt.dist1, inputt.User_Data)

def Seach_Name():
    print('Введите данные для поиска (ФИО)')
    element = update.message()
    for i in n:
        if n[i]['FIO'] == element:
            print('Выберите, что вы хотите изменить: 31. ФИО; 32. Дату рождения; 33. Страховой номер; 34. Контактный телефон; 35. Должность; 36. Отдел')
            izm = int(update.message())
            if izm == 31:
                n['FIO'] = update.message('Введите новые данные')
            if izm == 32:
                n['age'] = update.message('Введите новые данные')
            if izm == 33:
                n['str_number'] = update.message('Введите новые данные')
            if izm == 34:
                n['phone'] = update.message('Введите новые данные')
            if izm == 35:
                n['post'] = outputt.Print_Data(post)
            if izm == 36:
                n['otdel'] = outputt.Print_Data(otdel)