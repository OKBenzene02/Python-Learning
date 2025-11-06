# for i in range(0, 10):
#     print(i)
# for i in range(10):
#     print(i)

# Using steps in Ranges:
for i in range(10, -1, -2):
    print(i)

#Times Table:
    # used for huge data calculations

for j in range(1, 13):
    for i in range(1, 13):
        print("{} times {} is {}".format(j, i, i*j))
    print("-"*20)
# challenge solution

for i in range(0, 100, 7):
    print(i)
    if i > 0 and i % 11 == 0:
        break
