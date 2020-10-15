def my_sum(a, b, c):
    """
        Возвращает сумму двух наибольших чисел (sum - min)
        :param a: число
        :param b: число
        :param c: число
        :return: число
    """
    return sum([a, b, c])-min([a, b, c])


while True:
    try:
        nums = input("Укажите 3 числа через пробел ('Q' для выхода):").split()
        if nums[0].upper() == "Q":
            break
        print(f'Сумма двух наибольших значений =  {my_sum(float(nums[0]),float(nums[1]),float(nums[2]))}')
    except IndexError:
        print("Мало аргументов")
    except ValueError:
        print("Один или несколько параметров не число")
