# # =================================================================================
# Geek marks linear Search
# def geeks_marks(t):
#     res = []
#     while t:
#         n, x = map(int, input().split())
#         marks = list(map(int, input().split()))
#         count = 0
#         for mark in marks:
#             if mark > int(x):
#                 count += 1
#
#         res.append(count) if count else res.append(0)
#         t -= 1
#
#     for num in res:
#         print(num)
#
# t = int(input())
# geeks_marks(t)
import math


# # =================================================================================
# Geek and his marks, Binary Search
# def binary_search(t):
#     res = []
#     while t != 0:
#         n = int(input())
#         n = sorted([int(num) for num in input().split(" ")])
#         q = int(input())
#         temp = []
#         for i in range(q):
#             some_num = int(input())
#             temp.append(some_num)
#         for num in range(1, q + 1):
#             low = 0
#             high = len(n) - 1
#             sum = 0
#             while low <= high:
#                 mid = (low + high) // 2
#                 if n[mid] > num:
#                     sum += n[mid]
#                 low = mid + 1
#             res.append(sum)
#
#         t -= 1
#
#         for i in range(len(res)):
#             print(res[i])
#
#
# t = int(input())
# binary_search(t)
# # =================================================================================
# # Sieve of eratosthenes

# import math
# def sieve_eratosthenes(n):
#     primes = [True for i in range(n + 1)]
#     p = 2
#     while p * p <= n:
#         if primes[p]:
#             for i in range(p * p, n + 1, p):
#                 primes[i] = False
#         p += 1
#
#     for i in range(2, n + 1):
#         if primes[i]:
#             print(i, end=' ')
#
# sieve_eratosthenes(10)

# # Segmented Sieve's
# prime = []
# def simpleSieve(n):
#     primes = [True for i in range(n + 1)]
#     p = 2
#     while p * p <= n:
#         if primes[p]:
#             for i in range(p * p, n + 1, p):
#                 primes[i] = False
#         p += 1
#
#     for i in range(2, n):
#         if primes[i]:
#             prime.append(i)
#             print(i, end=" ")
#
#
# def segmentedSieve(n):
#     # Compute all the primes smaller than or equal to the
#     # square root of n using the simple sieve
#
#     limit = int(math.floor(math.sqrt(n)) + 1)
#     simpleSieve(limit)
#
#     low = limit
#     high = limit * 2
#
#     while low < n:
#         if high >= n:
#             high = n
#
#         marking = [True for i in range(limit + 1)]
#
#         for i in range(len(prime)):
#             lowLimit = int(math.floor(low / prime[i]) * prime[i])
#             if lowLimit < low:
#                 lowLimit += prime[i]
#
#             for j in range(lowLimit, high, prime[i]):
#                 marking[j - low] = False
#
#         for i in range(low, high):
#             if marking[i - low]:
#                 print(i, end=' ')
#
#         low = low + limit
#         high = high + limit
#
# segmentedSieve(100)

# simpleSieve(20)
# print(prime)

# ===============================================================================
# Product of primes

# def sieve(n):
#     prime = [True] * (n + 1)
#     p = 2
#     while p * p <= n:
#         if prime[p]:
#             for i in range(p * p, n + 1, p):
#                 prime[i] = False
#         p += 1
#
#     return prime
# def productPrimes(l, r):
#     d = 1
#     for i in range(l, r + 1):
#         if sieve(i)[i]:
#             d = d * i
#             d = d % (10 ** 9 + 7)
#     return d % (10 ** 9 + 7)
#
# print(productPrimes(1, 20))

# ===============================================================================
# Add Binary
# def addBinary(a, b) -> str:
#     max_len = max(len(a), len(b))
#     a = a.zfill(max_len)
#     b = b.zfill(max_len)
#     result = ''
#     carry = 0
#     for i in range(max_len - 1, -1, -1):
#         r = carry
#         r += 1 if a[i] == '1' else 0
#         r += 1 if b[i] == '1' else 0
#         result = ('1' if r % 2 == 1 else '0') + result
#         carry = 0 if r < 2 else 1
#
#     if carry != 0:
#         result = "1" + result
#
#     return result.zfill(max_len)
#
#
# print(addBinary('11','1'))

