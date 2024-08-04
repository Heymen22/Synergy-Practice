from datetime import datetime

art_numbers = {
    "0": [" *** ",
          "*   *",
          "*   *",
          "*   *",
          " *** "],
    "1": ["  *",
          "* *",
          "  *",
          "  *",
          "  *"],
    "2": ["*****",
          "    *",
          "  ** ",
          "*    ",
          "*****"],
    "3": ["*****",
          "   * ",
          " *** ",
          "    *",
          "**** "],
    "4": ["*  *",
          "*  *",
          "****",
          "   *",
          "   *"],
    "5": ["*****",
          "*    ",
          "**** ",
          "    *",
          "**** "],
    "6": [" *** ",
          "*    ",
          "**** ",
          "*   *",
          " *** "],
    "7": ["*****",
          "    *",
          "  *  ",
          "  *  ",
          "  *  "],
    "8": [" *** ",
          "*   *",
          " *** ",
          "*   *",
          " *** "],
    "9": [" *** ",
          "*   *",
          " ****",
          "    *",
          " *** "],
    ".": ["  ",
          "  ",
          "  ",
          "**",
          "**"],
}


def get_day_of_week(date):
    """Returns the name of the day of the week corresponding to the date"""
    return date.strftime("%A")  # Возвращаем день недели


def is_a_leap_year(year):
    """Determines whether the year was a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def get_age(date_of_birth):
    """Determines how old the user is now."""
    today = datetime.now()
    age = today.year - date_of_birth.year - (
            (today.month, today.day) < (date_of_birth.month, date_of_birth.day))
    return age


def date_format(date_of_birth):
    """Formats the date in dd mm yyyy format with asterisks."""
    unformatted_date = date_of_birth.strftime("%d.%m.%Y")

    result = ""
    for row in range(0,5):
        for char in unformatted_date:
            result += art_numbers[char][row]
            result += "  "
        else:
            result += "\n"
    return result


if __name__ == "__main__":
    # Requesting a date from the user
    day = int(input("Введите день рождения (DD): "))
    month = int(input("Введите месяц рождения (MM): "))
    year = int(input("Введите год рождения (YYYY): "))

    # 1. Creating a datetime Object
    date_of_birth = datetime(year=year, month=month, day=day)

    print(f"День недели: {get_day_of_week(date_of_birth)}")

    # 2. Checking for leap year
    if is_a_leap_year(year):
        print(f"{year} - это високосный год.")
    else:
        print(f"{year} - это не високосный год.")

    # 3. Determining the user's age
    print(f"Возраст пользователя: {get_age(date_of_birth)} лет.")

    # 4. Format the date with asterisks
    formatted_date = date_format(date_of_birth)
    print(f"Дата рождения с звёздочками:\n{formatted_date}")
