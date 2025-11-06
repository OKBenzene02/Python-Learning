with open("C:\\Python\\sample.txt", 'a') as file_location:
    for i in range(2, 13):
        for j in range(1, 13):
            print("{1:>2} times {0} is {2}".format(i, j, i * j), file=file_location)
        print("=" * 80, file=file_location)