# def addBinary(a, b):
#     length = max(len(a), len(b))
#     a, b = a.zfill(length), b.zfill(length)
#     int_a, int_b = 0, 0
#     for i in range(len(a) - 1, -1, -1):
#         if a[i] == '0':
#             int_a += (pow(2, len(a) - 1 - i) * 0)
#         else:
#             int_a += pow(2, len(a) - 1 - i)
#
#     for i in range(len(b) - 1, -1, -1):
#         if b[i] == '0':
#             int_b += (pow(2, len(b) - 1 - i) * 0)
#         else:
#             int_b += pow(2, len(b) - 1 - i)
#
#     return str(bin(int_a + int_b))[2:].zfill(length)
#
# print(addBinary('1010', '1011'))

# ==============================================================================
# Is Subsequence

# def isSub(s, t):
#     s = list(s)
#     t = list(t)
#     char = len(t) - len(s)
#     for _ in range(char):
#         s.append("")
#
#     l, r = 0, 0
#     while (l < len(s)) and (r < len(t)):
#         if s[l] == t[r]:
#             s[l] = ""
#             l += 1
#             r = l
#         else:
#             r += 1
#     if s.count("") == len(s):
#         return True
#     else:
#         return False
#
# print(isSub('abc', 'ahbgdc'))

# =========================================================================
# Isomorphic strings

# def isomorphic(s, t):
#     mapST, mapTS = {}, {}
#
#     for c1, c2, in zip(s, t):
#         if (c1 in mapST and mapST[c1] != c2) or (c2 in mapTS and mapTS[c2] != c1):
#             return False
#         mapST[c1] = c2
#         mapTS[c2] = c1
#     return True
#
# print(isomorphic('egg', 'add'))
# ==========================================================================
# Finding the divisors

# def divisors(n: int):
#     i = 1
#     while i <= math.floor(math.sqrt(n)):
#         if n % i == 0:
#             if n/i == i:
#                 print(i, end=" ")
#             else:
#                 print(i, int(n/i), end=" ")
#         i += 1
#
# divisors(3)

# ==========================================================================
# Count the total number of divisors

# def count_divisors(n: int) -> int:
#     i = 1
#     l = []
#     while i <= math.sqrt(n):
#         if n % i == 0:
#             if n / i == i:
#                 l.append(i)
#             else:
#                 l.append(i)
#                 l.append(int(n/i))
#         i += 1
#
#     return len(l)
#
# print(count_divisors(10))
# ========================================================================
# kth smallest factor

# def smallestFactor(n: int, k: int):
#     t = 0
#     for i in range(1, n//2+1):
#         if n % i == 0:
#             t += 1
#             if t == k:
#                 return i
#     t += 1
#     if t == k:
#         return n
#     else:
#         return -1
#
# print(smallestFactor(10, 3))

# ========================================================================
# Array form of integer

# def array_form(n: [int], k: int):
#     str_l = [str(i) for i in n]
#     toInt = int("".join(str_l))
#     added = toInt + k
#     str_to_int = [int(i) for i in list(str(added))]
#     return str_to_int
#
# print(array_form([1, 2, 3], 334))
# ========================================================================
# All prime factors of n

# def prime_factors(n: int):
#     factors = []
#
#     while n % 2 == 0:
#         factors.append(2)
#         n = n // 2
#
#     for i in range(3, int(math.sqrt(n)) + 1, 2):
#         while n % i == 0:
#             factors.append(i)
#             n = n // i
#
#     if n > 2:
#         factors.append(n)
#
#     return factors
#
# print(prime_factors(378))

# ==========================================================================
# Least Prime Factor

# def leastPrimeFactor(n):
#     l = [0] * (n + 1)
#     l[1] = 1
#     for i in range(2, n + 1):
#         if l[i] == 0:
#             l[i] = i
#             for j in range(i * i, n + 1, i):
#                 if l[j] == 0:
#                     l[j] = i
#
#     return l[1:]
#
#
# print(leastPrimeFactor(12))

# ==========================================================================
# Largest Prime Number
# def largestPrime(n):
#     l = []
#     if n == 0:
#         return None
#     while n % 2 == 0:
#         l.append(2)
#         n = n / 2
#
#     for i in range(3, int(math.sqrt(n)) + 1, 2):
#         while n % i == 0:
#             l.append(i)
#             n = n / i
#
#     if n > 2:
#         l.append(n)
#
#     return int(max(l))
#
# print(largestPrime(6))

# ==========================================================================
# Prime Factorization using sieve O(log(n)) for multiple queries

