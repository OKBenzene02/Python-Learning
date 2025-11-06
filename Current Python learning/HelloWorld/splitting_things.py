panagram = "the quick brown fox jumps over a lazy dog"
print(panagram.split())

numbers = "1,234,456,6654,023,3"
print(numbers.split(","))
generated_lists = [
        '1', ' ',
        '2', '3', '4', ' ',
        '4', '5', '6', ' ',
        '6', '6', '5', '4', ' ',
        '0', '2', '3', ' ',
        '3', ' '
]

values = "".join(generated_lists)
print(values)

values_lists = values.split()
print(values_lists)

for index in range(len(values_lists)):
    values_lists[index] = int(values_lists[index])

print(values_lists)

integer_values = []
for value in values_lists:
    integer_values.append(int(value))

print(integer_values)