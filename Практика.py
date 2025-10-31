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
#3
# start = int(input("Введите начало диапазона: "))
# end = int(input("Введите конец диапазона: "))
#
# if start > end:
#     print("Начало диапазона должно быть меньше конца.")
# else:
#     for number in range(start, end + 1):
#         if number % 3 == 0 and number % 5 == 0:
#             print("Fizz Buzz")
#         elif number % 3 == 0:
#             print("Fizz")
#         elif number % 5 == 0:
#             print("Buzz")
#         else:
#             print(number)
#############################################################
#1
# numbers = (2, 5, 6, 8)
# product = 1
# for number in numbers:
#     product *= number
# print(product)
# #2
# numbers = (7, 5, 2, 9, 3)
# minimum = numbers[0]
# for number in numbers:
#     if number < minimum:
#         minimum = number
# print("Минимум:", minimum)
#3
# numbers = (3, 4, 5, 7, 10, 24, 25)
# prime_count = 0
# for num in numbers:
#     if num > 1:
#         is_prime = 1
#     for i in range(2, int(num**0.5) + 1):
#          if num % i == 0:
#             is_prime = 0
#             break
#     if is_prime:
#          prime_count += 1
# print("Количество простых чисел:", prime_count)
#4
# numbers = [2, 3, 4, 5, 6, 3, 15, 18, 22, 27]
# number_to_remove = 3
# removed_count = 0
# new_number = []
# for number in numbers:
#     if number == number_to_remove:
#         removed_count += 1
#     else:
#         new_number .append(number)
# numbers = new_number
# print("количество удалённых элементов:", removed_count)
#5
# a = (1, 3, 5)
# b = (2, 4, 6)
# num = a + b
# print("Объединённые списки:", num)
#6
# numbers = (1, 3, 4, 6, 8)
# power = 2
# result = ()
# for number in numbers:
#     result += (number ** power,)
# print("Результаты:", result)
###################################################
#1
# import random
# N = 20
# list_booble = []
# for i in range(N):
#     list_booble.append(random.randint(-10,10))
# print(f"Начальный список:{list_booble}")
# #левая половина
# for i in range(N//2):
#     for j in range(N//2 - 1 - i):
#        if list_booble[j] < list_booble[j + 1]:
#            list_booble[j], list_booble[j + 1] = list_booble[j + 1], list_booble[j]
# #правая половина
# for i in range(N//2):
#     for j in range(N//2, N -1):
#        if list_booble[j] > list_booble[j + 1]:
#            list_booble[j], list_booble[j + 1] = list_booble[j + 1], list_booble[j]
# print(f"Финальный список: {list_booble} ")
#2
# import random
# N = 45
# list_booble = []
# for i in range(N):
#     list_booble.append(random.randint(-20, 20))
# print(list_booble)
# for i in range(N//3):
#     for j in range(N//3 - 1 - i):
#         if list_booble[j] < list_booble[j+1]:
#             list_booble[j], list_booble[j+1] = list_booble[j+1], list_booble[j]
# for i in range(N//3):
#     for j in range(N//3, N - 1):
#         if list_booble[j] > list_booble[j + 1]:
#             list_booble[j], list_booble[j + 1] = list_booble[j + 1], list_booble[j]
# for i in range(N // 3):
#     for j in range(N // 3, N):
#         if list_booble[j] > list_booble[j // 2]:
#             list_booble[j], list_booble[j - 1] = list_booble[j - 1], list_booble[j]
# print(f"Финальный список: {list_booble} ")
################################################################
#1
# import re
#
# def is_cyrillic(text):
#     return bool(re.search('[а-яА-Я]', text))
#
# def calculate_score(text, points):
#     return sum([key for letter in text.upper() for key, value in points.items() if letter in value])
#
# def main():
#     point_en = {
#         1: 'AEIOULNSTR',
#         2: 'DG',
#         3: 'BCMP',
#         4: 'FHVWY',
#         5: 'K',
#         8: 'JX',
#         10: 'QZ'
#     }
#
#     point_ru = {
#         1: 'АВЕИЙНОСТ',
#         2: 'ДКМПУ',
#         3: 'БГЁЬЯ',
#         4: 'ЙЫ',
#         5: 'ЖЗЧЦ',
#         8: 'ШЭЮ',
#         10: 'ФЩЪ'
#     }
#
#     num_players = int(input("Введите количество игроков: "))
#     rounds = 10
#     scores = [0] * num_players
#
#     for round_number in range(1, rounds + 1):
#         print(f"\nРаунд {round_number}")
#         for player in range(num_players):
#             word = input(f"Игрок {player + 1}, введите слово: ").strip()
#             if is_cyrillic(word):
#                 score = calculate_score(word, point_ru)
#             else:
#                 score = calculate_score(word, point_en)
#
#             scores[player] += score
#             print(f"Игрок {player + 1} набрал {score} очков в этом раунде.")
#
#     print("\nИтоговые результаты:")
#     for player in range(num_players):
#         print(f"Игрок {player + 1}: {scores[player]} очков")
#
# if __name__ == "__main__":
#     main()
#2
# backpack = {
#     'Зажигалка': 20, 'Компас': 100, 'Фрукты': 500, 'Рубашка': 300,
#     'Термос': 1000, 'Аптечка': 200, 'Куртка': 600, 'Бинокль': 400,
#     'Удочка': 1300, 'Салфетки': 40, 'Бутерброды': 800, 'Палатка': 5500,
#     'Спальный мешок': 2500, 'Изолента': 250, 'Котел': 3000
# }
#
# massa = int(input("Введите допустимый вес рюкзака (в кг): ")) * 1000
#
# print("Могу взять:")
# for key, value in backpack.items():
#     if value < massa:
#         print(key, value ,end='')
# print()
# print("\nНе могу взять:")
# for key, value in backpack.items():
#     if value > massa:
#         print(key,value,end='')
#3
# def main():
#     note_book = {
#         "Маша": {
#             'tel': '+7922123561',
#             'vk': 'vk.com/masha321',
#             'youtube': 'youtube.com/masha321',
#             'telegram': 't.me/masha321'
#         },
#         "Наташа": {
#             'tel': '+7922123562',
#             'vk': 'vk.com/natasha321',
#             'youtube': 'youtube.com/natasha321',
#             'telegram': 't.me/natasha321'
#         },
#         "Петя": {
#             'tel': '+7922123563',
#             'vk': 'vk.com/petya321',
#             'youtube': 'youtube.com/petya321',
#             'telegram': 't.me/petya321'
#         }
#     }
#
#     user_search = input("Введите имя контакта: ").capitalize()
#     if user_search in note_book:
#         contact = note_book[user_search]
#         print(f"Контакт: {user_search}")
#         print(f"Телефон: {contact['tel']}")
#         print(f"VK: {contact['vk']}")
#         print(f"YouTube: {contact['youtube']}")
#         print(f"Telegram: {contact['telegram']}")
#     else:
#         print("Контакт не найден.")
#
# if __name__ == "__main__":
#     main()
