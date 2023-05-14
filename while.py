# a = [1, 3, 4, 3, 6, 3]
# while 3 in a:
#     a.remove(3)
# print(a)

# Программа распечатывает посимвольно слово ‘privet’
# a = 'privet'
# while len(a) > 0:
#     print(a[0])
#     a = a[1:]

# Программа заставляет вводить пользователя пароль до тех пор, пока не будет введен правильный
# q = input("Введите пароль:")
# count = 0
# password = "qwerty"
# while q != password:
#     count += 1
#     print("Wrong password")
#     q = input("Введите пароль вновь: ")
# print("Right password")
# print(f"Количество неправильных попыток: {count}")

# phrase = input('Введите фразу: ')
# while phrase != 'стоп':
#   print('Продолжаем веселиться!')
#   phrase = input('Введите фразу: ')
# print('Закончили вечеринку!')

# while (phrase := input('Введите фразу: ')) != 'стоп':
#   print('Продолжаем веселиться!')
# print('Закончили вечеринку!')

# a = 1000
# while a != 2000:
#     a += 1
#     print(a)

# a = 6790
# while a != 195:
#     a -= 5
#     print(a)

# a, b = map(int, input().split())
# y = 0
# while a <= b:
#     a *= 3
#     b *= 2
#     y += 1
# print(y)

# word = input()
# print(word)
# while len(word) > 0:
#     word = word[1:-1]
#     print(word)

# number = int(input())
# n = 1
# while n ** 2 <= number:
#     print(n ** 2)
#     n += 1

# x, y = map(int, input().split())
# d = 1
# while x < y:
#     x *= 1.15
#     d += 1
# print(d)

# s1, s2 = map(int, input().split())
# days = 0
#
# while s1 > 0:
#     s1 -= 1
#     days += 1
#     if days % s2 == 0:
#         s1 += 1
# print(days)

# candle1, candle2 = map(int, input().split())
#
# hours = candle1
#
# while candle1 >= candle2:
#     candles = candle1 // candle2
#     hours += candles
#     candle1 = candles + candle1 % candle2
# print(hours)

# number = int(input())
#
# n = 1
# x = 0
# while n < number:
#     n *= 2
#     x += 1
# if n == number:
#     print(x)
# else:
#     print("НЕТ")

# 1. Сначала мы записываем в переменную number целое число, которое будет получено от пользователя.
# 2. Далее запускается цикл while, который будет работать до тех пор, пока первая цифра в
# числе number не станет единицей и число не достигнет значение 1000000000.
# 3. Внутри цикла мы проверяем первую цифру числа, используя условие str(number)[0] != '1'.
# Если это условие выполняется, то мы умножаем первую цифру числа на само число и
# записываем новое значение в переменную number.
# 4. Если же условие не выполняется, то цикл прекращается и мы переходим к следующей строке кода.
# 5. Наконец, мы выводим полученное значение number. Таким образом, код выполняет умножение
# первой цифры заданного числа на само это число до тех пор, пока первая цифра
# не станет равна единице или число не достигнет 1000000000.

# number = int(input())
# while str(number)[0] != '1' and number < 1000000000:
#     number = int(str(number)[0]) * number
# print(number)

# summa = 0
# number = int(input())
# while number != 0:
#     summa += number
#     number = int(input())
# print(summa)

# n = 4782
# while n > 0:
#     print(n % 10)
#     n = n // 10

# Узнаем сколько разрядов в числе
# n = int(input('Введите число: '))
# count = 0
# while n > 0:
#     n = n//10
#     count = count + 1
# print(f"Количество цифр={count}")

# Найдем сколько всего четных цифр
#
# n = int(input("Enter number"))
# count_even = 0
# while n > 0:
#     last = n % 10
#     if last% 2 == 0:
#         count_even = count_even + 1
#     n = n // 10
# print(f"Количество четных цифр = {count_even}")

# Посчитаем сумму всех цифр числа
# n = int(input('Введите число: '))
# s = 0
# while n > 0:
#     s = s + n % 10
#     n = n//10
# print(f"Сумма всех цифр = {s}")

# Посчитаем произведение всех цифр числа
# n = int(input('Введите число: '))
# product = 1
# while n > 0:
#     last = n % 10
#     product = product * last
#     n = n//10
# print(f"Произведение всех цифр = {product}")

# Найдем самую большую и самую маленькую цифру в числе
# n = int(input('Введите число: '))
# maximum = 0
# minimum = 9
# while n > 0:
#     last = n% 10
#     if last > maximum:
#         maximum = last
#     if last < minimum:
#         minimum = last
#     n = n //10
#
# print(f"Самая большая цифра = {maximum}")
# print(f"Самая маленькая цифра = {minimum}")

# number = int(input())
# summa = 0
# while number > 0:
#     summa = summa + number % 10
#     number = number // 10
# print(summa)

# number = int(input())
# a = 1
# while number > 0:
#     b = number % 10
#     a *= b
#     number //= 10
# print(a)

# number = int(input())
# maximum = 0
# minimum = 9
# while number > 0:
#     last_number = number % 10
#     if last_number > maximum:
#         maximum = last_number
#     if last_number < minimum:
#         minimum = last_number
#     number = number // 10
# print(minimum)
# print(maximum)

# number = int(input())
# n = 0
# while number > 0:
#     if number % 10 == 7:
#         n += 1
#     number = number // 10
# print(n)

# lst = ''.join(list(input()))
# print(f'{lst.count("7")}')

# Программа принимает на вход одно натуральное число и выводит его цифры
# в двоичной системе в столбик в обратном порядке.
# number = int(input())
# while number > 0:
#     last_number = number % 2
#     print(last_number)
#     number = number // 2

