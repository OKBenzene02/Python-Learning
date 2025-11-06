# def fizz_buzz(number: int) ->str:
#     """
#     Fizz buzz game can be played by 2 or more players.
#     :param number:to check number
#     :return:if the number is divisible by 3 we call fizz.
#         if the number is divisible by 5 we call buzz.
#         if the number is divisible by both 3 and 5 we call fizz buzz.
#     """
#     if number % (3 * 5) == 0:
#         return "fizz buzz"
#     elif number % 3 == 0:
#         return "fizz"
#     elif number % 5 == 0:
#         return "buzz"
#     else:
#         return str(number)
#
# input("""Fizz Buzz
# Press ENTER to start.""")
# print()
# next_number = 0
# while next_number < 99:
#     next_number += 1
#     print(fizz_buzz(next_number))
#     next_number += 1
#     correct_number = fizz_buzz(next_number)
#     players_numbers = input("Your go: ")
#     if players_numbers != correct_number:
#         print("You lose, the correct answer was {}.".format(correct_number))
#         break
# else:
#     print("well done you reached {}.".format(next_number))

# def fizz_buzz(number: int) -> str:
#     if number % 15 == 0:
#         return "Fizz Buzz".casefold()
#     elif number % 3 == 0:
#         return "Fizz".casefold()
#     elif number % 5 == 0:
#         return "Buzz".casefold()
#     else:
#         return str(number)
#
# input("""FIZZ BUZZ
# Press ENTER to start.""")
# print()
#
# next_number = 0
# while next_number < 99:
#     next_number += 1
#     print(fizz_buzz(next_number))
#     next_number += 1
#     correct_number = fizz_buzz(next_number)
#     players_number = input("Your Turn: ")
#     if players_number != correct_number:
#         print("You lose the correct answer was {}".format(correct_number))
#         break

# num = int(input("Enter a number: "))

for num in range(100):
    if num % 15 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)


