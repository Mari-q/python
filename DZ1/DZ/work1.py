# # Задача 1: Найдите сумму цифр трехзначного числа.
# n=int(input("Введите трехзначное число n:  "))
# print(n)
# print(n//100 + (n//10)%10 + n%10)

# Задача 2: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# s = int(input())
# print((s//6), ((s//6)*4), (s//6))

# Задача 3: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость 
#билета.
# a = int(input('Введите номер билета: '))  
# sum_left = 0
# sum_right = 0
# for i in range(6):
#     if i < 3:
#         sum_right += a // 10**i % 10
#     else:
#         sum_left  += a // 10**i % 10 
# if sum_left == sum_right:
#    print('yes')
# else:
#     print('no')  

# Задача 4: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку 
#на два прямоугольника).
n = int(input("введите число n "))
m = int(input("Введите число m "))
k = int(input("введите число K "))
if k < m*n and (k%m==0 or k%n==0):
    print('YES')
else:
    print('NO')