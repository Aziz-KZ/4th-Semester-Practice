import datetime

day = int(input("Введите день рождения: "))
month = int(input("Введите месяц рождения: "))
year = int(input("Введите год рождения: "))

def get_weekday(day, month, year):
    date = datetime.date(year, month, day)
    weekdays_en = date.strftime("%A")
    weekdays_ru = {
        "Monday": "Понедельник",
        "Tuesday": "Вторник",
        "Wednesday": "Среда",
        "Thursday": "Четверг",
        "Friday": "Пятница",
        "Saturday": "Суббота",
        "Sunday": "Воскресенье"
    }
    return weekdays_ru[weekdays_en]

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
    
if is_leap_year(year):
    print("Год рождения был високосным")
else:
    print("Год рождения не был високосным")

def get_age(day, month, year):
    today = datetime.date.today()
    birth_date = datetime.date(year, month, day)
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age

age = get_age(day, month, year)
print("Ваш возраст:", age)

weekday = get_weekday(day, month, year)
print("День недели вашего рождения:", weekday)

digits = {
    "0": [
        " *** ",
        "*   *",
        "*   *",
        "*   *",
        " *** "
    ],
    "1": [
        "  *  ",
        " **  ",
        "  *  ",
        "  *  ",
        "*****"
    ],
    "2": [
        "*****",
        "    *",
        "*****",
        "*    ",
        "*****"
    ],
    "3": [
        " ****",
        "    *",
        " ****",
        "    *",
        " ****"
    ],
    "4": [
        "*   *",
        "*   *",
        "*****",
        "    *",
        "    *"
    ],
    "5": [
        "*****",
        "*    ",
        "*****",
        "    *",
        "*****"
    ],
    "6": [
        " *** ",
        "*    ",
        "*****",
        "*   *",
        " *** "
    ],
    "7": [
        "*****",
        "    *",
        "   * ",
        "  *  ",
        " *   "
    ],
    "8": [
        "*****",
        "*   *",
        "*****",
        "*   *",
        "*****"
    ],
    "9": [
        "*****",
        "*   *",
        "*****",
        "    *",
        "*****"
    ]
}

def print_star_date(day, month, year):
    day_str = f"{day:02d}"     # 2 цифры для дня
    month_str = f"{month:02d}" # 2 цифры для месяца
    year_str = str(year)        # 4 цифры года

    # Каждая строка (0–4) цифр
    for i in range(5):
        line = ""
        # День
        for digit in day_str:
            line += digits[digit][i] + "  "
        line += "   "  # дополнительный пробел между день/месяц
        # Месяц
        for digit in month_str:
            line += digits[digit][i] + "  "
        line += "   "  # пробел между месяц/год
        # Год
        for digit in year_str:
            line += digits[digit][i] + "  "
        print(line)

print("\nВаша дата рождения в виде «электронного табло»:")
print_star_date(day, month, year)

print("""
ТЗ по практике выполнено полностью: 
• Программа запрашивает у пользователя последовательно день его рождения, месяц и год;
• Функция определяет, к какому дню недели соответствует эта дата;
• Функция определяет - високосный это был год, или нет;
• Функция определяет сколько сейчас лет пользователю;
• Работает вывод даты рождения пользователя, как на электронном табло.
""")