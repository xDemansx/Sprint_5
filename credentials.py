import random

class Credentials():
    # Данные для предрегистрации/проверки входа
    my_name = 'Dmitriy' # Имя
    my_email = 'Dmitriy_28@mail.ru' # Почта
    my_password = '123qwe' # Корректный пароль
    
    # Проверить шибку для некорректного пароля. Минимальный пароль — шесть символов.
    negative_password = '123qw' # Некорректный пароль - 5 символов

    def email(): # Генерация почты для регистрации в формате: имя_фамилия_номер когорты_любые 3 цифры@домен
        return f'Dmitriy_Zaharychev_28_{random.randint(100, 999)}@mail.ru' 
    
    def password(): # Генерация пароля, минимальный пароль — шесть символов
        return f'{random.randint(100000, 99999999)}' 


