from itertools import count
from itertools import cycle


def my_count(start, stop):
    for i in count(start):
        if i > stop:
            return
        else:
            print(i)


def my_cycle(my_list):
    с = 0
    for i in cycle(my_list):
        if с == len(my_list):
            return
        print(i)
        с += 1


my_count(10, 100)
my_cycle([2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11])
