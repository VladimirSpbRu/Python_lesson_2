'''
Домашнее задание ко второму уроку
'''

'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
# i = 1
# while i<6:
#     print(i, '00000000000000000000')
#     i=i+1

'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
# number_of_fives = 0
# for i in range(10):
#     a = int(input('Введите цифру: '))
#     if a==5:
#         number_of_fives = number_of_fives+1
# print('Количество введенных цифр 5:', number_of_fives)

'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
# sum = 0
# for i in range(1,101):
#     sum+= i
# print(sum)

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
# mult = 1
# for i in range(1,11):
#     mult*= i
# print(mult)

'''
Задача 5
Вывести цифры числа на каждой строчке.
'''
# source_number = int(input('Введите целое число: '))
# aux_number = source_number
# quantity_of_digits = 0
# while aux_number > 0:
#     aux_number = aux_number//10
#     quantity_of_digits+= 1
# print('Количество цифр в числе:', quantity_of_digits)
# aux_number = source_number
# for i in range(quantity_of_digits-1, 0, -1):
#     print(aux_number//(10**i))
#     aux_number = aux_number - aux_number//(10**i)*(10**i)
# print(source_number%10)

'''
Задача 6
Найти сумму цифр числа.
'''
# number = int(input('Введите целое число: '))
# sum = 0
# while number > 0:
#     sum+= number%10
#     number = number//10
# print('Сумма цифр числа равна', sum)

'''
Задача 7
Найти произведение цифр числа.
'''
# number = int(input('Введите целое число: '))
# mult = 1
# while number > 0:
#     mult*= number%10
#     number = number//10
# print('Произведение цифр числа равна', mult)

'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
# number = int(input('Введите целое число: '))
# answer = 0
# while number > 0:
#     if number%10 == 5:
#         answer+= 1
#     number = number//10
# if answer>0:
#     print('Количество цифр 5 в числе:', answer)
# else:
#     print ('В числе нет цифр 5')

'''
Задача 9
Найти максимальную цифру в числе
'''
# number = int(input('Введите целое число: '))
# maximal_digit = 0
# while number > 0:
#     if number%10 > maximal_digit:
#         maximal_digit = number%10
#     number = number//10
# print('Максимальная цифра в числе равна', maximal_digit)

'''
Задача 10
Найти количество цифр 5 в числе
'''
# number = int(input('Введите целое число: '))
# number_of_fives = 0
# while number > 0:
#     if number%10 == 5:
#         number_of_fives = number_of_fives+1
#     number = number//10
# print('Количество цифр 5 во введенном числе равно', number_of_fives)
