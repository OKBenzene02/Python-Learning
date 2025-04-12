# Best time to buy stocks and sell - 2
import collections
import math

# def buyStocksAndSell(prices):
#     # profit = 0
#     # for i in range(1, len(prices)):
#     #     if prices[i - 1] < prices[i]:
#     #         profit += prices[i] - prices[i - 1]
#     # return profit
#
#     i = 0
#     valley = prices[0]; peak = prices[0]
#     maxProfit = 0
#     while i < len(prices) - 1:
#         while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
#             i += 1
#         valley = prices[i]
#         while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
#             i += 1
#         peak = prices[i]
#         maxProfit += peak - valley
#     return maxProfit
#
# print(buyStocksAndSell([7,1,5,3,6,4]))
# # ========================================================================
# # H-index

# def Hindex(citations):
#     citations.sort()
#     for i in range(len(citations)):
#         if citations[i] >= len(citations) - i: return len(citations) - i
#     return -1
#
# print(Hindex([1,3,1]))

# def Hindex(citations):
#     low, high = 0, len(citations)
#     while low < high:
#         mid = (low + high) // 2
#         if citations[mid] >= len(citations) - mid: return len(citations) - mid
#         elif citations[mid] < len(citations) - mid: low = mid + 1
#         else: high = mid - 1
#     return 0
#
# print(Hindex([0,1,3,5,6]))
# # ========================================================================

# # Insert Delete GetRandom O(1)

# import random
#
# class RandomizedSet:
#
#     def __init__(self):
#         self.mp = dict()
#         self.array = []
#     def insert(self, val) -> bool:
#         if val in self.mp: return False
#         self.array.append(val)
#         self.mp[val] = self.array.index(val)
#         return True
#     def remove(self, val) -> bool:
#         if not val in self.mp: return False
#         elementToRemove = self.mp[val]
#         lastElement = self.array[-1]
#
#         self.mp[lastElement] = elementToRemove
#         self.array[elementToRemove] = lastElement
#         self.array[-1] = val
#         self.array.pop()
#         self.mp.pop(val)
#         return True
#
#     def getRandom(self) -> int:
#         return random.choice(self.array)
#
#
# sol = RandomizedSet()
# print(sol.insert(1))
# print(sol.remove(2))
# print(sol.insert(2))
# print(sol.getRandom())
# print(sol.remove(1))
# print(sol.insert(2))
# print(sol.getRandom())

# # ========================================================================

# # Product of Array Expect Self

# def productOfArray(nums):
#     prefix, postfix, res = 1, 1, [1] * len(nums)
#     for i in range(len(nums)):
#         res[i] = prefix
#         prefix *= nums[i]
#     for i in range(len(nums) - 1, -1, -1):
#         res[i] *= postfix
#         postfix *= nums[i]
#     return res
#
# print(productOfArray([1,2,3,4]))

# # ========================================================================
# def custom_counter(nums, k):
#     mp = {}
#     for num in nums:
#         mp[num] = mp.get(num, 0) + 1
#
#     arr = [[] for _ in range(len(nums) + 1)]
#     for key, ele in mp.items():
#         arr[ele].append(key)
#     final = []
#     for i in range(len(arr) - 1, 0, -1):
#         if arr[i]:
#             final.extend(arr[i])
#     return final
#
# print(custom_counter([1, 1], 3))
# # ========================================================================
# Increasing chain problem using DP

# def increasingChain(nums):
#     n = len(nums)
#     if n == 0:
#         return 0
#
#     dp = [1] * n
#
#     for i in range(1, n):
#         for j in range(i):
#             if nums[i] > nums[j]:
#                 dp[i] = max(dp[i], dp[j] + 1)
#                 # print(nums[j], nums[i])
#
#     return max(dp) if max(dp) != 1 else 0
#
# print(increasingChain([11, 10, 3, 4, 5, 6]))

# # ========================================================================

# Integer to roman

# def intToRoman(num):
#     symbols = {1000: 'M',
#                900: 'CM',
#                500: 'D',
#                400: 'CD',
#                100: 'C',
#                90: 'XC',
#                50: 'L',
#                40: 'XL',
#                10: 'X',
#                9: 'IX',
#                5: 'V',
#                4: 'IV',
#                1: 'I'
#                }
#     res = ""
#     for k in symbols:
#         res += (num // k) * symbols[k]
#         num %= k
#     return res
#
# print(intToRoman(1994))

