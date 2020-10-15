def div_func(a, b):
    """
        Возвращает результат деления a на b
        :param a: число
        :param b: число
        :return: число
    """
    return a / b


while True:
    try:
        nums = input("Укажите делимое и делитель через пробел ('Q' для выхода):").split()
        if nums[0].upper() == "Q":
            break
        print(f'{float(nums[0])} / {float(nums[1])} = {div_func(float(nums[0]),float(nums[1]))}')
    except ZeroDivisionError:
        print("На ноль делить нельзя")
    except IndexError:
        print("Мало аргументов")
    except ValueError:
        print("Один или оба параметра не число")
