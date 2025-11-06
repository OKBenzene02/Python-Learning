low = 1
high = 1000

print("please think of a number between {} and {}: ".format(low, high))
input("press ENTER to start")

guesses = 1
while low != high:
    # print("\tGuessing in the range {} and {}.".format(low, high))
    guess = low + (high - low) // 2
    high_low = input("my guess is {}.should i guess higher or lower?"
                     "Enter h or l, c if my guess was correct.".format(guess)).casefold()
    if high_low == "h":
        # guess higher.the low of the range becomes 1 greater than the guess.
        low = guess + 1
    elif high_low == "l":
        #guess lower.the high of the range becoes 1 lower than the guess.
        high = guess - 1
    elif high_low == "c":
        print("I got it in {} guesses.".format(guesses))
        break
    else:
        print("please enter h, l or c")
    guesses += 1
else:
    print("you guessed the number {}".format(low))
    print("i got it in {} guesses".format(guesses))

# LOW = 1
# HIGH = 1000
#
# # print("Please think of a number between the range {} and {}.".format(low, high))
#
# def guess_binary(answer, low, high):
#     guesses = 1
#     while True:
#         # print("Guessing in range {} and {}.".format(low, high))
#         guess = low + (high - low) // 2
#         # high_low = input("my guess is {}.Should i guess higher or lower?"Enter h, l or c if my guess was correct.".format(guess).casefold())"
#         if guess < answer:
#             low = guess + 1
#         elif guess > answer:
#             high = guess - 1
#         elif guess == answer:
#             # print("I got it correct in {} guesses.".format(guesses))
#             # break
#             return guesses
#
#         # else:
#         #     print("please enter h, l or c")
#
#         guesses += 1
#
# correct_count = 0
# max_guesses = 0
# for number in range(LOW, HIGH + 1):
#     number_of_guesses = guess_binary(number, LOW, HIGH)
#     print("{} guessed in {}".format(number, number_of_guesses))
#
#     if number_of_guesses > max_guesses:
#         max_guesses, correct_count = number_of_guesses, 1
#     elif number_of_guesses == max_guesses:
#         correct_count += 1
#
# print("I guessed without being told {} times. Max {} guesses".format(correct_count, max_guesses))










