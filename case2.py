import datetime

# Функция определения дня недели
def day_of_week(birth_date):
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    return days[birth_date.weekday()]

# Функция определения високосного года
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Функция определения возраста пользователя
def calculate_age(birth_date):
    today = datetime.date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

# Функция для вывода даты рождения в формате с звёздочками
def print_birthdate_with_stars(birth_date):
    formatted_date = birth_date.strftime("%d %m %Y").replace("0", "*")
    print(formatted_date)

# Запрос данных у пользователя
day = int(input("Введите день вашего рождения: "))
month = int(input("Введите месяц вашего рождения: "))
year = int(input("Введите год вашего рождения: "))

# Создание объекта даты
birth_date = datetime.date(year, month, day)

# Вывод результата
print("День недели вашего рождения:", day_of_week(birth_date))
print("Високосный ли был год вашего рождения:", is_leap_year(year))
print("Вам сейчас", calculate_age(birth_date), "лет")
print("Дата вашего рождения со звёздочками:")
print_birthdate_with_stars(birth_date)