# max_n = 100001
# spf = [0] * (max_n + 1)
#
# def least_prime():
#     spf[1] = 1
#     for i in range(2, max_n):
#         spf[i] = i
#
#     for i in range(4, max_n, 2):
#         spf[i] = 2
#
#     for i in range(3, math.ceil(math.sqrt(max_n))):
#         if spf[i] == i:
#             for j in range(i * i, max_n, i):
#                 if spf[j] == j:
#                     spf[j] = i
#
#
# def primeFactor(n):
#     res = set()
#     while n != 1:
#         res.add(spf[n])
#         n = n // spf[n]
#
#     return res
#
# least_prime()
# x = 100
# print(primeFactor(x))

# ==========================================================================
# Sum of all factors with O(N) and O(sqrt(N))
# def sum_factors(n):
#     sum = 0
#     for i in range(2, n + 1):
#         if n % i == 0:
#             sum += i
#
#     return 1 + sum
#
# print(sum_factors(378))

# def sumFactor(n):
#     if n == 1:
#         return 1
#
#     sum = 0
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             if (n / i) == i:
#                 sum += (n/i)
#             else:
#                 sum += i + (n/i)
#
#     return 1 + n + int(sum)
#
# print(sumFactor(15))

# By using the formula
# def factor_sum(n):
#     sum = 1
#     if n == 1:
#         return 1
#
#     for i in range(2, int(math.sqrt(n)) + 1):
#         curr_sum = 1
#         curr_term = 1
#         while n % i == 0:
#             n = n / i
#             curr_term *= i
#             curr_sum += curr_term
#
#         sum *= curr_sum
#
#     if n > 2 :
#         sum = sum * (1 + n)
#
#     return sum
#
# print(factor_sum(30))

# ======================================================================
# GCD or HCF of two numbers using the Euclidean subtraction algorithm
# Has Time complexity of O(min(a, b))

# Iterative method
# def gcd(a: int, b: int) -> int:
#     min_num = min(a, b)
#     while min_num:
#         if a % min_num == 0 and b % min_num == 0:
#             break
#         min_num -= 1
#
#     return min_num
#
# print(gcd(36, 60))

# Recursive method
# def gcd(a: int, b: int) -> int:
#     if a == 0:
#         return b
#     if b == 0:
#         return a
#
#     if a == b:
#         return a
#
#     if a > b:
#         return gcd(a - b, b)
#
#     return gcd(a, b - a)
#
# print(gcd(98, 56))

# Gcd using the extended euclidean algorithm
# Time complexity O(log(min(a, b)))
# def extented_gcd(a, b):
#     if a == 0:
#         return b, 0, 1
#
#     g, x1, y1 = extented_gcd(b % a, a)
#     x = y1 - (b // a) * x1
#     y = x1
#
#     return g, x, y
#
#
# print(extented_gcd(98, 56))
# ===========================================================================
# Linear Diophantine equations

# def gcd(a, b):
#     if b == 0:
#         return a
#
#     return gcd(b, a % b)
# def linear(a, b, c):
#     return 1 if (c % gcd(a, b) == 0) else 0
#
# print(linear(3, 6, 9))

# =============================================================================
# Least common multiple using GCD by O(log(min(a, b)))

# def gcd(a, b):
#     if a == 0:
#         return b, 0, 1
#
#     g, x1, y1 = gcd(b % a, a)
#     x = y1 - (b // a) * x1
#     y = x1
#
#     return g, x, y
#
# def lcm(a, b):
#     return (a * b) // (gcd(a, b)[0])
#
# print(lcm(15, 25))

# ==============================================================================
# Maximum and minimum in an array using tournament method with O(n)
# def findSum(A,N):
#     max_num = A[0]
#     min_num = A[0]
#     if N == 1:
#         return A[0] + A[0]
#
#     elif N == 2:
#         if A[0] > A[1]:
#             max_num = A[0]
#             min_num = A[1]
#         else:
#             max_num = A[1]
#             min_num = A[0]
#
#         return max_num + min_num
#
#     for i in range(N):
#         if A[i] > max_num:
#             max_num = A[i]
#         elif A[i] < min_num:
#             min_num = A[i]
#
#     return max_num + min_num
#
# print(findSum([-2, 1, -4, 5, 3], 5))
# ================================================================================
# Best time to buy stocks and sell stocks

# def buy_sell(l: [list]) -> int:
#     left, right = 0, 1
#     currProfit = 0
#     while right < len(l):
#         if l[left] < l[right]:
#             profit = l[right] - l[left]
#             currProfit = max(profit, currProfit)
#         else:
#             left = right
#         right += 1
#
#     return currProfit
#
# print(buy_sell([7,1,5,3,6,4]))

