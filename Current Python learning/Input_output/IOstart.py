# file_location = open("C:/Python/sample.txt")
#
# for line in file_location:
#     print(line)
#
# file_location.close()

# file_location = open("C:\\Python\\sample.txt", "r")
#
# for line in file_location:
#     if "jabberwock" in line.lower():
#         print(line, end='')
#
# file_location.close()

# with open("C:\\Python\\sample.txt", "r") as file_loaction:
#     line = file_loaction.readline()
#     while line:
#         print(line, end='')
#         line = file_loaction.readline()

# with open("C:\\Python\\sample.txt", "r") as file_loaction:
#     lines = file_loaction.readlines()
# print(lines)
#
# for line in lines[::-1]:
#     print(line, end='')


# with open("C:\\Python\\sample.txt", "r") as file_loaction:
#     lines = file_loaction.read()
# # print(lines)
#
# for line in lines[::-1]:
#     print(line, end='')

reading = open("something.txt", 'r')
# ok = reading.read()
# print(ok)
# reading.close()
for i in reading:
    print(i, end="")

reading.close()