# # ========================================================================

# Ransom Notes
from collections import Counter, defaultdict
# def ransomNote(ransom, magazine):
#     print(Counter(ransom))
#     print(Counter(magazine))
#
# print(ransomNote("aa", "aab"))

# # ========================================================================

# Word Pattern

# def wordPattern(pattern, s):
#     if len(pattern) != len(s.split(" ")): return False
#     patMap, strMap = {}, {}
#     for c1, c2 in zip(pattern, s.split(" ")):
#         if (c1 in patMap and patMap[c1] != c2) or (c2 in strMap and strMap[c2] != c1):
#             return False
#         patMap[c1] = c2
#         strMap[c2] = c1
#     return True
#
# print(wordPattern("abba", "dog cat cat fish"))

# # ========================================================================

# Two Sum 2 - where input array is sorted and solution to be given is in o(n)

# def twoSum2(nums, target):
#     l, r = 0, len(nums) - 1
#     while l < len(nums) and r > 0:
#         currTarget = nums[l] + nums[r]
#         if currTarget == target: return [l + 1, r + 1]
#         if currTarget > target: r -= 1
#         else: l += 1
#     return False
#
# print(twoSum2([2,7,11,13], 9))

# # ========================================================================

# Valid Anagram and Group Anagrams

# def validAnagram(s, t):
#     if len(s) != len(t): return False
#     return Counter(s) == Counter(t)
#
# print(validAnagram("anagram", "nagaram"))

# def gropuAnagrams(strings):
#     str_dict = defaultdict(list)
#     for words in strings:
#         str_dict[tuple(sorted(words))].append(words)
#     return list(str_dict.values())
#
# print(gropuAnagrams(["eat","tea","tan","ate","nat","bat"]))

# # ========================================================================

# Contains duplicate II

# def containsDuplicate(nums, k):
#     mp = {}
#     for i, num in enumerate(nums):
#         if num in mp and abs(i - mp[num]) <= k: return True
#         mp[num] = i
#     return False
#
# print(containsDuplicate([1,2,3,1], 3))

# # ========================================================================

# Longest consecutive sequence

# def longestConsecutive(nums):
#     st = set(nums); maxSeq = 0; currSeq = 0
#     for num in nums:
#         if (num - 1) not in st:
#             currSeq = 0
#             while (num + currSeq) in st: currSeq += 1
#         maxSeq = max(currSeq, maxSeq)
#     return maxSeq
#
# print(longestConsecutive([100, 4, 200, 1, 3, 2]))
# # ========================================================================

# Maximum sum subarray

# def maxSubarraySum(nums):
#     # Boundary condition
#     if all(num < 0 for num in nums): return max(nums)
#
#     inverted = [-1 * num for num in nums]
#
#     # original kadane's algorithm
#     tempMax, tempRes = 0, -999999999
#     for num in nums:
#         tempMax += num
#         if tempMax > tempRes:
#             tempRes = tempMax
#         if tempMax < 0:
#             tempMax = 0
#
#     # Inverted array's kadane's algorithm
#     currSum, maxSum= 0, -999999999
#     for num in inverted:
#         currSum += num
#         if currSum > maxSum:
#             maxSum = currSum
#         if currSum < 0:
#             currSum = 0
#
#     return max(-1 * (sum(inverted) + (-1 * maxSum)), tempRes)
#
# print(maxSubarraySum([5, -3, -2, 6, -1, 4]))

# # ========================================================================
# Candy - Array problem hard
#
# def candy(ratings):
#     if not ratings: return 0
#     n, candies = len(ratings), [1] * len(ratings)
#     # Iterating from start to end - 1 index
#     for i in range(n - 1):
#         # print(ratings[i], ratings[i + 1])
#         if ratings[i] < ratings[i + 1]: candies[i + 1] = max(1 + candies[i], candies[i + 1])
#     # Iterating from end - 2 to start index
#     for i in range(n - 2, -1, -1):
#         # print(ratings[i], ratings[i + 1])
#         if ratings[i + 1] < ratings[i]: candies[i] = max(candies[i + 1] + 1, candies[i])
#
#     return sum(candies)
#
# print(candy([1, 0, 2]))
# # ========================================================================