# ==========================================
# Counting frequencies of the elements

# def count(arr):
#     mp = {}
#     for i in range(len(arr)):
#         if arr[i] not in mp.keys():
#             mp[arr[i]] = 1
#         else:
#             mp[arr[i]] += 1
#
#     return mp
#
# print(count([10, 20, 20, 10, 10, 20, 5, 20]))

# Contains duplicates
# def isDuplicate(arr):
#     mp = set()
#     for i in arr:
#         if i not in mp:
#             mp.add(i)
#         else:
#             return True
#     return False
#
# print(isDuplicate([10, 20]))

# =======================================================================
# Two Sum
# def two_sum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i):
#             if nums[i] + nums[j] == target:
#                 return i, j
#     return -1
#
# print(two_sum([3, 3], 6))

# Two Sum using Hash Table

# def twoSum(nums, target):
#     mp = {}
#     for i, num in enumerate(nums):
#         right = target - num
#         if right in mp:
#             return [mp[right], i]
#         mp[num] = i
#
# print(twoSum([1,2,3,4,5,6,7,8,9,10], 15))
# ======================================================================
# Reverse integer
# def int_reverse(x):
#     if x >= 0:
#         l = list(str(x))[::-1]
#         if l[0] == "0":
#             return int("".join(l[1::]))
#         else:
#             return int("".join(l))
#
#     l = list(str(x))
#     sign = l[0]
#     l_rev = l[1::]
#     temp = l_rev[::-1]
#     if temp[0] == "0":
#         return int(sign + "".join(temp[1::]))
#     else:
#         return int(sign + "".join(temp))
#
# print(int_reverse(-123))

# def reverse(x):
#     min_num = -2147483648
#     max_num = 2147483647
#
#     res = 0
#     while x:
#         digit = int(math.fmod(x, 10))
#         x = int(x / 10)
#
#         if (res > max_num // 10) or (res == max_num // 10 and digit >= max_num % 10):
#             return 0
#         if (res < min_num // 10) or (res == min_num // 10 and digit <= min_num % 10):
#             return 0
#         res = (res * 10) + digit
#     return res
#
# print(reverse(-123))
# print(list(str(-123))[1::])
# ======================================================================
# Longest palindrome

# def palindrome(s: str):
#     mp = {}
#
#     for char in s:
#         mp[char] = mp.get(char, 0) + 1
#+-
#     res, odd = 0, False
#
#     for key, count in mp.items():
#         if count % 2 == 0:
#             res += count
#         else:
#             odd = True
#             res = res + count - 1
#
#     if odd:
#         res += 1
#     return res
#
# print(palindrome('abccccdd'))

# ======================================================================
# Number compression using Hashmap or unordered list

# def reduced_form(l):
#     temp = l
#     temp = sorted(temp)
#
#     mp = dict()
#     for i in range(len(l)):
#         mp[temp[i]] = i
#
#     for i in range(len(l)):
#         l[i] = mp[l[i]]
#
#     return l
#
# print(reduced_form([10, 40, 20]))
# ======================================================================
# Kadane's Algorithm

# def maximumSumSubArray(nums):
#     currMax, res = 0, -99999999999999
#
#     for num in nums:
#         currMax += num
#         if currMax > res:
#             res = currMax
#         if currMax < 0:
#             currMax = 0
#
#     return res
#
# print(maximumSumSubArray([-7,-8 ,-16, -4, -8, -5, -7, -11, -10, -12, -4, -6, -4, -16, -10]))

# Min subarray using Kadane's algorithm
# def min_subarray(l: list):
#     min_so_far = 999999999999999
#     min_ending_here = 0
#     min_arr = []
#
#     for i in range(len(l)):
#         min_ending_here = min_ending_here + l[i]
#         if min_so_far > min_ending_here:
#             min_so_far = min_ending_here
#         if min_ending_here > 0:
#             min_ending_here = 0
#
#     return min_so_far
#
#
# print(min_subarray([5, 9, -3, -2, 9, 4]))

# ======================================================================
# String compression

# def compress(l: list) -> :
#     mp = {}
#     s = ""
#     for char in l:
#         if char not in mp:
#             mp[char] = 1
#         else:
#             mp[char] += 1
#
#     for key, val in mp.items():
#         if mp[key] == 1:
#             s += key
#         else:
#             s += key + str(val)
#
#     return len(s) if s else 0
#
# print(compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))

