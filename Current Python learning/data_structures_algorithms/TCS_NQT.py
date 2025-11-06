# Find smallest in the array
import math
# def findSamllest(nums):
#     minNum = nums[0]
#     for num in nums:
#         if num < minNum:
#             minNum = num
#     return minNum
#
# print(findSamllest([2,5,1,3,0]))
# print(findSamllest([8,10,5,7,9]))
# print(findSamllest([-2,-5,-10,10,-100]))
# print(findSamllest([float('inf'), float('-inf'), -100, 300]))

# ================================================================================================================================
# Find the largest in the array

# def findLargest(nums):
#     maxNum = nums[0]
#     for num in nums:
#         if num > maxNum:
#             maxNum = num
#     return maxNum
#
# print(findLargest([2,5,1,3,0]))
# print(findLargest([8,10,5,7,9]))
# print(findLargest([-2,-5,-10,10,-100]))
# print(findLargest([float('inf'), float('-inf'), -100, 300]))

# ================================================================================================================================
# Find Second Small and Second Large elements from array

# def secondElements(nums):
#     if not nums: return -1, -1
#     if len(nums) == 1: return nums[0], nums[0]
#     large, secondLarge = float('-inf'), float('-inf')
#     small, secondSmall = float('inf'), float('inf')
#     for num in nums:
#         if num > large:
#             secondLarge = large
#             large = num
#         elif num > secondLarge and num != large:
#             secondLarge = num
#
#         if num < small:
#             secondSmall = small
#             small = num
#         elif num < secondSmall and num != small:
#             secondSmall = num
#
#     return secondSmall, secondLarge
#
# print(secondElements([1,2,4,7,7,5]))

# ================================================================================================================================
# Reverse a given array

# def reverseArray(nums):
#     if not nums: return -1
#     l, r = 0, len(nums) - 1
#     while l <= r:
#         nums[l], nums[r] = nums[r], nums[l]
#         l += 1
#         r -= 1
#     return nums
#
# print(reverseArray([10]))

# ================================================================================================================================
# Count frequency of array

# def countFreq(nums):
#     mp = dict()
#     for num in nums:
#         mp[num] = mp.get(num, 0) + 1
#     return mp
#
# print(countFreq([10,5,10,15,10,5]))
# ================================================================================================================================
# Count Frequency Sort
from collections import Counter

# def countSort(nums):
#     count = Counter(nums)
#     sort = sorted(count.items(), key=lambda x: (x[1], x[0]))
#     res = []
#     for ele, freq in sort:
#         res.extend([ele] * freq)
#     return res
#
# print(countSort([4, 5, 6, 5, 4, 3]))

# ================================================================================================================================
# Re-arrange array in increasing decreasing order

# def increasingDecreasing(nums):
#     nums = list(map(int, nums.split()))
#     nums.sort()
#     k = len(nums) // 2
#     r = len(nums) - 1
#     while k <= r:
#         nums[k], nums[r] = nums[r], nums[k]
#         k += 1
#         r -= 1
#     return nums
#
#
# print(increasingDecreasing("4 2 8 6 15 5 9 20"))

# ================================================================================================================================
# Rotate array

# def rotateArray(nums, k):
#     # k %= len(nums)
#     # nums[:] = nums[-k:] + nums[:-k]
#     # return nums
#     n = len(nums)
#     k %= n
#     l, r = 0, n - 1
#     while l <= r:
#         nums[l], nums[r] = nums[r], nums[l]
#         l += 1
#         r -= 1
#
#     l, r = 0, k - 1
#     while l <= r:
#         nums[l], nums[r] = nums[r], nums[l]
#         l += 1
#         r -= 1
#
#     l, r = k, n - 1
#     while l <= r:
#         nums[l], nums[r] = nums[r], nums[l]
#         l += 1
#         r -= 1
#     return nums
#
#
# print(rotateArray([1,2,3,4,5], 2))

# ================================================================================================================================
# Find median of the array

