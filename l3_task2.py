def user_print(name, surname, birth, residence, email, phone):
    """
        Возвращает строку сообщей информацией
        :param name: строка
        :param surname: строка
        :param birth: строка
        :param residence: строка
        :param email: строка
        :param phone: строка
        :return: строка
    """
    return f'{name} {surname}, {birth} года рождения, проживает в городе {residence}, ' \
           f'email - {email}, телефон - {phone}'


print(user_print(name='Александр', surname='Кочунёв', birth='1986', residence='Зеленоград',
                 email='tarantul@rezonit.ru', phone='+7916*******'))