# def compress(chars):
#     i, j = 0, 0
#     while j < len(chars):
#         chars[i] = chars[j]
#         count = 1
#         while (j + 1) < len(chars) and chars[j] == chars[j + 1]:
#             j += 1
#             count += 1
#         if count > 1:
#             for c in str(count):
#                 chars[i + 1] = c
#                 i += 1
#         j += 1
#         i += 1
#     return i
#
# print(compress(["b","b","a","a","c","c","c"]))
# ======================================================================
# String matching problem

# def string_match(haystack, needle) -> int:
#
#     l = []
#     n, m = len(haystack), len(needle)
#
#     for i in range(n - m + 1):
#         count = 0
#         for j in range(m):
#             if haystack[i + j] != needle[j]:
#                 break
#             count += 1
#         if count == m:
#             l.append(i)
#
#     return l[0] if l else -1
#
#
# print(string_match('mississippi', 'issip'))

# ======================================================================
# Count the number of sub arrays with fixed bounds

# def count_sub(arr, minK, maxk):
#     res = 0
#     bad_index, left_index, right_index = -1, -1, -1
#
#     for i, num in enumerate(arr):
#         if not minK <= num <= maxk: bad_index = i
#         if num == minK: left_index = i
#         if num == maxk: right_index = i
#         res += max(0, min(left_index, right_index) - bad_index)
#
#     return res
#
# print(count_sub([1,3,5,2,7,5], 1, 5))


# ======================================================================
# import numpy as np
#
# def isBadVersion(n):
#     temp = np.random.randint(1, n)
#     if temp == n:
#         return True
#     return False
#
# def FirstBad(n):
#     low = 1
#     high = n + 1
#     while low < high:
#         mid = low + (high - low) // 2
#         if not isBadVersion(mid):
#             low = mid + 1
#         else:
#             high = mid
#
#     return low
#
# print(FirstBad(5))

# ======================================================================
# Jump game by using greedy search with O(n)

# def jump(n: list) -> bool:
#     goal = len(n) - 1
#
#     for i in range(len(n) - 1, -1 , -1):
#         if i + n[i] >= goal:
#             goal = i
#     return True if goal == 0 else False
#
# print(jump([2,3,1,1,4]))

# Variant of Jump game --> Jump game 2
# Count minimum number of jumps

# def jump(arr):
#     res = 0
#     l, r = 0, 0
#
#     while r < len(arr) + 1:
#         far = 0
#         for i in range(l, r + 1):
#             far = max(far, i + arr[i])
#
#         l = r + 1
#         r = far
#         res += 1
#
#     return res
#
# print(jump([2,3,1,1,4]))

# Variant of Jump game --> Jump game 3
# Reach the end index with some specified starting point

# def jump(arr, start):
#     if start < 0 or start >= len(arr) or arr[start] < 0:
#         return False
#     arr[start] *= -1
#     return arr[start] == 0 or jump(arr, start + arr[start]) or jump(arr, start - arr[start])
#
# print(jump([3,0,2,1,2], 2))

# Variant of Jump game --> Jump game 4
# from collections import defaultdict, deque
# def minJump(arr):
#     n = len(arr)
#     if n == 1:
#         return 0
#
#     indices = defaultdict(list)
#     for i in range(n):
#         indices[arr[i]].append(i)
#
#     storeIndex = deque()
#     visited = [False] * n
#     storeIndex.append(0)
#     visited[0] = True
#     steps = 0
#
#     while storeIndex:
#         size = len(storeIndex)
#         while size > 0:
#             currIndex = storeIndex.popleft()
#             size -= 1
#             if currIndex == n - 1:
#                 return steps
#
#             jumpNextIndices = indices[arr[currIndex]]
#             jumpNextIndices.append(currIndex - 1)
#             jumpNextIndices.append(currIndex + 1)
#             for jumpNextIndex in jumpNextIndices:
#                 if 0 <= jumpNextIndex < n and not visited[jumpNextIndex]:
#                     storeIndex.append(jumpNextIndex)
#                     visited[jumpNextIndex] = True
#             jumpNextIndices.clear()
#         steps += 1
#     return -1
#
# print(minJump([100,-23,-23,404,100,23,23,23,3,404]))

