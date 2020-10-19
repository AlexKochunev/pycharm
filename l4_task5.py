from functools import reduce


def my_sum(a, b):
    return a+b


my_list = [i for i in range(100, 1000, 1) if i % 2 == 0]
print(reduce(my_sum, my_list))
