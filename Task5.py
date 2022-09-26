# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

a = [1, 4, 43, 6, 5, 11]

s = 0
for i in range (len(a)):
    if i%2 != 0:
        s += a[i]
    
print(s)

print("Variant 2:")

elements = [1, 4, 43, 6, 5, 11]
print(elements)
res = 0
for i, item in enumerate(elements): # enumerate
    item = int(item)
    if i % 2 == 1:
        res += item
print(res)