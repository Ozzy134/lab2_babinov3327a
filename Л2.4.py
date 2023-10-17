def temp_cat(temp):
    if temp <= -20: #Указываем программе, функцию больше или равно
        return '1, Холодно'
    elif temp <= 0: #Для каждого показателя указываем допустимую температуру
        return '2, Прохладно'
    elif temp <= 15:
        return '3, Зябко'
    elif temp <= 25:
        return '4, Тепло'
    else: #Если не один из пунктов не прошел, то выдаем "Жарко"
        return '5, Жарко'

temp = int(input())
print (temp_cat(temp))

