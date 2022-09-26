# 4 Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# *Пример:* 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# ЗДЕСЬ ПЕРВОНАЧАЛЬНЫЙ ВАРИАНТ И ДВА ДОПОЛНИТЕЛЬНЫХ. ТРЕТИЙ ВАРИАНТ ПОЛУЧАЕТСЯ СЛОЖНЕЕ, Я НАПИСАЛА ТОЛЬКО ДЛЯ ТОГО 
# ЧТОБЫ ИСПОЛЬЗОВАТЬ ZIP. рЕЗУЛЬТАТЫ ВЫВОЖУ В КОНСОЛЬ, А НЕ В ФАЙЛ

import random

k = random.randint(0, 100)

k = int(input("Введите натуральную степень k: "))
list_koef = []

for i in range(k):
    if (k - i) > 1:
        degr = str(k - i)
        add = '*x^'
    else:
        degr = ''
        add = '*x'
    list_koef.append(str(random.randint(0, 100)) + add + degr)      

final_str = ''

for i in range(len(list_koef)):
    final_str = final_str + list_koef[i] + ' + '

last_element = str(random.randint(0, 100))
final_str = final_str + last_element + " = 0"

with open('Task4.txt', 'w') as data:
    data.write(final_str) 


print('Variant 2')

# k = int(input("Введите натуральную степень k: "))
list_koef = [str(random.randint(1, 100)) + "x^" + str(i) + " + " for i in range(k+1) if i > 1]
string1 = ''
for i in range(len(list_koef)):
    string1 = str(list_koef[i]) + string1

string1 = string1 + str(random.randint(1, 100)) + 'x + ' + str(random.randint(1, 100)) + ' = 0'

print(string1)    # я вывела на консоль, а не записывала в файлик.


print("Variant 3")

k = int(input("Введите натуральную степень k: "))

list_koef = [random.randint(1, 100) for i in range(k-1)]
list_x = ["x^" for i in range(k+1) if i >1]
list_k = list((i for i in range(k+1)))
list_f = list(filter(lambda x: x > 1, list_k))     # filter, lambda, list comprehension
list_zipped = list(zip(list_koef, list_x, list_f))  # zip

str_w = ''

for i in range(len(list_zipped)):
    str_w = str(list_zipped[i]) + str_w
str_w2 = ''
for i in str_w:
    if i in {'(', ',', "'", ' '}:
        continue
    elif i == ')':
        str_w2 = str_w2 + ' + '
    else:
        str_w2 = str_w2 + i

str_w2 = str_w2 + str(random.randint(1, 100)) + 'x + ' + str(random.randint(1, 100)) + " = 0"

print(str_w2)  # я вывела на консоль, а не записывала в файлик.