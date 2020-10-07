num = int(input('Введите число:'))
digit = 0
while num // 10 > 0:
    if num % 10 > digit:
        digit = num % 10
    num = num // 10
print(f'Максимальная цифра = {digit}')