# def median(nums):
#     nums.sort()
#     n = len(nums)
#     if len(nums) % 2 != 0:
#         return nums[n // 2]
#     else:
#         return (nums[(n // 2) - 1] + nums[(n // 2)]) / 2
#
# print(median([2,5,1,7]))

# ================================================================================================================================
# Remove elements from a sorted array

# def removeElements(nums):
#     l = 1
#     for i in range(len(nums) - 1):
#         if nums[i] != nums[i + 1]:
#             nums[l] = nums[i + 1]
#             l += 1
#     return nums
#
# print(removeElements([1,1,2,2,2,3,3]))

# ================================================================================================================================
# Remove duplicates from unsorted array

# def removeDuplicates(nums):
#     seen = set()
#     for num in nums:
#         if num not in seen:
#           seen.add(num)
#
#     return seen
#
# print(removeDuplicates([4,3,9,2,4,1,10,89,34]))

# ================================================================================================================================
# Find all repeating elements in array

# def repeatingElements(nums):
#     count = Counter(nums)
#     res = [k for k, v in count.items() if count[k] > 1]
#     return res
#
#
# print(repeatingElements([1,1,2,3,4,4,5,2]))

# ================================================================================================================================
# Find all the non-repeating elements in array

# def nonRepeating(nums):
#     mp = Counter(nums)
#     res = [k for k, v in mp.items() if mp[k] < 2]
#     return res
#
# print(nonRepeating([1,2,3]))

# ================================================================================================================================
# Find all symmetric pairs

# def symmetricPairs(pairs):
#     pair_map = {}
#     result = []
#
#     for a, b in pairs:
#         # Check if the reverse pair exists in the map
#         if (b, a) in pair_map:
#             result.append((b, a))
#         else:
#             # Add the current pair to the map
#             pair_map[(a, b)] = True
#
#     return result
#
# print(symmetricPairs([(1,2),(2,1),(3,4),(4,5),(5,4)]))

# ================================================================================================================================
# Maximum product subarray

# def maxProd(nums):
#     prod1 = nums[0]
#     prod2 = nums[0]
#     result = nums[0]
#
#     for i in range(1, len(nums)):
#         temp = max(nums[i], prod1 * nums[i], prod2 * nums[i])
#         prod2 = min(nums[i], prod1 * nums[i], prod2 * nums[i])
#         prod1 = temp
#
#         result = max(result, prod1)
#
#     return result
#
# print(maxProd([6, -3, -10, 0, 2]))

# ================================================================================================================================
# Find the pivot element

# def pivotIndex(nums):
#     total = sum(nums)
#     left = 0
#     for r in range(len(nums)):
#         right = total - left - nums[r]
#         if left == right:
#             return r
#         left += nums[r]
#     return -1
#
#
# print(pivotIndex([1,-1,4]))

# ================================================================================================================================
# Sort an array according to the order defined by another array

def sortArray(nums1, nums2):
    mp = Counter(nums1)
    i = 0
    for num in nums2:
        while mp[num]:
            nums1[i] = num
            i += 1
            mp[num] -= 1
    remaining = sorted(mp.elements())
    nums1[i:] = remaining
    return nums1

print(sortArray([2, 1, 2, 5, 7, 1, 9, 9, 5, 6, 3, 6, 8, 8], [2, 1, 8, 3]))

# ================================================================================================================================
# Search element in a an array

# def binarySearch(nums, k):
#     l, h = 0, len(nums) - 1
#     while l <= h:
#         mid = (l + h) // 2
#         if nums[mid] == k: return mid
#         elif nums[mid] > k: h = mid - 1
#         else: l = mid + 1
#     return -1
#
# print(binarySearch([1,2,3,4,5], 4))

# ================================================================================================================================
# Combinations

# def combinations(n, k):
#     def dfs(nums, temp, res, k):
#         if len(temp) == k:
#             res.append(temp)
#             return
#         for i in range(len(nums)):
#             dfs(nums[i+1:], temp + [nums[i]], res, k)
#
#     nums = [i + 1 for i in range(n)]
#     res = []
#     dfs(nums, [], res, k)
#     return res
#
# print(combinations(4, 2))

