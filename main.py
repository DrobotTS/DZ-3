print('1) У вас есть список my_list с значениями типа int.Распечатать те значения, которые больше 100 Задание выполнить с помощью цикла for.')
# вариант 1

from random import randint
my_list = []
result = []
for elements in range (10):
    my_list.append(randint(0, 200))
print(f"Your list: {my_list}")
for end in my_list[:]:
    if end > 100:
        result.append(end)
print(f"Your result: {result}")

# вариант 2

my_list = [1, 2, 3, 4, 5, 100, 200, 300, 400]
results = []
for elements in my_list:
    if elements > 100:
        results.append(elements)
for elements in results:
    print(elements)