pangram = "The quick brown fox jumps over lazy dog"
letters = sorted(pangram)
print(letters)


numbers = [1.1, 1.2, 1.3, 1.03, 1.009]
numbers_sorted = sorted(numbers)
print(numbers_sorted)

numbers.sort()
print(numbers)

list_sort = ['c', 'o', 'f', 'h']
list_sort.sort()
print(list_sort)

sorted_ = sorted(list_sort)
print(sorted_)

names = ['Gerry',
         'Graham',
         'liyakhat',
         'john'
        ]
names.sort(key=str.casefold)
print(names)