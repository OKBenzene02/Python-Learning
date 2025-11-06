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

# low = 1
# high = 500
#
# print("Please guess a number between {} and {}.".format(low, high))
# input("Press enter to START")
#
# guesses = 1
# while True:
#     print("\tGuessing in the range {} and {}.".format(low , high))
#     guess = low + (high-low)//2
#     high_low = input("My guess is {}.Should i guess higher or lower?"
#                      "Enter 'h', 'l' or 'c' if my guess was correct.".format(guess)).casefold()
#     if high_low == "h":
#         low = guess + 1
#     elif high_low == "l":
#         high = guess - 1
#     elif high_low == "c":
#         print("I got it correct in {} guesses.".format(guesses))
#         break
#     else:
#         print("Please enter h, l or c")
#     guesses += 1
#
#













