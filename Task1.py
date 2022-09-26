# Задание 1 Напишите программу, которая принимает
# на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

# Variant 1:
number = float(input("please type a number: "))
st = str(number)
a = list(st)
h = 0
for i in range(len(a)):
    if a[i] == '.':
        continue
    h += int(a[i])
print(h)

# Variant 2:
print('Variant 2:')
number = input("please type a number: ")
my_list = [i for i in number if i not in {',', '.'}]       # list comprehension
print(sum(map(int, my_list)))    # map



