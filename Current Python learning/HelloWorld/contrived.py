numbers = [1, 2, 45, 15]

for number in numbers:
    if number % 8 == 0:
        print("the numbers are not acceptable")
        break
else:
    print("the numbers are acceptable")