# Approach by using bfs and concept of Jump game 2, 3
# def minJumps(arr):
#     n = len(arr)
#     if n == 1:
#         return 0
#
#     indices = defaultdict(list)
#     for i, adj in enumerate(arr):
#         indices[adj].append(i)
#
#     indexArray = deque()
#     visited = [False] * n
#     indexArray.append(0)
#     visited[0] = True
#     steps = 0
#     while indexArray:
#         size = len(indexArray)
#         while size > 0:
#             currIndex = indexArray.popleft()
#             size -= 1
#             if currIndex == n - 1:
#                 return steps
#             jumpIndexes = indices[arr[currIndex]]
#             jumpIndexes.append(currIndex - 1)
#             jumpIndexes.append(currIndex + 1)
#
#             for jumpIndex in jumpIndexes:
#                 if 0 <= jumpIndex < n and not visited[jumpIndex]:
#                     indexArray.append(jumpIndex)
#                     visited[jumpIndex] = True
#             jumpIndexes.clear()
#         steps += 1
#     return -1
#
# print(minJumps([100,-23,-23,404,100,23,23,23,3,404]))

# =============================================================================================
# Kth missing integer

# def missing(arr, k):
#     temp = [i for i in range(1, 9999)]
#     return list(set(temp).difference(arr))[k-1]
#
# print(missing([2], 1))

# =============================================================================================
# Minimum time to complete trips (Binary Search)
#
# def calc_total_trip(arr, givenTime):
#     total = 0
#     for i in range(len(arr)):
#         total += givenTime // arr[i]
#
#     return total
#
# def trips(arr, totalTrips):
#     low = 1
#     high = totalTrips * min(arr)
#
#     while low < high:
#         mid = (high + low) // 2
#
#         total_val = calc_total_trip(arr, mid)
#
#         if total_val < totalTrips:
#             low = mid + 1
#
#         else:
#             high = mid
#
#     return low
#
# print(trips([1, 2, 3], 5))


# =============================================================================================
# Koko eating banana's (Binary Search)

# def kokoBananas(piles, h):
#     low, high = 1, max(piles)
#     res = high
#
#     while low < high:
#         mid = (low + high) // 2
#         totalTime = 0
#         for num in piles:
#             totalTime += (num // mid) + 1
#         if totalTime <= h:
#             res = min(mid, res)
#             high = mid
#         else:
#             low = mid + 1
#
#     return low
#
# print(kokoBananas([30, 11, 23, 4, 20], 5))

# =============================================================================================
# Ceaser cipher
# import string
# def shifts(word, value):
#     letters = string.ascii_lowercase
#
#     new = ''
#     for i in range(len(word)):
#         if word[i] in letters:
#             index = letters.index(word[i])
#             new = new + letters[(index+value)%26]
#         else:
#             new = new + word[i]
#
#     return new
#
#
# print(shifts('Hello Juliet', 4))

# =============================================================================================
# Unique Paths using Dynamic Programming

# def unique_paths(m, n):
#     end_row = [1] * n
#
#     for i in range(m - 1):
#         prev_row = [1] * n
#         for j in range(n - 2, -1, -1):
#             prev_row[j] = prev_row[j + 1] + end_row[j]
#         end_row = prev_row
#
#     return end_row[0]
#
# print(unique_paths(3, 7))

# =============================================================================================
# Backspace character

# def backspace(s: str, t: str) -> bool:
#     res1, res2 = [], []
#     for char in s:
#         if char != '#':
#             res1 += char
#         elif res1:
#             res1.pop()
#
#     for char in t:
#         if char != '#':
#             res2 += char
#         elif res2:
#             res2.pop()
#
#     return True if "".join(res1) == "".join(res2) else False
#
# print(backspace('a##c', "#a#c"))
# =============================================================================================
# Decode string

# def decode(s: str):
#     stack = []
#     for i in range(len(s)):
#         if s[i] != ']':
#             stack.append(s[i])
#         else:
#             substr = ''
#             while stack[-1] != '[':
#                 substr = stack.pop() + substr
#             stack.pop()
#             integer = ''
#             while stack and stack[-1].isdigit():
#                 integer = stack.pop() + integer
#
#             stack.append(int(integer) * substr)
#
#     return "".join(stack)
#
# print(decode('3[a]2[bc]'))

# =============================================================================================
# Binary search...

# def search(arr, target):
#     low = 0
#     high = len(arr) - 1
#     while low <= high:
#         mid = (high + low) // 2
#         if arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return low
#
# print(search([1,3,5,6], 7))
