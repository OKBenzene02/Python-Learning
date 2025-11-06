from math import isqrt

# l = []
# while True:
#     a = int(input())
#     if a == 42:
#         break
#     l.append(a)
#
# for i in l:
#     print(i)

l = []
t = int(input())
for i in range(t):
    m, n = map(int, input().split())
    prime = [True for q in range(n+1)]
    p = 2
    while (p * p <= n):

        if (prime[p] == True):

            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1

    for p in range(m, n+1):
        if p == 1:
            continue
        elif prime[p]:
            l.append(p)
    l.append(" ")

for i in range(len(l)):
    print(l[i])

# def sieveAlgo(n: int):
#     if n <= 2:
#         return []
#     isPrime = [True for i in range(n)]
#     isPrime[0] = False
#     isPrime[1] = False
#
#     for i in range(2, isqrt(n) + 1):
#         if isPrime[i]:
#             for x in range(i * i, n, i):
#                 isPrime[x] = False
#
#     return [i for i in range(n) if isPrime[i]]
#
# a = 100
# print(sieveAlgo(a))

# Python program to print all
# primes smaller than or equal to
# n using Sieve of Eratosthenes


