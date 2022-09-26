import random

# sum_2 = lambda a, b: a + b
# f = lambda x: x**3
# list = [(i, f(i)) for i in range(1,21) if i%2 == 0]

list1 = ['x^3', 'x^2', 'x' ]
list2 = [2, 5, 6]

list_t = list(zip(list2, list1))

k = int(input("Введите натуральную степень k: "))

list_koef = [random.randint(1, 100) for i in range(k-1)]
list_x = ["x^" for i in range(k+1) if i >1]
list_k = list((i for i in range(k+1)))
list_f = list(filter(lambda x: x > 1, list_k))

list_zipped = list(zip(list_koef, list_x, list_f))
list_en = list(enumerate(list_zipped))
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

print(str_w2)