# Trapping rain water

# def trappingRainWater(height):
#     if not height: return 0
#
#     l, r = 0, len(height) - 1
#     leftMax, rightMax = height[l], height[r]
#     res = 0
#     while l < r:
#         if leftMax < rightMax:
#             l += 1
#             leftMax = max(leftMax, height[l])
#             res += leftMax - height[l]
#         else:
#             r -= 1
#             rightMax = max(rightMax, height[r])
#             res += rightMax - height[r]
#     return res
#
# print(trappingRainWater([0,1,0,2,1,0,1,3,2,1,2,1]))

# # ========================================================================
# find duplicates in an array using mathematical function

# def findDuplicates(nums):
#     res = []
#     for i in range(len(nums)):
#         idx = nums[i] % len(nums)
#         nums[idx] += len(nums)
#     for i, num in enumerate(nums):
#         if num >= 2 * len(nums): res.append(i)
#
#     if len(res) == 0: return -1
#     else: return res
#
# print(findDuplicates([2,3,1,2,3]))

# # ========================================================================

# Single number bit manipulation

# def singleNumber(nums):
#     xor = 0
#     for i in range(len(nums)):
#         xor ^= nums[i]
#     return xor
#
# print(singleNumber([2,2,3,2]))
# # ========================================================================

# Bitwise AND of Numbers Range

# def bitwiseAND(left, right):
#     if left == -(2 ** 32 - 1) or right == 2 ** 32: return 0
#     bit_and = left
#     for num in range(left, right + 1):
#         bit_and &= num
#     return bit_and
#
# print(bitwiseAND(1, 2147483647))

# # ========================================================================
# def symmetricPairs(nums):
#     seen = set()
#     for num in nums:
#         a, b = num
#         if ([b, a] in nums) and (((a, b) and (b, a)) not in seen): seen.add((a, b))
#
#     for num in seen:
#         a, b = num
#         print(f"{a, b} and {b, a} are symmetric")
#
#
# print(symmetricPairs([[1, 2], [3,4], [5,6], [2,1], [4,3], [10,11]]))

# # ========================================================================

# def differentIdx(nums):
#     rem = nums[0] % 2
#     for i in range(1, len(nums)):
#         if nums[i] % 2 != rem: return i + 1
#
#     return -1
#
# n = int(input())
# arr = [int(num) for num in input().split(" ")]
# print(differentIdx(arr))

# # ========================================================================

# Search Suggestions of words

# def suggestProducts(products, searchWord):
#     res = []
#     products.sort()
#
#     l, r = 0, len(products) - 1
#     for i in range(len(searchWord)):
#         char = searchWord[i]
#
#         while l <= r and (len(products[l]) <= i or products[l][i] != char): l += 1
#         while l <= r and (len(products[r]) <= i or products[r][i] != char): r -= 1
#
#         res.append([])
#         remain = r - l + 1
#         for k in range(min(3, remain)):
#             res[-1].append(products[l + k])
#     return res
#
# print(suggestProducts(["mobile","mouse","moneypot","monitor","mousepad"], "mouse"))

# # ========================================================================

# Buddy Strings

# def buddyStrings(s, goal):
#     n = len(s)
#     if s == goal:
#         temp = set(s)
#         return len(temp) < len(goal)
#
#     i, j = 0, n - 1
#     while i < len(s) and s[i] == goal[i]: i += 1
#     while j > 0 and s[j] == goal[j]: j -= 1
#
#     if i < j:
#         l = list(s)
#         l[i], l[j] = l[j], l[i]
#         s = "".join(l)
#     return s == goal
#
#
# print(buddyStrings('ab', 'ab'))

# # ========================================================================

# Longest valid parentheses

# def longestValid(s):
#     dp, stack = [0] * (len(s) + 1), []
#     for i in range(len(s)):
#         if s[i] == '[': stack.append(i)
#         else:
#             if stack:
#                 char = stack.pop()
#                 dp[i + 1] = dp[char] + i - char + 1
#     return max(dp)
#
#
# print(longestValid('][][]]'))

