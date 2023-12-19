# # 1. Користувач вводить із клавіатури номер дня тижня (1-7).
# # Необхідно вивести на екран назви дня тижня.
# # Наприклад, якщо 1, на екрані напис понеділок, 2 — вівторок тощо.
#
# try:
#     day = int(input("Please, enter a number week: "))
#     match day:
#         case 1:
#             print("It`s Monday!")
#         case 2:
#             print("It`s Tuesday!")
#         case 3:
#             print("It`s Wednesday!")
#         case 4:
#             print("It`s Thursday!!")
#         case 5:
#             print("It`s Friday!")
#         case 6:
#             print("It`s Saturday!")
#         case 7:
#             print("It`s Sunday!")
#         case _:
#             print("Invalid input day of week!")
# except Exception as error:
#     print(f"ExceptionError: {error}")


# 2. Користувач вводить два числа.
# Визначити, чи рівні ці числа, і, якщо ні, вивести їх на екран у порядку зростання.

try:
    while True:
        try:
            number1 = int(input("Please, input a number 1: "))
            number2 = int(input("Please, input a number 2: "))
            if number1 == number2:
                print("Yes, these numbers are equal!")
            elif number1 < number2:
                print(f"{number1},\t{number2}")
                break
            else:
                print(f"{number2},\t{number1}")
                break
        except ValueError as error:
            print(f"ValueError occurred:{error}")
            print("Please retry the operation!")
except Exception as error:
    print(f"ExceptionError: {error}")