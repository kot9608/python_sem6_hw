# Задача 30:  
# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.

# Каждое число вводится с новой строки.

# Input:
# А1 = 1
# D = 2
# N = 5
# Output:
# 1, 3, 5, 7, 9


a=int(input('Введите первый элемент прогрессии: '))
d=int(input('Введите разность между элементами прогрессии: '))
size=int(input('Введите первый количество элементов прогрессии: '))
lst=[]
i=1#счетчик
while i<=size:
    temp=a+(i-1)*d
    lst.append(temp)
    i+=1
print(lst)