# ================================================================================================================================
# Combination sum

# def combinationSum(nums, target):
#     def dfs(nums, target, temp, res):
#         if target == 0:
#             res.append(list(temp))
#             return
#         if target < 0: return
#         for i in range(len(nums)):
#             dfs(nums[i:], target - nums[i], temp + [nums[i]], res)
#
#     res = []
#     dfs(nums, target, [], res)
#     return res
#
# print(combinationSum([2,3,5], 8))

# ================================================================================================================================
# Permutations of array or string

# def permutate(nums):
#     nums.sort()
#     mp = dict()
#     res = []
#
#     for i in range(len(nums)):
#         mp[i] = False
#
#     def solve(nums, mp, temp, res):
#         if len(temp) == len(nums):
#             res.append(list(temp))
#             return
#         for i in range(len(nums)):
#             if not mp[i]:
#                 mp[i] = True
#                 temp.append(nums[i])
#                 solve(nums, mp, temp, res)
#                 temp.pop()
#                 mp[i] = False
#     solve(nums, mp, [], res)
#     return res
#
# print(permutate([1,2,3]))

# ================================================================================================================================
# Count vowels, consonants, spaces
import string
# def countFromString(s):
#     s = s.lower()
#     vowels = set(("a", "e", "i", "o", "u"))
#     consonants = set(tuple(string.ascii_lowercase)) - vowels
#     space, vow, con = 0, 0, 0
#     for c in s:
#         if c.isspace(): space += 1
#         if c in vowels: vow += 1
#         if c in consonants: con += 1
#     return space, vow, con
#
#     return consonants
#
# print(countFromString("Take u forward is Awesome"))

# ================================================================================================================================
# Convert string to ascii

# def strToAscii(s):
#     return ord(s)
#
# print(strToAscii('A'))

# ================================================================================================================================
# Remove brackets from an algebraic expression

# def removeBrackets(s):
#     res = ""
#     for c in s:
#         if c != "(" and c != ")": res += c
#     return res
#
#
# print(removeBrackets("(((a-b))+c)"))

# ================================================================================================================================
# Sum of the Numbers in a String

# def sumNumbers(s):
#     res = 0
#     temp = ""
#     for c in s:
#         if c.isnumeric():
#             temp += c
#         else:
#             if temp:  # Ensure temp is not empty before converting to int
#                 res += int(temp)
#                 temp = ""
#     if temp:  # Add any number left in temp after the loop
#         res += int(temp)
#     return res
#
# print(sumNumbers("123xyz"))

# ================================================================================================================================
# Capitalize first and last character of each word

# def capitalizeFirstLast(s):
#     s = s.split()
#     res = []
#     for word in s:
#         if len(word) > 1:
#             word = word[0].upper() + word[1:-1] + word[-1].upper()
#         else:
#             word = word.upper()
#         res.append(word)
#     return " ".join(res)
#
# print(capitalizeFirstLast("take u forward is awesome"))

# ================================================================================================================================
# Calculate frequency of every character

# def frequencyCharacter(s):
#     # mp = dict()
#     # for c in s:
#     #     mp[c] = mp.get(c, 0) + 1
#     # return mp
#     chars = [0] * 26
#     letters = list(string.ascii_lowercase)
#
#     for c in s:
#         if c.islower():
#             chars[ord(c) - ord('a')] += 1
#
#     res = []
#     for i in range(len(chars)):
#         if chars[i] > 0:
#             temp = letters[i] + str(chars[i])
#             res.append(temp)
#
#     return res
#
# print(frequencyCharacter("takeuforward"))

# ================================================================================================================================
# Count anagrams

# def countAnagrams(s, t):
#     return Counter(s) == Counter(t)
#
# print(countAnagrams("rat", "car"))

# ================================================================================================================================
# Count common subsequence

