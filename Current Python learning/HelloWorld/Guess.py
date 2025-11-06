import random

highest = 10
answer = random.randint(1, highest)
print(answer)     # TODO:Remove after testing

print("please enter a number between 1 to {}:".format(highest))
guess = 0
while guess != answer:
    guess = int(input())

    if guess == answer:
        print("well done you got it correct.")
        break
    else:
        if guess < answer:
            print("please guess higher")
        else:
            print("please guess lower")
        # guess = int(input())
        # if guess == answer:
        #     print("well done you got it correct.")
        # else:
        #     print("sorry, you got it wrong")

# import random
#
# highest = 21
# answer = random.randint(11, highest)
# print(answer)
# print("please enter a number between 11 to {}.".format(highest))
#
# guess = 0
#
# while guess != answer:
#     guess = int(input())
#     if guess == answer:
#         print("Well done you guessed it correctly")
#         break
#     else:
#         if guess > answer:
#             print("please guess lower")
#         else:
#             print("please guess higher")
























