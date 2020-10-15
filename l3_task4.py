def my_sqr1(a, b):
    """
        возвращает число a в степени b через возведение в степень
        :param a: число, больше 0
        :param b: число, меньше 0
        :return: число
    """
    return a ** b


def my_sqr2(a, b):
    """
        возвращает число a в степени b через умножение
        :param a: число, больше 0
        :param b: число, меньше 0
        :return: число
    """
    b = abs(b)
    r = 1
    if b > 0:
        while b != 0:
            r *= a
            b -= 1
        return 1 / r
    else:
        return 1


while True:
    try:
        nums = input("Укажите 2 числа через пробел первое положительное, "
                     "второе отрицательное ('Q' для выхода):").split()
        if nums[0].upper() == "Q":
            break
        if int(nums[1]) > 0 or int(nums[0]) < 0:
            print('Первое положительное, второе отрицательное!')
        else:
            print(f'Ответ 1 : {nums[0]} в степени {nums[1]} =  {my_sqr1(int(nums[0]), int(nums[1]))}')
            print(f'Ответ 2 : {nums[0]} в степени {nums[1]} =  {my_sqr2(int(nums[0]), int(nums[1]))}')
    except IndexError:
        print("Мало аргументов")
    except ValueError:
        print("Один или несколько параметров не число")
