# 45. Два различных натуральных числа n и m называются дружественными, 
# если сумма делителей числа n (включая 1, но исключая само n) 
# равна числу m и наоборот. 
# Например, 220 и 284 – дружественные числа. 
# По данному числу k выведите все пары дружественных чисел, 
# каждое из которых не превосходит k. 
# Программа получает на вход одно натуральное число k, 
# не превосходящее 10^5. 
# Программа должна вывести  все пары дружественных чисел, 
# каждое из которых не превосходит k. 
# Пары необходимо выводить по одной в строке, 
# разделяя пробелами. 
# Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).
# Ввод: 1220
# Вывод:
# 220(1, 2, 4, 5, 10, 11, 20, 22, 44, 55 и 110 сумма делителей равна 284) 284(1, 2... 142 сумма делителей равна 220)

# 1184 1210


a=int(input('Введите максимальное число для дружественных чисел: '))
####отсюда запихнуть в фор
i=1
j=1
sum=0
sum2=0
while i<a:
    if a%i==0:
        sum+=i
    i=i+1
print(sum)
while j<sum:
    if sum%j==0:
        sum2+=j
    j=j+1
if a==sum2:
    print(f'Число {a} является дружественным для числа {sum}')













# int cntNumbers=0;
# for (int i = 2; i <= Math.Pow(10,6); i++){
#    int sumNumDividersOne=1;

#    for (int j = 2; j * j <= i; j++ )
#       if (i % j == 0) sumNumDividersOne += j + i/j;
#    if (i < sumNumDividersOne) {
#       if (i! = sumNumDividersOne){
#          int sumNumDividersTwo=1;
#          for (int j = 2; j * j <= sumNumDividersOne; j++ )
#             if (sumNumDividersOne % j == 0) sumNumDividersTwo+=j + sumNumDividersOne/j;

#          if (i == sumNumDividersTwo) {
#             cntNumbers++;
#             Console.WriteLine($"{cntNumbers}. Дружественные числа: " + 
#                               sumNumDividersTwo + " и " + sumNumDividersOne);     
#          }
#       }
#    }
# }