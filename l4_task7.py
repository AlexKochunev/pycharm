from itertools import count


def fact_gen():
    r = 1
    for i in count(1):
        r *= i
        yield r


def get_fact(n):
    if n == 0:
        return 1
    for j, f in enumerate(fact_gen()):
        if j == n - 1:
            print(f)


print(get_fact(4))