# # ========================================================================

# Frequency game
# from collections import Counter
# def frequency(nums):
#     for k, v in Counter(nums).items():
#         print(f"{k} occurs {v} times")
#
# frequency([1,2,3,5,2,9,7,3,5])

# # ========================================================================

# Minimum path sum

# def minPathSum(grid):
#     m = len(grid)
#     n = len(grid[0])
#
#     for i in range(1, n):
#         grid[0][i] += grid[0][i - 1]
#
#     for i in range(1, m):
#         grid[i][0] += grid[i - 1][0]
#
#     for i in range(1, m):
#         for j in range(1, n):
#             grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
#
#     return grid[-1][-1]
#
# print(minPathSum([[0,3],[5,100],[1,2]]))

# # ========================================================================

# def splitSep(words, sep):
#     res = []
#     for word in words:
#         for split in word.split(sep):
#             if split: res.append(split)
#     return res
#
# print(splitSep(["|||"], '|'))

# # Largest Element in an Array after Merge Operations

# def largestElement(nums):
#     # queue = []
#     # queue.extend(nums)
#     # while len(queue) > 1:
#     #     n1, n2 = queue.pop(), queue.pop()
#     #     if n1 >= n2:
#     #         n1 += n2
#     #         queue.append(n1)
#     #     else:
#     #         queue.append(n2)
#     # return queue[0]
#
#     stack = []
#     for num in reversed(nums):
#         while stack and stack[-1] >= num:
#             num += stack.pop()
#         stack.append(num)
#     return stack[-1]
#
# print(largestElement([2,3,7,9,3]))
# # ========================================================================

# def count_complete_subarrays(nums):
#     def count_distinct_elements(arr):
#         return len(set(arr))
#
#     num_elements = len(nums)
#     left, right = 0, 0
#     freq_map = {}
#     total_distinct = count_distinct_elements(nums)
#     complete_subarrays = 0
#
#     while right < num_elements:
#         # Expand the window and update frequency map
#         freq_map[nums[right]] = freq_map.get(nums[right], 0) + 1
#
#         # Shrink the window until the subarray is no longer complete
#         while count_distinct_elements(freq_map) == total_distinct:
#             freq_map[nums[left]] -= 1
#             if freq_map[nums[left]] == 0:
#                 del freq_map[nums[left]]
#             left += 1
#
#         # Count complete subarrays that end at index 'right'
#         complete_subarrays += left
#
#         right += 1
#
#     return complete_subarrays
#
# # Example usage:
# nums = [5,5,5,5]
# print(count_complete_subarrays(nums))

# # ========================================================================
# Letter combinations of phone number

# def letterCombinations(digits):
#     def dfs(temp, res, i):
#         if len(digits) == i:
#             res.append("".join(temp))
#             return
#         for char in mp.get(digits[i]):
#             temp.append(char)
#             dfs(temp, res, i + 1)
#             temp.pop()
#
#     mp = {
#         '2': ['a', 'b', 'c'],
#         '3': ['d', 'e', 'f'],
#         '4': ['g', 'h', 'i'],
#         '5': ['j', 'k', 'l'],
#         '6': ['m', 'n', 'o'],
#         '7': ['p', 'q', 'r', 's'],
#         '8': ['t', 'u', 'v'],
#         '9': ['w', 'x', 'y', 'z'],
#     }
#     res = []
#     dfs([], res, 0)
#
#     return res
#
# print(letterCombinations("23"))


# def leastNumber(scores):
#     n = len(scores)
#     nearest_smaller = [-1] * n
#     stack = []
#
#     for i in range(n):
#         while stack and scores[i] < scores[stack[-1]]:
#             nearest_smaller[stack.pop()] = i + 1
#         stack.append(i)
#
#     return nearest_smaller

# def numberPattern(n):
#     num, res = 1, []
#     for i in range(n):
#         temp = [-1] * n
#         for j in range(i + 1):
#             if num > 9:
#                 num = 1
#             temp[-(i + 1) + j] = num
#             num += 1
#         res.append(temp)
#     return res
#
# print(numberPattern(3))

