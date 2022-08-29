import inputt

n = inputt.New_Dist(inputt.dist1, inputt.User_Data)

def Del():
    print('Введите ФИО сотрудника, которого вы хотите удалить')
    element = update.message()
    for i in n:
        if n[i]['FIO'] == element:
            n.pop(i)
        else:
            update.message.reply_text('Элемент не найден')
    return n