# n = int(input())
# i = 1
# while i <= n//2:
#     if n % i == 0:
#         print(i, end=' ')
#     i += 1

# n = int(input())
# i = 1
# a = []
# while i*i <= n:
#     if n % i == 0:
#         a.append(i)
#         if i !=n//i:
#             a.append(n//i)
#     i += 1
# a.sort()
# print(a)

# n = int(input())
# i = 1
# a = []
#
# while i ** 2 <= n:
#     if n % i == 0:
#         a.append(i)
#         if i != n // i:
#             a.append(n // i)
#     i += 1
#
# if len(a) == 2:
#     print('Yes')
# else:
#     print('No')

# находит сумму его делителей.
# number = int(input())
# summa = 0
# i = 1
# while i <= number:
#     if number % i == 0:
#         summa += i
#     i += 1
# print(summa)

# a, b = map(int, input().split())
#
# while a != b:
#     if a > b:
#         a = a - b
#     else:
#         b = b - a
# print(a)

# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# while b > 0:
#     c = a % b
#     a = b
#     b = c         # a, b = b, a % b
# print(f'Нод={a}')

# first_number, second_number = map(int, input().split())
# while second_number > 0:
#     first_number, second_number = second_number, first_number % second_number
# print(first_number)

# a, b = map(int, input().split())
# nod = 0
# z, v = a, b
# while b != 0:
#     nod = a % b
#     a, b = b, nod
# nok = (z * v) // a
# print(nok)

# a = 0
# while a <= 10:
#     a += 1
#     if a % 2 != 0:
#         continue
#     print(a)

# a = [24, 68, 42, 32, 23, 18, 22]
#
# while len(a) > 0:
#     last = a.pop()
#     if last % 2 !=0:
#         print("No")
#         break
#     print(f'{last} четное число')
# else:
#     print('Yes')

# number = int(input())
# count = 2
# while number % count != 0:
#     count += 1
#     if count == number:
#         break
# print(count)

# a = int(input())
# b = int(input())
# a -= 1
# while a < b:
#     a += 1
#     if a % 777 == 0:
#         break
#     if a % 2 == 0 or a % 3 == 0:
#         continue
#
#     print(a)

# number = int(input())  # вводим число
# count = 0  # инициализируем счетчик шагов
#
# while number != 1:  # пока число не равно 1
#     if number % 2 == 0:  # если число четное
#         number /= 2  # заменяем его на n/2
#     else:  # если число нечетное
#         number = 3 * number + 1  # заменяем его на 3n + 1
#     count += 1  # увеличиваем счетчик шагов
#
# print(count)  # выводим количество шагов

# word = str(input())
# count = 0
# while count < len(word):
#     letter = word[count]
#     if letter == 'e' or letter == 'a':
#         print("Ага! Нашлась")
#         break
#     else:
#         print(f"Текущая буква:", letter)
#         count += 1
# else:
#     print("Распечатали все буквы")

# word = list(input())
# q = 0
# while len(word) != 0:
#     q = word.pop(0)
#     if q == 'e' or q == 'a':
#         print('Ага! Нашлась')
#         break
#     if q != 'e' or q != 'a':
#         print('Текущая буква:', q)
# else:
#     print('Распечатали все буквы')

# num = int(input())  # вводим число, которое нужно проверить
#
# reverse_num = 0  # здесь будет записано число, полученное переворачиванием порядка цифр num
# temp = num  # временная переменная для хранения num
#
# while temp > 0:
#     remainder = temp % 10  # получаем остаток от деления на 10, чтобы получить последнюю цифру
#     reverse_num = reverse_num * 10 + remainder  # добавляем последнюю цифру к числу
#     # без этой цифры
#     temp //= 10  # удаляем последнюю цифру из temp, деля ее на 10
#
# if num == reverse_num:  # проверяем, равны ли исходное число и его перевернутое значение
#     print(True)
# else:
#     print(False)
# тоже самое через строки
# s = input()
# print(s == s[::-1])

# stack = []  # создаем пустой стек и читаем первое число
# number = int(input())  # читаем первое число
# while number != -1:  # повторяем цикл до тех пор, пока не будет введен -1
#     stack.append(number)  # добавляем число в стек
#     number = int(input())  # читаем следующее число
# while len(stack) > 0:  # повторяем цикл, пока стек не опустеет
#     print(stack.pop())  # извлекаем число из стека и выводим его на экран

# stack = []  # Создаем пустой стек
# command = ""    # Создаем переменную для хранения вводимой команды
# # Запускаем бесконечный цикл, который будет выполняться, пока пользователь не введет команду "close"
# while command != "close":
#     command = input()
#     if command.split()[0] == "add":  # Если команда начинается с "add", то добавляем заданный элемент в стек
#         stack.append(int(command.split()[1]))
#     elif command == "pop":      # Если команда равна "pop", то извлекаем элемент из стека
#         print(stack.pop())
#     elif command == "head":      # Если команда равна "head", то выводим верхний элемент стека
#         print(stack[-1])
#     elif command == "close":
#         break      # Если команда равна "close", то завершаем работу программы (выходим из цикла)

# from queue import Queue
# q = Queue()
# while True:
#     cmd = input().strip().split()
#     if cmd[0] == "add":
#         q.put(int(cmd[1]))
#     elif cmd[0] == "pop":
#         if not q.empty():
#             print(q.get())
#     elif cmd[0] == 'head':
#         if not q.empty():
#             print(q.queue[0])
#     elif cmd[0] == 'close':
#         break