# def countCommonSubsequence(s, t):
#     n1, n2 = len(s), len(t)
#     dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
#     for i in range(1, n1 + 1):
#         for j in range(1, n2 + 1):
#             if s[i - 1] == t[j - 1]:
#                 dp[i][j] = 1 + dp[i - 1][j] + dp[i][j - 1]
#             else:
#                 dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]
#     return dp[n1][n2]
#
# print(countCommonSubsequence("ajblqcpdz", "aefcnbtdi"))

# ================================================================================================================================
# Move Zeros

# def moveZeros(arr):
#     l = 0
#     for r in range(1, len(arr)):
#         if arr[l] == 0 and arr[r] != 0:
#             arr[l], arr[r] = arr[r], arr[l]
#             l += 1
#         elif arr[l] != 0: l += 1
#     return arr
#
# print(moveZeros([4,5,0,1,9,0,5,0]))

# ================================================================================================================================
# Toggle bits and convert to decimal

# def toggle(n):
#     nBin = list(bin(n)[2:])
#     for i, c in enumerate(nBin):
#         if c == '1': nBin[i] = '0'
#         elif c == '0': nBin[i] = '1'
#     return int("".join(nBin), 2)
#
# print(toggle(10))

# ================================================================================================================================
# Sort 0, 1, 2

# def dutchNationalFlag(nums):
#     low, mid, high = 0, 0, len(nums) - 1
#     while mid <= high:
#         if nums[mid] == 0:
#             nums[low], nums[mid] = nums[mid], nums[low]
#             low += 1
#             mid += 1
#         elif nums[mid] == 1:
#             mid += 1
#         elif nums[mid] == 2:
#             nums[mid], nums[high] = nums[high], nums[mid]
#             high -= 1
#     return nums
#
# print(dutchNationalFlag([2,1,0,2,1,0,0,1,2,0]))

# ================================================================================================================================
# Array leaders

# def arrayLeaders(arr):
#     # First reverse the array as per the question if needed
#     l, r = 0, len(arr) - 1
#     while l <= r:
#         arr[l], arr[r] = arr[r], arr[l]
#         l += 1
#         r -= 1
#     res = [arr[-1]]
#     maxEle = res[-1]
#     for i in range(len(arr) - 2, -1, -1):
#         if arr[i] > maxEle:
#             maxEle = arr[i]
#             res.append(arr[i])
#
#     return res
#
# print(arrayLeaders([3, 4, 5, 8, 9]))

# ================================================================================================================================
# Product of digits for the given number

# def productDigits(n):
#     temp = n
#     res = 1
#     while temp != 0:
#         rem = temp % 10
#         res *= rem
#         temp //= 10
#     return res
#
# print(productDigits(123))

# ================================================================================================================================
# Maximum consecutive occur

# def maxConsecutive(s, k):
#     n = len(s)
#     max_aqua = 0
#     for i in range(len(s)):
#         substr = s[i: i + k]
#         count_a = substr.count('a')
#         max_aqua = max(max_aqua, count_a)
#     return max_aqua
#
#
# print(maxConsecutive("abbbaabbb", 5))

# ================================================================================================================================
# Combinations

# def findCombinations(n):
#     return 2 * math.factorial(n - 1)
#
# print(findCombinations(4))

# ================================================================================================================================
# Possible ways to fill cistern

# def waysToFill(n, r):
#     def numToDigit(n):
#         temp = n
#         res = 0
#         while temp != 0:
#             rem = temp % 10
#             res += rem
#             temp //= 10
#         return res
#
#     repeat = r * numToDigit(n)
#     return numToDigit(repeat)
#
#
# print(waysToFill(99, 3))

# ================================================================================================================================
# Fine odd even vehicles

# def fineOddEven(n, nums, d, x):
#     is_even_date = d % 2 == 0
#     total_fine = 0
#
#     for num in nums:
#         is_even_vehicle = num % 2 == 0
#         if is_even_vehicle and not is_even_date: total_fine += x
#         elif not is_even_vehicle and is_even_date: total_fine += x
#     return total_fine
#
#
# print(fineOddEven(5, [2,5,1,6,8], 3, 300))

# ================================================================================================================================
# Remove characters from first string present in second string

