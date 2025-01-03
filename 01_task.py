# Завдання 1

# Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.

# Вимоги до завдання:

# Функція приймає один параметр: date — рядок, що представляє дату у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09').
# Функція повертає ціле число, яке вказує на кількість днів від заданої дати до поточної. Якщо задана дата пізніша за поточну, результат має бути від'ємним.
# У розрахунках необхідно враховувати лише дні, ігноруючи час (години, хвилини, секунди).
# Для роботи з датами слід використовувати модуль datetime Python.


# Рекомендації для виконання:

# Імпортуйте модуль datetime.
# Перетворіть рядок дати у форматі 'РРРР-ММ-ДД' у об'єкт datetime.
# Отримайте поточну дату, використовуючи datetime.today().
# Розрахуйте різницю між поточною датою та заданою датою.
# Поверніть різницю у днях як ціле число.


# Критерії оцінювання:

# Коректність роботи функції: функція повинна точно обраховувати кількість днів між датами.
# Обробка винятків: функція має впоратися з неправильним форматом вхідних даних.
# Читабельність коду: код повинен бути чистим і добре документованим.


# Приклад:

# Якщо сьогодні 5 травня 2021 року, виклик get_days_from_today("2021-10-09") повинен повернути −157, оскільки 9 жовтня 2021 року є на 157 днів пізніше від 5 травня 2021 року.


import datetime
past="2022-01-01"
future = "2028-01-01"
the_present=datetime.datetime.today().strftime("%Y-%m-%d")
invalid_value="01"


def get_days_from_today(date):
    try:
        today=datetime.datetime.today()
        date=datetime.datetime.strptime(date, "%Y-%m-%d")
        result = (today - date).days
        return result
    except:
        return "Введено не вірний формат дати. Введіть дату у форматі 'РРРР-ММ-ДД'."
 
print("Різниця в днях: ",get_days_from_today(past))
print("Різниця в днях: ",get_days_from_today(future))
print("Різниця в днях: ",get_days_from_today(the_present))
print("Різниця в днях: ",get_days_from_today(invalid_value))

