# computer_parts = ["computer", "mouse", "keyboard", "cpu", "desktop", "laptop"]
# print(computer_parts)
# computer_parts[2] = "rack"
# print(computer_parts)
# del computer_parts[3]
# print(computer_parts)

# data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 188, 191, 350, 360]
#
# min_valid = 100
# max_valid = 200
#
# stop = 0
# for index, value in enumerate(data):
#     if value >= min_valid:
#         stop = index
#         break
# print(stop)
# del data[:stop]
# print(data)
#
# start = 0
# for index in range(len(data) - 1, -1, -1):
#     if data[index] <= max_valid:
#         start = index + 1
#         break
# print(start)
# del data[start:]
# print(data)

given = [1, 3, 10, 12, 14, 17, 4, 20, 50, 23]
min_value = 10
max_value = 20
given.sort()
print(given)

stop = 0
for index, value in enumerate(given):
    if value >= min_value:
        stop = index
        break
print(given)
print(stop)
del given[:stop]
print(given)

start = 0
for index in range(len(given) - 1, -1, -1):
    if given[index] <= max_value:
        start = index
        break
print(start)
del given[start:]


# computer_parts = ["computer", "mouse", "keyboard", "cpu", "desktop", "laptop"]
#
# for parts in computer_parts:
#     print(parts)
#
# print(computer_parts[1])