# def removeChars(str1, str2):
#     seen = dict()
#     for c in str2:
#         seen[c] = True
#     ans = ""
#     for c in str1:
#         if not seen.get(c):
#            ans += c
#     return ans
#
# print(removeChars("abcdef", "cefz"))

# ================================================================================================================================
# Change every letter with next lexographic alphabet

# def changeLetter(s):
#     s = list(s)
#     for i in range(len(s)):
#         s[i] = string.ascii_lowercase[(ord(s[i]) - ord('a') + 1) % 26]
#     return "".join(s)
#
# print(changeLetter("abcdxyz"))

# ================================================================================================================================
# Program to find the largest word

# def findLargestWord(strs):
#     return sorted(strs.split(), key=len, reverse=True)[0]
#
# print(findLargestWord("Google Doc"))

# ================================================================================================================================
# Find word with highest number of repeated letters in string

# def wordWithHighestRepeated(s):
#     s = s.split()
#     max_repeated = 1
#     res = ""
#     for word in s:
#         letter_count = Counter(word)
#         curr = max(letter_count.values())
#         if curr > max_repeated:
#             max_repeated = curr
#             res = word
#     return res
#
#
# print(wordWithHighestRepeated("abcdefghij google microsoft"))

# ================================================================================================================================
# Change case of each character

# def toggleCase(s):
#     s = list(s)
#     for i in range(len(s)):
#         if s[i].isspace(): continue
#         elif s[i].isupper(): s[i] = s[i].lower()
#         elif s[i].islower(): s[i] = s[i].upper()
#     return "".join(s)
#
# print(toggleCase("javA"))

# ================================================================================================================================
# find string occurrance

# def findString(str1, str2):
#     n = len(str1); m = len(str2)
#     for i in range(n - m + 1):
#         count = 0
#         for j in range(m):
#             if str1[i + j] != str2[j]: break
#             count += 1
#         if count == m: return i
#     return -1
#
# print(findString("takeuforward", "forward"))

# ================================================================================================================================
# Check if a number is a palindrome or not

# def checkNumberPalindrome(n):
#     temp = n
#     rev = 0
#     while temp != 0:
#         digit = temp % 10
#         rev = (rev * 10) + digit
#         temp //= 10
#     return n == rev
#
# print(checkNumberPalindrome(4554))

# ================================================================================================================================
# Find all palindrome numbers in the given range

# def findPalindromes(min, max):
#     def validPalindrome(n):
#         temp = n
#         rev = 0
#         while temp != 0:
#             digit = temp % 10
#             rev = (rev * 10) + digit
#             temp //= 10
#         return rev == n
#     res = []
#     for i in range(min, max + 1):
#         if validPalindrome(i):
#             res.append(i)
#     return res
#
# print(findPalindromes(100, 150))

# ================================================================================================================================
# Check if a number is prime or not

# def isPrime(n):
#     if n <= 1: return False
#
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0: return False
#     return True
#
#
# print(isPrime(4))

# ================================================================================================================================
# Check prime in a given range

# def checkPrime(low, high):
#     def isPrime(n):
#         for i in range(2, int(math.sqrt(n)) + 1):
#             if n % i == 0: return False
#         return True
#
#     res = []
#     for i in range(low, high + 1):
#         if isPrime(i):
#             res.append(i)
#     return res
#
#
# print(checkPrime(11, 17))

# ================================================================================================================================
# Armstrong number

# def isArmstrongNumber(n):
#     temp = n
#     res = 0
#     while temp != 0:
#         digit = temp % 10
#         res += digit ** 3
#         temp //= 10
#     return res == n
#
# print(isArmstrongNumber(370))

# ================================================================================================================================
# Perfect Number

# def perfectNumber(n):
#     res = 0
#     for i in range(1, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             res += i
#             if i != 1 and i != n // i:
#                 res += (n // i)
#     return res == n
#
# print(perfectNumber(28))

# ================================================================================================================================
# Arithematic Progression

