import random

string = '0000000000000000000000000'
l = list(string)
for i in range(len(l)):
    idx = random.randint(1, len(string) - 1)
    if l[idx] == '0':
        l[idx] = '1'
    else:
        continue

print("".join(l))