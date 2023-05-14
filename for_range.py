# elements = range(123)
# print(len(elements))

# print(list(range(-11, -36, -1)))

# for i in range(100, 1000):
#     if i % 2 == 0 and i % 7 == 0:
#         print(i)

# for i in range(1, 11):
#     print(i, i**2)
#     print('*'*i) # (2**i)

# from random import randint
# s = 0
# for i in range(3):
#     a = randint(1, 10)
#     print(a, end=' ')

# n = int(input())
# s = 0
# for i in range(n):
#     a = int(input())
#     s += a
#     print('current s:', s)
# print('total', s)
# print('sredn arifm=', s/n)

# summa = 0
# for i in range(1, 101):
#     summa = summa + i
# print(summa)

# factorial
# n = 1
# for i in range(1, 5):
#     n = n + i
# print(n)

# найти факториал числа n
# n = int(input('Введите число: '))
# pr = 1
# for i in range(1, n+1):
#     pr = pr * i
#
# print(f'Факториал {n} = {pr}')

# n = int(input())
# for i in range(1, n+1):
#     print(i)

# for i in range(1, int(input()) + 1):
#     print(i)

# for i in range(0, 501, 5):
#     print(i)
# print(*range(0, 501, 5), sep='\n')

# n = int(input())
# for i in range(n, 0, -1):
#     print(i)
#
# for i in range(int(input()), 0, -1):
#     print(i)

# phrase = str(input())
# quantity = int(input())
# for i in range(quantity):
#     print(phrase)

# a, b = int(input()), int(input())
#
# for i in range(a, b+1):
#
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

# a, b = int(input()), int(input())
#
# for i in range(a, b+1):
#     print(f"Число {i}; его квадрат = {i**2}; его куб = {i**3}")

# number = int(input())
# n = 0
# for i in range(1, number):
#     if i % 3 == 0 or i % 5 == 0:
#         n += i
# print(n)
#
# print(sum([i for i in range(int(input())) if not i % 3 or not i % 5]))

# s = 0
# for i in range(50, 101):
#     s += i**3
# print(s)
# print(sum([(i**3) for i in range(50, 101)]))

# n = int(input())
# n1 = 1
# for i in range(1, n+1):
#     n1 *= i
# print(n1)

# quantity = int(input())
# mishka = 0
# chris = 0
#
# for i in range(quantity):
#     mishka_dice, chris_dice = map(int, input().split())
#     if mishka_dice > chris_dice:
#         mishka += 1
#     elif chris_dice > mishka_dice:
#         chris += 1
# if mishka > chris:
#     print("Mishka")
# elif chris > mishka:
#     print("Chris")
# else:
#     print("Friendship is magic!^^")

# quantity = int(input())
#
# for i in range(quantity):
#     word = input().lower()
#     if 'рок' in word:
#         print(i+1, word.find('рок')+1)

# quantity = int(input())
# words_with_salt = []
# for i in range(quantity):
#     words = input()
#     if 'соль' not in words:
#         words_with_salt.append(words)
# print(', '.join(words_with_salt))

# quantity = int(input())
#
# for i in range(quantity):
#     word = input()
#     if len(word) > 10:
#         abbreviation = word[0] + str(len(word)-2) + word[-1]
#         print(abbreviation)
#     else:
#         print(word)

# phrase = input().split()
# empty_list = []
# for i in phrase:
#     if i.lower() not in [empty_list_lower.lower() for empty_list_lower in empty_list]:
#         empty_list.append(i)
#
# print(' '.join(empty_list))

# a = [1, 2, 3, 4, 32, 5, 3, 8, 7, 5]
# even = []
# odd = []
# n = len(a)
# for i in range(n):
#     if a[i] % 2 == 0:
#         even.append(i+1)
#     else:
#         odd.append(i+1)
#
# print(even)
# print(odd)

# s = 'Hello WorlD'
# for i in s:
#     if i >= 'a' and i <= 'z':
#         print(i, 'small')
#     elif "A" <= i <= "Z":
#         print(i, 'big')
#     else:
#         print(i) # находит строчные и заглавные буквы

# vowels = 'aeiou'    # гласные
# s = 'aertiooukjikld'
# n = len(s)
# for i in range(n-1):
#     if s[i] in vowels and s[i+1] in vowels:
#         print(s[i], s[i+1])

# a = [43, 65, 3, 54, 6]
# for i in a:
#     i += 5
#     print(i, end=" ")
# print()
# print(a) #  48 70 8 59 11 # [43, 65, 3, 54, 6]

# a = [43, 65, 3, 54, 6]
# for i in a:
#     print(i, a.index(i))  # обойти все элементы и указать на каком месте стоит каждый из элементов

# a = [43, 65, 3, 43, 6, 43]
# for i in range(5):
#     print(i, a[i]) # вариант обхода элементов списка – обход по индексам

# a = [43, 65, 3, 43]
# b = len(a)
# for i in range(b):
#     a[i] += 5
# print(a)

# a = [1, 2, 3, 4, 32, 4, 5, 3, 5]
# b = []
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b) # [1, 2, 3, 4, 32, 5]