# def ap_series(n, a, d):
#     # res = 0
#     # for i in range(n):
#     #     res += a
#     #     a += d
#     # return res
#     return (n / 2) * (2 * a + (n - 1) * d)
#
#
# print(ap_series(5, 1.5, 3))

# ================================================================================================================================
# Sum of GP series

# def gp_series(n, a, r):
#     return a * (((r ** n) - 1) / (r - 1))
#
# print(gp_series(3, 1, 0.5))

# ================================================================================================================================
# Leap year

# def leap_year(year):
#     return ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)
#
# print(leap_year(2025))

# ================================================================================================================================
# Fibonacci series

# def fibbo(n):
#     if n <= 1: return n
#     else: return fibbo(n - 1) + fibbo(n - 2)
#
# print(fibbo(5))

# ================================================================================================================================
# All Prime Factors of the given number

# def primeFactors(n):
#     res = []
#     for i in range(2, n + 1):
#         if n % i == 0:
#             res.append(i)
#         while n % i == 0:
#             n //= i
#     return res
#
# print(primeFactors(60))

# ================================================================================================================================
# Strong number

# def strongNumber(n):
#     temp = n
#     res = 0
#     while temp != 0:
#         digit = temp % 10
#         res += (math.factorial(digit))
#         temp //= 10
#     return res == n
#
# print(strongNumber(26))

# ================================================================================================================================
# Automorphic Number

# def automorphicNumber(n):
#     sq = 76 ** 2
#     while n > 0:
#         if n % 10 != sq % 10:
#             return False
#         n //= 10
#         sq //= 10
#     return True
#
#
# print(automorphicNumber(76))

# ================================================================================================================================
# GCD of two numbers

# def gcd(a, b):
#     if a == 0: return b, 0, 1
#     g, x1, y1 = gcd(b % a, a)
#     x = y1 - (b // a) * x1
#     y = x1
#
#     return g, x, y
#
# print(gcd(9, 12))

# ================================================================================================================================
# LCM of two numbers

# def lcm(a, b):
#     def gcd(c, d):
#         if c == 0: return d, 0, 1
#         g, x1, y1 = gcd(d % c, c)
#         x = y1 - (d // a) * x1
#         y = x1
#         return g, x, y
#
#     return (a * b) // (gcd(a, b)[0])
#
# print(lcm(4, 8))

# ================================================================================================================================
# Harshad number

# def harshadNumber(n):
#     res, temp = 0, n
#     while temp != 0:
#         digit = temp % 10
#         res += digit
#         temp //= 10
#     return n % res == 0
#
# print(harshadNumber(376))

# ================================================================================================================================
# Abundant number

# def abundantNumber(n):
#     res = 0
#     for i in range(1, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             res += i
#             if i != 1 and i != (n // i):
#                 res += (n // i)
#     return "Abundant" if res > n else "Not Abundant"
#
# print(abundantNumber(21))

# ================================================================================================================================
# Sum of numbers in a given range

# def sumRange(l, r):
#     return ((r * (r + 1)) / 2) - (((l-1) * l) / 2)
#
# print(sumRange(2, 7))

# ================================================================================================================================
# Permutation

# def permutation(n, r):
#     return math.factorial(n) / math.factorial(n - r)
#
# print(permutation(6, 4))

# ================================================================================================================================
# Add Fractions

# def addFractions(frac1, frac2):
#     num1, denom1 = map(int, frac1.split('/'))
#     num2, denom2 = map(int, frac2.split('/'))
#
#     # Find Common Denominator from both the fractions
#     common_denom = (denom1 * denom2) // math.gcd(denom1, denom2)
#
#     # Convert the fractions to have same denominator
#     num1 *= (common_denom // denom1)
#     num2 *= (common_denom // denom2)
#
#     res_num = num1 + num2
#     res_denom = common_denom
#
#     # Simplify result
#     common_divisor = math.gcd(res_num, res_denom)
#     res_num //= common_divisor
#     res_denom //= common_divisor
#     return f"{res_num}/{res_denom}"
#
#
# print(addFractions("5/2", "1/2"))

# ================================================================================================================================
# Selection Sort