# def printPattern(n):
#     for i in range(n):
#         print(" " * (n - i - 1), end="")
#         print("*" * (2 * i + 1))
#
# printPattern(5)

# def convertCases(s):
#     res = ""
#     for i, char in enumerate(s):
#         if i == 0 and char.isupper(): res += char.lower()
#         elif i > 0 and char.isupper(): res += " " + char.lower()
#         else:
#             res += char.lower()
#     return res
#
# print(convertCases("hello world"))

# def funcc(a,b):
#     return a + b
# n = 5
# h = 5
# # res = funcc(n,h)
# # funcc(n, h)
# funcc(n,h)

# def countRepeated(s):
#     counter = Counter(s)
#     repeated = {char: count for char, count in counter.items() if count > 1}
#     return repeated
#
# print(countRepeated("hello world"))
#

# def pairsWithSum(nums, x):
#     # res = []
#     # seen = set()
#     # for num in nums:
#     #     left = x - num
#     #     if left in seen: res.append([num, left])
#     mp = {}
#     for i, num in enumerate(nums):
#         left = x - num
#         if left in mp: return [mp[i], left]
#         mp[num] = i
#
# print(pairsWithSum([1, 2, 3, 4, 5, 6, 7], 5))

# def countStringNumber(s):
#     total = 0
#     for char in s:
#         if char.isalpha():
#             total += ord(char.upper()) - ord('A')
#     return total
#
# print(countStringNumber("ZXY"))

# ===================================================================
# Monotonic Array

# def isMonotonic(nums) -> bool:
#     increase = False
#     decrease = False
#     for i in range(len(nums) - 1):
#         if nums[i] < nums[i + 1]:
#             increase = True
#         elif nums[i] >= nums[i + 1]:
#             decrease = True
#     return False if increase and decrease else True
#
# print(isMonotonic([6,5,4,4]))
# ===================================================================

# Reverse Vowels in string
# def reverseVowels(s: str) -> str:
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     stack = []
#     for vowel in s:
#         if vowel in vowels: stack.append(vowel)
#
#     s = list(s)
#     for i, char in enumerate(s):
#         if char in vowels:
#             s[i] = stack.pop()
#     return "".join(s)

# Reverse words in the string
# def reverseWords(s):
#     res = ""
#     i = 0
#     n = len(s)
#     while i < n:
#         while i < n and s[i] == " ": i += 1
#
#         if i >= n: break
#         j = i + 1
#         while j < n and s[j] != ' ': j += 1
#         word = s[i: j]
#         if not res: res = word
#         else: res = word + " " + res
#         i = j + 1
#     return res
#
# print(reverseWords("hello world"))

# # ============================================================================
# Set Matrix zeros

# def setZeros(matrix):
#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             if matrix[i][j] == 0:
#                 # Change the row values of that 0 as -1
#                 for m in range(len(matrix)):
#                     if matrix[m][j] != 0:
#                         matrix[m][j] = -1
#
#                 # Change the column values of that 0 as -1
#                 for n in range(len(matrix[0])):
#                     if matrix[i][n] != 0:
#                         matrix[i][n] = -1
#
#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             if matrix[i][j] == -1:
#                 matrix[i][j] = 0
#
#     return matrix
#
# print(setZeros([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))

# # ============================================================================
# Next Permutation in lexicographically greater form

# def nextPermutation(nums):
#     n = len(nums)
#     idx = -1
#     for i in range(n - 2, -1, -1):
#         if nums[i] < nums[i + 1]:
#             idx = i
#             break
#
#     if idx == -1:
#         nums.sort()
#         return nums
#
#     for i in range(n - 1, idx, -1):
#         if nums[i] > nums[idx]:
#             nums[i], nums[idx] = nums[idx], nums[i]
#             break
#
#     nums[idx + 1: ] = reversed(nums[idx + 1: ])
#     return nums
#
#
# print(nextPermutation([4,3,2,1]))
# # ============================================================================
# Increasing Triplet Subsequence

# def increasingTripletSequence(nums):
#     left, mid = float('inf'), float('inf')
#     for right in nums:
#         if right < left: left = right
#         elif left < right < mid: mid = right
#         elif mid < right: return True
#     return False
# 
# print(increasingTripletSequence([2,1,5,0,4,6]))
