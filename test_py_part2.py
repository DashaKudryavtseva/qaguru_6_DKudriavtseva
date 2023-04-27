from datetime import time

def test_dark_theme():
    """
    Протестируйте правильность переключения темной темы на сайте
    """
    current_time = time(hour=23)
    # TODO переключите темную тему в зависимости от времени суток (с 22 до 6 часов утра - ночь)

    is_dark_theme = None
    if current_time >=time(22) or current_time <= time(6):
        is_dark_theme = True
    else:
        is_dark_theme = False
    assert is_dark_theme is True
    current_time = time(hour=16)
    dark_theme_enabled = True
    # TODO переключите темную тему в зависимости от времени суток,
    #  но учтите что темная тема может быть включена вручную
    is_dark_theme = None
    if dark_theme_enabled == True or current_time >= time(22) or current_time <= time(6):
        is_dark_theme = True
    else:
        is_dark_theme = False
    assert is_dark_theme is True

def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]
    suiable_user = None
    # TODO найдите пользователя с именем "Olga"
    for user in users:
        if user.get("name") == "Olga":
            suiable_user = user
    assert suiable_user == {"name": "Olga", "age": 45}
    # TODO найдите всех пользователей младше 20 лет
    suiable_users = []
    for user in users:
        if user.get("age") < 20:
            suiable_users.append(user)
    assert suiable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]

# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser [Chrome]"

def text_editor_func(func):
    print(func.__name__)
    print(func.__dict__)

def test_readable_function():
    text_editor_func(some_func)
    # open_browser(browser_name="Chrome")
    # go_to_companyname_homepage(page_url="https://companyname.com")
    # find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")


def some_func():
    some_func().a = 10
    print("Hello ")
def open_browser(browser_name):
    actual_result = None
    assert actual_result == "Open Browser [Chrome]"

def go_to_companyname_homepage(page_url):
    actual_result = None
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"

def find_registration_button_on_login_page(page_url, button_text):
    actual_result = None
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"