
original_password = 'x777'  # правильный пароль, хранится в программе
password = input('Введите пароль: ')  # просим пользователя ввести пароль
access = False  # переменная, хранит разрешение на доступ
if password == original_password:  # если введен правильный пароль
    print('Пароль принят, добро пожаловать в систему')
    access = True
else:
    password != original_password  # если введен неправильный пароль
    print('Пароль неверен, вход запрещен')
