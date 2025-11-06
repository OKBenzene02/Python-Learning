def bubble_sort(a):
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


high = int(input("Enter Range of elements to be entered: "))
array = []
for i in range(high):
    b = int(input(f"Enter element {i + 1}: "))
    array.append(b)
bubble_sort(array)
print(array)