# for letter in 'python':
#     if letter == 'h':
#         break
#     print(f"Current letter: {letter}")
# print("End exercise!")

# for letter in 'Python':
#     if letter == 'h':
#         break
#     print(f'Current Letter : {letter}')
# else:
#     print('Мы сюда не попадем')
#
# print('-' * 20)
#
# for letter in 'Python':
#     if letter == 'W':
#         break
#     print(f'Current Letter : {letter}')
# else:
#     print('А вот здесь мы побываем')
# print('Закончили упражение!')

# for letter in 'AbracadabRa':
#   if letter == 'a':
#       continue
#   print(f'Current Letter : {letter}')
# print('Закончили упражнение!')

# for letter in 'AbracadabRa':
#   if letter == 'a':
#       continue
#   print(f'Current Letter : {letter}')
# print('Закончили упражнение!')

# numbers = [23, 324, 2, 33, -4, 9]
# for i in range(len(numbers)):
#     numbers[i] *= 2
# print(numbers)
#
# numbers = [i*2 for i in numbers]
# print(numbers)

# quantity = int(input())
# e_list = []
# for i in range(quantity):
#     word = input()
#     e_list.append(word)
# print(e_list)
#
# print([input() for i in range(int(input()))])
#
# list = []
# for i in range(int(input())):
#     list.append(input())
# print(list)

# letter = input()
# string = input().split()
# result = [word for word in string if letter in word.lower()]
# print(result)

# letter = input()
# string = input().split()
# a = len(string)
# for i in range(a):
#     if letter in string[i]:
#         print(string[i])
#
# letter = input()
# string = input()
#
# words = string.split()
# result = []
# for word in words:
#     if letter.lower() in word.lower():
#         result.append(word)
# print('\n'.join(result))
#
# s = input()
# lst = input().split()
# for i in range(len(lst)):
#     if s in lst[i].lower():
#         print(lst[i])

# numbers = list(map(int, input().split())) # Линейный поиск, код ищет позицию (индекс)
#                                           заданного числа в списке.
# number = int(input())
# n = len(numbers)
# for i in range(n):
#     if numbers[i] == number:
#         print(i + 1)
#         break
# else:
#     print("ErrorValue")

# numbers = list(map(int, input().split()))
# e_list = []
# for i in range(len(numbers)):
#     if numbers[i] > 0:
#         e_list.append(numbers[i])
# if len(e_list) > 0:
#     print(min(e_list))
# else:
#     print("Empty")

# a = [2, 1, 2, 3, 2, 1, 2, 3, 3, 2, 4, 3, 5, 3, 2]
# count = [0]
# for i in a:
#     count[i] += 1
# print(count)

# a = [2, 1, 2, 3, 2, 1, 2, 3, 3, 2, 4, 3, 5, 3, 2]
# count = [0] * 6
# for i in a:
#     count[i] += 1
# for i in range(6):
#     if count[i] > 0:
#         print((str(i) + " ") * count[i], end="")

# s = "abcZVjhdf HG jgkfYGg jhgkdf 543 *(^$&*#"
# letters = [0] * 26
# for i in s.lower():
#     if i >= 'a' and i <= 'z':
#         nomer = ord(i) - 97
#         letters[nomer] += 1
# for i in range(26):
#     if letters[i] > 0:
#         print(chr(i + 97), *letters[i], end='')

# a = []
# import random
#
# for i in range(10):
#     a.append(random.randint(-10, 10))
#
# count = [0]*21
# for i in a:
#     count[i + 10]+=1
# for i in range(21):
#     print(i-10, count[i])

# number = list(map(int, input()))
# count = [0] * 10
# for i in number:
#     count[i] += 1
# for i in range(10):
#     if count[i] > 0:
#         print(i, count[i])

# import random
# quantity = int(input())
# e_list = []
# for i in range(100):
#     numbers = list(map(int, input()))
#     e_list.append(random.randint(-100, 100))
#
# count = [0]*201
# for i in e_list:
#     count[i + 100] += 1
#
# for i in range(1, 201):
#     count[i] += count[i+1]

# quantity = int(input())
# my_list = list(map(int, input().split()))
#
# count = [0] * 201
# for i in my_list:
#     count[i + 100] += 1
# sorted_list = []
# for i in range(-100, 101):
#     sorted_list.extend([i] * count[i + 100])
# print(' '.join(map(str, sorted_list)))

# a = input()
# b = list(map(int, input().split()))
# rez = []
# for i in range(-100, 101):
#     if i in b:
#         for j in range(b.count(i)):
#             rez.append(i)
# print(*rez)

# s = input()
# for i, c in enumerate(s):
#     print(c * (i+1))


# s = input()
#
#
# def find_longest_sequence(s):
#     max_len = 0
#     len_current = 1
#     res = ''
#     for i in range(1, len(s)):
#         if s[i] == s[i - 1]:
#             len_current += 1
#         else:
#             if len_current >= max_len:
#                 max_len = len_current
#                 res = s[i - 1]
#             len_current = 1
#
#     # Check sequence of the last character
#     if len_current >= max_len:
#         max_len = len_current
#         res = s[-1]
#
#     return res, max_len
#
#
# res, acc = find_longest_sequence(s)
# print(res, acc)
