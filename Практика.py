#Задание 1
# a = int(input())
# b = int(input())
# c = int(input())
# print (a + b + c)
# print (a * b * c)
#Задание 2
# a = int(input("Зарплата за месяц:"))
# b = int(input("Сумма месячного платежа:"))
# c = int(input("Задолженность:"))
# print (a + b + c)
#Задание 3
# a = int(input("Диагональ ромба:"))
# b = int(input("Диагональ ромба:"))
# print (a * b // 2)
#Задание 4
# print("to be\n", "\tor not \n\t" , "\tto be")
#Задание 5
# print("Life is happens\n","\t\twhen\n", "\tyou`re busy making others plans")
# print("\t\t\t\tJohn\n", "\t\t\t\t\tLennon")
##############################################################################
#1
# number1 = int(input("Введите первое число:"))
# number2 = int(input("Введите второе число:"))
# number3 = int(input("Введите третье число:"))
# print("Выберите операцию:")
# print("1. Сложить числа")
# print("2. Умножить числа")
#
# choice = input("Введите 1 или 2: ")
# if choice == '1':
#     result = number1 + number2 + number3
#     print(f"Сумма чисел: {result}")
# elif choice == '2':
#     result = number1 * number2 * number3
#     print(f"Произведение чисел: {result}")
# else:
#     print("Неправильный выбор.Введите 1 или 2.")
#2
# number1 = int(input("Введите первое число:"))
# number2 = int(input("Введите второе число:"))
# number3 = int(input("Введите третье число:"))
# print("Выберите операцию:")
# print("1.Максимум")
# print("2.Минимум")
# print("3.Среднее арифметическое")
#
# choice = input("Введите 1,2 или 3: ")
#
# if choice == '1':
#     result = max(number1, number2, number3)
#     print(f"Максимум:{result}")
# elif choice == '2':
#     result = min(number1, number2, number3)
#     print(f"Минимум:{result}")
# elif choice == '3':
#     result = (number1 + number2 + number3) / 3
#     print(f"Среднее арифметическое:{result}")
# else:
#     print("Неправильный выбор.Введите 1, 2 или 3.")
#3
# meters = int(input("Введите количество метров: "))
# print("Выберите, в какую единицу измерения перевести:")
# print("1.Мили")
# print("2.Дюймы")
# print("3.Ярды")
#
# choice = input("Введите 1, 2 или 3: ")
# if choice == '1':
#     miles = meters // 1609
#     print(f"{meters} метров равно {miles} миль.")
# elif choice == '2':
#     inches = meters * 39
#     print(f"{meters} метров равно {inches} дюймов (приблизительно).")
# elif choice == '3':
#     yards = meters
#     print(f"{meters} метров равно {yards} ярдов (приблизительно).")
# else:
#     print("Неправильный выбор.Введите 1, 2 или 3.")
##############################################################################
# 1
# day = int(input("Введите номер недели:"))
# if day == 1:
#     print("Понедельник")
# elif day == 2:
#     print("Вторник")
# elif day ==3:
#     print("Среда")
# elif day ==4:
#     print("Четверг")
# elif day ==5:
#     print("Пятница")
# elif day ==6:
#     print("Суббота")
# elif day ==7:
#     print("Воскресенье")
# else:
#     print("Нет такого дня недели")
# 2
# month_number = int(input("Введите номер месяца (1-12): "))
# match month_number:
#     case 1:
#         print("Январь")
#     case 2:
#         print("Февраль")
#     case 3:
#         print("Март")
#     case 4:
#         print("Апрель")
#     case 5:
#         print("Май")
#     case 6:
#         print("Июнь")
#     case 7:
#         print("Июль")
#     case 8:
#         print("Август")
#     case 9:
#         print("Сентябрь")
#     case 10:
#         print("Октябрь")
#     case 11:
#         print("Ноябрь")
#     case 12:
#         print("Декабрь")
#     case _:
#         print("Неправильный номер месяца. Пожалуйста, введите число от 1 до 12.")
# #3
# number = int(input("Введите число:"))
# if number > 0:
#     print("Number is positive")
# elif number < 0:
#     print("Nimber is negative")
# elif number == 0:
#     print("Number is equal to zero")
# else:
#     print("...")
# #4
# number1 = int(input("Введите число:"))
# number2 = int(input("Введите число:"))
# if number1 == number2:
#     print("Равно")
# elif number1 < number2:
#     print(number1, number2)
# else:
#     print(number2, number1)
##########################################
#1
# number =  int(input("Введите число от 1 до 100:"))
# if 1 <= number <=100:
#     if number % 3 == 0:
#         print("FIZ")
#     if number % 5 == 0:
#         print("BUZ")
#     if number % 5 == 0 and\
#         number % 3 == 0:
#         print("FIZ BUZ")
#     else:
#         print(number)
# else:
#     print("Неверно")
#2
# number = int(input("Введите число:"))
# result = number ** 0
# print(result)
# result = number ** 1
# print(result)
# result = number ** 2
# print(result)
# result = number ** 3
# print(result)
# result = number ** 4
# print(result)
# result = number ** 5
# print(result)
# result = number ** 6
# print(result)
# result = number ** 7
# print(result)
#############################################
#1
# start = int(input("Введите начало диапозона:"))
# end = int(input("Введите конец диапозона:"))
# if start > end:
#     print("Начало диапозона должны быть меньше конца.")
# else:
#     print(f"Числа кратные 7,в диапозоне {start} до {end}:")
# for number in range(start, end + 1):
#     if number % 7 == 0:
#         print(number)
# #2
# start = int(input("Введите начало диапазона: "))
# end = int(input("Введите конец диапазона: "))
#
# if start > end:
#     print("Начало диапазона должно быть меньше конца.")
# else:
#     print(f"Все числа диапазона от {start} до {end}:")
#     for number in range(start, end + 1):
#         print(number, end=' \n')
#
#     print(f"Все числа диапазона от {end} до {start} в убывающем порядке:")
#     for number in range(end, start - 1, -1):
#         print(number, end=' \n')
#
#     print(f"Числа, кратные 7, в диапазоне от {start} до {end}:")
#     for number in range(start, end + 1):
#         if number % 7 == 0:
#             print(number, end=' \n')
#
#     count_multiples_of_5 = 0
#     for number in range(start, end + 1):
#         if number % 5 == 0:
#             count_multiples_of_5 += 1
#
#     print(f"Количество чисел, кратных 5, в диапазоне от {start} до {end}: {count_multiples_of_5}")
