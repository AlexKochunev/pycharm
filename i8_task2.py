class MyZeroDivError(Exception):
    def __init__(self, txt):
        self.txt = txt


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
        if float(nums[1]) == 0:
            raise MyZeroDivError("На ноль делить нельзя")
        print(f'{float(nums[0])} / {float(nums[1])} = {div_func(float(nums[0]),float(nums[1]))}')
    except MyZeroDivError as err:
        print(err)
    except IndexError:
        print("Мало аргументов")
    except ValueError:
        print("Один или оба параметра не число")
