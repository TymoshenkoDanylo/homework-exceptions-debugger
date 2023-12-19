# 1. Користувач вводить із клавіатури номер дня тижня (1-7).
# Необхідно вивести на екран назви дня тижня.
# Наприклад, якщо 1, на екрані напис понеділок, 2 — вівторок тощо.

try:
    day = int(input("Please, enter a number week: "))
    match day:
        case 1:
            print("It`s Monday!")
        case 2:
            print("It`s Tuesday!")
        case 3:
            print("It`s Wednesday!")
        case 4:
            print("It`s Thursday!!")
        case 5:
            print("It`s Friday!")
        case 6:
            print("It`s Saturday!")
        case 7:
            print("It`s Sunday!")
        case _:
            print("Invalid input day of week!")
except Exception as error:
    print(f"ExceptionError: {error}")