# Вы работаете над разработкой программы для проверки корректности даты, введенной пользователем.
# На вход будет подаваться дата в формате "день.месяц.год". Ваша задача - создать программу,
# которая проверяет, является ли введенная дата корректной или нет.
# Ваша программа должна предоставить ответ "True" (дата корректна)
# или "False" (дата некорректна) в зависимости от результата проверки.

# from datetime import datetime
#
#
# def validate_date(date):
#     try:
#         datetime.strptime(date, '%d.%m.%Y')
#         return True
#     except ValueError:
#         return False
#
#
# date_to_prove = "15.4.2023"
# print(validate_date(date_to_prove))


# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях, включающий в себя
# функцию is_attacking(q1,q2), проверяющую, бьют ли ферзи друг друга и check_queens(queens),
# которая проверяет все возможные пары ферзей.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь. Не забудьте напечатать результат.
import random
from random import randint


def check_queens(queens):
    temp = [(i, j) for i in queens for j in queens if i != j]
    if temp != []:
        for i in range(8):
            for j in range(i + 1, 8):
                if temp[i][0] == temp[j][0] or \
                        temp[i][1] == temp[j][1] or \
                        abs(temp[i][0] - temp[j][0]) == abs(temp[i][1] - temp[j][1]):
                    return False
    return True

# print(check_queens(queens=[(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1)]))


def generate_boards():
    result = []
    while len(result) < 4:
        positions = generate_positions()
        x = check_queens(positions)
        if x is False:
            result.append(positions)
    return result


def generate_positions():
    positions = [(randint(0,9),randint(0,9)) for i in range(8)]
    return positions


board_list = generate_boards()
print(board_list)
