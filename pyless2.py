# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

# n = int(input("Введите количество элементов первого набора "))
# list1 = list(range(0,n))
# finaly = []

# for ind in range(n):
#     list1[ind] = int(input(f"Введите {ind + 1}-e число набора 1 "))
# print(list1)
# print()
# m = int(input("Введите количество элементов второго набора "))
# list2 = list(range(0,m))
# for j in range(m):
#     list2[j] = int(input(f"Введите {j + 1}-e число набора 2 "))
# print(list2)
# nset = set(list1)
# mset = set(list2)
# s_set = sorted(nset.intersection(mset))
# print()
# print(sorted(nset))
# print(sorted(mset))
# print(*s_set)
            
        



# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на ind-ом кусте выросло a[ind] ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном списке урожайности грядки.

# import random
# bush = int(input("введите количество кустов: "))
# ber = list(random.randint(0, 10) for ind in range(bush))
# res = []
# ind = 0
# sum = 0

# print(ber)

# while (ind < bush):
#     if (ind == bush - 1):
#         sum = ber[ind] + ber[ind - 1] + ber[0]
#     else:
#         sum = ber[ind] + ber[ind - 1] + ber[ind + 1]
#         res.append(sum)
#         res.sort()
#     ind += 1

# print(f"Максимальное количество ягод собранных за один заход - {res[-1]}")