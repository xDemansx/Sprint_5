from selenium.webdriver.common.by import By 

class Locators: # Локаторы сайта
    # Главная страница
    main_logo_button = (By.XPATH, '//div[contains(@class,"AppHeader_header__logo")]')  # Кнопка с логотипом на главной странице
    main_account_button = (By.XPATH, '//p[contains(text(),"Личный Кабинет")]/parent::a')  # Кнопка "Личный Кабинет" на главной странице
    main_enter_button = (By.XPATH, '//button[text()="Войти в аккаунт"]')  # Кнопка "Войти в аккаунт" на главной странице
    main_order_button = (By.XPATH, '//button[text()="Оформить заказ"]') # Кнопка "Оформить заказ" на главной странице
    main_constructor_button = (By.XPATH, '//p[contains(text(),"Конструктор")]/parent::a')  # Кнопка "Конструктор" на главной странице

    # Страница входа
    enter_email_input = (By.XPATH, '//label[text()="Email"]/parent::*/input') # Поле ввода email на странице Входа
    enter_password_input = (By.XPATH, '//label[text()="Пароль"]/parent::*/input') # Поле ввода пароля на странице Входа
    enter_login_button = (By.XPATH, '//button[text()="Войти"]') # Кнопка "Войти" на странице Входа
    
    # Страница регистрации
    registration_name_input = (By.XPATH, '//label[text()="Имя"]/parent::*/input') # Поле "Имя" на странице регистрации
    registration_email_input = (By.XPATH, '//label[text()="Email"]/parent::*/input') # Поле "Email" на странице регистрации
    registration_password_input = (By.XPATH, '//label[text()="Пароль"]/parent::*/input') # Поле "Пароль" на странице регистрации
    registration_button = (By.XPATH, '//button[text()="Зарегистрироваться"]') # Кнопка "Зарегистрироваться" на странице Регистрации!!! (не Входа)
    registration_login_button = (By.XPATH, '//a[contains(text(),"Войти")]') # Кнопка "Войти" на странице регистрации и в форме восстановления пароля
    registration_error_password = (By.XPATH, '//*[contains(text(),"Некорректный")]') # Надпись об ошибке "Некорректный пароль"
    registration_error_user = (By.XPATH, '//*[contains(text(),"пользователь уже существует")]') # Надпись об ошибке "Такой пользователь уже существует"
    
    # Страница восстановления пароля
    recover_button = (By.XPATH, '//button[text()="Восстановить"]') # Кнопка "Восстановить" на странице Восстановления пароля

    # Личный кабинет
    lk_exit_button = (By.XPATH, '//button[text()="Выход"]') # Кнопка "Выход" в личном кабинете

    # Конструктор
    constructor_active_press = (By.XPATH, '//div[contains(@class, "tab_tab_type_current")]') # Активная кнопка Конструктора
    constructor_buns = (By.XPATH, '//span[text()="Булки"]/parent::*') # Раздел 'Булки'
    constructor_sauces = (By.XPATH, '//span[text()="Соусы"]/parent::*') # Раздел 'Соусы'
    constructor_stuff = (By.XPATH, '//span[text()="Начинки"]/parent::*') # Раздел 'Начинки'
    constructor_buns_text = 'Булки' # Текст 'Булки'
    constructor_sauces_text = 'Соусы' # Текст 'Соусы'
    constructor_stuff_text = 'Начинки' # Текст 'Начинки'