# def selectionSort(nums):
#     for i in range(len(nums)):
#         mini = i
#         for j in range(i + 1, len(nums)):
#             if nums[j] < nums[mini]:
#                 mini = j
#         nums[i], nums[mini] = nums[mini], nums[i]

# ================================================================================================================================
# Insertion Sort

# def insertionSort(nums):
#     for i in range(len(nums)):
#         j = i
#         while j > 0 and nums[j - 1] > nums[j]:
#             nums[j - 1], nums[j] = nums[j], nums[j - 1]
#             j -= 1
#
# nums = [13,46,24,52,20,9]
# # selectionSort(nums)
# insertionSort(nums)
# print(nums)

# ================================================================================================================================
# Quick Sort

# class QuickSort:
#
#     def helper(self, nums, l, r):
#         pivot = nums[r]
#         i = l - 1
#         for j in range(l, r):
#             if nums[j] <= pivot:
#                 i += 1
#                 nums[j], nums[i] = nums[i], nums[j]
#
#         nums[i + 1], nums[r] = nums[r], nums[i + 1]
#         return i + 1
#
#     def quickSort(self, nums, l, r):
#         if l <= r:
#             mid = self.helper(nums, l, r)
#             self.quickSort(nums, l, mid - 1)
#             self.quickSort(nums, mid + 1, r)
#             return nums
#         return
#
#
# nums = [13,46,24,52,20,9]
# print(QuickSort().quickSort(nums, 0, len(nums) - 1))

# ================================================================================================================================
# Linked List

# class ListNode:
#
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class LinkedList:
#
#     def __init__(self):
#         self.head = None
#         self.size = 0
#
#     def appendleft(self, data):
#         node = ListNode(data)
#         if not self.head:
#             self.head = node
#             self.size += 1
#             return
#
#         node.next = self.head
#         self.head = node
#         self.size += 1
#
#     def append(self, data):
#         node = ListNode(data)
#         if not self.head:
#             self.head = node
#             self.size += 1
#             return
#
#         curr = self.head
#         while curr.next:
#             curr = curr.next
#
#         curr.next = node
#         self.size += 1
#
#     def insertAt(self, ind, data):
#         node = ListNode(data)
#         if not self.head: return
#
#         curr = self.head
#         if ind == 0:
#             node.next = curr.next
#             curr.next = node
#             self.size += 1
#             return
#
#         while curr and ind > 1:
#             curr = curr.next
#             if not curr: return
#             ind -= 1
#
#         node.next = curr.next
#         curr.next = node
#         self.size += 1
#
#     def reverse(self):
#         curr, prev = self.head, None
#         while curr:
#             temp = curr.next
#             curr.next = prev
#             prev = curr
#             curr = temp
#         self.head = prev
#
#     def showList(self):
#         curr = self.head
#         while curr:
#             print(curr.data, "->",end=" ")
#             if not curr.next: print("None")
#             curr = curr.next
#
#
# ll = LinkedList()
# ll.append(10)
# ll.append(11)
# ll.append(23)
# ll.appendleft(5)
# ll.appendleft(1)
# ll.appendleft(2)
# ll.insertAt(3, 45)
# ll.showList()
# ll.reverse()
# ll.showList()
# print(ll.size)

# ================================================================================================================================
# Subsets

# def subsets(nums):
#     res = []
#     def dfs(arr, res, i, temp):
#         if i >= len(arr):
#             res.append(list(temp))
#             return
#         temp.append(arr[i])
#         dfs(arr, res, i + 1, temp)
#         temp.pop()
#         dfs(arr, res, i + 1, temp)
#     dfs(nums, res, 0, [])
#     return res
#
# print(subsets([1,2,3]))

# ================================================================================================================================

def shuffleGlass(glasses, num):
    for i, glass in enumerate(glasses):
        if num in glass:
            num = glass.index(num) + 1
    return num


n = int(input())
glasses = []
for _ in range(3):
    glasses.append(list(map(int, input().split())))

print(shuffleGlass(glasses, n))