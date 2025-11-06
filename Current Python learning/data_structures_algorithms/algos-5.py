# # Count the number of inversions in an array using Enhanced merge sort algorithm
import math

# def countInversions(nums):
#     def mergeSort(arr):
#         if len(arr) > 1:
#             mid = len(arr) // 2
#             L, R = arr[:mid], arr[mid:]
#             inv = 0
#             inv += mergeSort(L)
#             inv += mergeSort(R)
#
#             i, j, k = 0, 0, 0
#             while i < len(L) and j < len(R):
#                 if L[i] <= R[j]:
#                     arr[k] = L[i]
#                     i += 1
#                 else:
#                     arr[k] = R[j]
#                     inv += (len(L) - i)
#                     j += 1
#                 k += 1
#
#             while i < len(L):
#                 arr[k] = L[i]
#                 i += 1
#                 k += 1
#
#             while j < len(R):
#                 arr[k] = R[j]
#                 j += 1
#                 k += 1
#
#             return inv
#         return 0
#     return mergeSort(nums)
#
# print(countInversions([5,3,2,1,0]))

# # =============================================================================================
# Find the Duplicate number

# def findDuplicateNumber(nums):
#     slow = nums[0]
#     fast = nums[0]
#     while True:
#         slow = nums[slow]
#         fast = nums[nums[fast]]
#         if slow == fast: break
#
#     slow2 = nums[0]
#     while slow2 != slow:
#         slow = nums[slow]
#         slow2 = nums[slow2]
#     return slow
#
# print(findDuplicateNumber([1,3,4,2,2]))

# # =============================================================================================
# Find repeated and missing numbers in the array

# def repeatedAndMissing(nums):
#     # mp = {val: 0 for val in range(1, len(nums) + 1)}
#     # for num in nums:
#     #     if num in mp:
#     #         mp[num] += 1
#     #
#     # repeating = 0
#     # missing = 0
#     # for k, v in mp.items():
#     #     if v > 1: repeating = k
#     #
#     # for k, v in mp.items():
#     #     if v <= 0: missing = k
#     #
#     # return missing, repeating
#
#     # Optimal Approach
#     # Let x be repeating and y be missing
#     # Find the sum of all integers N and sum of all integers in array and subtract them -> s - s1
#     # Find the sum of squares of all integers N and sum of squares of all integers in array and subtract them -> s` - s`1
#     # Now x - y = (s - s1)
#     # Now x^2 - y^2 = (s` - s`1)
#     # Solve the above two equations for x, y
#     n = len(nums)
#     x = 0  # repeating
#     y = 0  # missing
#     sn = 0  # sum of integers in array
#     ss = 0  # sum of squares of integers in array
#     s1 = n * (n + 1) // 2  # sum of natural numbers
#     s2 = n * (n + 1) * (2 * n + 1) // 6  # sum of squared of all natural numbers
#
#     for num in nums:
#         sn += num
#         ss += (num ** 2)
#
#     x = (((ss - s2) // (sn - s1)) + (sn - s1)) // 2
#     y = ((ss - s2) // (sn - s1)) - x
#     return x, y
#
# print(repeatedAndMissing([6,4,3,5,5,1]))
# # =============================================================================================

# Move Zeros

# def moveZeros(nums):
#     l, r = 0, 1
#     while r < len(nums):
#         if nums[l] == 0 and nums[r] != 0:
#             nums[l], nums[r] = nums[r], nums[l]
#             l += 1
#         if nums[l] != 0: l += 1
#         r += 1
#     return nums
#
# print(moveZeros([0,1,0,3,12]))

# # =============================================================================================
# # Count Subarrays with XOR of k

# def countSubArraysXOR(nums, k):
#     count = 0
#     for i in range(len(nums)):
#         xor = 0
#         for j in range(i, len(nums)):
#             xor ^= nums[j]
#             if xor == k: count += 1
#     return count
#
# print(countSubArraysXOR([5, 6, 7, 8, 9], 5))

# from collections import defaultdict
# # # Optimal Approach
# def countSubArrays(nums, k):
#     count = 0
#     mp = defaultdict(int)
#     xor = 0
#     mp[xor] = 1
#     for num in nums:
#         xor ^= num
#         x = xor ^ k
#         count += mp[x]
#         mp[xor] += 1
#     return count
#
# print(countSubArrays([4,2,2,6,4], 6))

# # =============================================================================================

# # 4 Sum

# def fourSum(nums, target):
#     # nums.sort()
#     # res = set()
#     # for i in range(len(nums)):
#     #     for j in range(i + 1, len(nums)):
#     #         l, r = j + 1, len(nums) - 1
#     #         while l < r:
#     #             quad = nums[i] + nums[j] + nums[l] + nums[r]
#     #             if quad > target: r -= 1
#     #             elif quad < target: l += 1
#     #             else:
#     #                 res.add((nums[i], nums[j], nums[l], nums[r]))
#     #                 l += 1
#     #                 r -= 1
#     # return res
#
#     nums.sort()
#     res = []
#     for i in range(len(nums)):
#         if i > 0 and nums[i] == nums[i - 1]: continue
#         for j in range(i + 1, len(nums)):
#             if j > i + 1 and nums[j] == nums[j - 1]: continue
#             l, r = j + 1, len(nums) - 1
#             while l < r:
#                 quad = nums[i] + nums[j] + nums[l] + nums[r]
#                 if quad > target: r -= 1
#                 elif quad < target: l += 1
#                 else:
#                     res.append([nums[i], nums[j], nums[l], nums[r]])
#                     l += 1
#                     r -= 1
#                     while l < r and nums[l] == nums[l - 1]: l += 1
#                     while l < r and nums[r] == nums[r + 1]: r -= 1
#     return res
#
# print(fourSum([2,2,2,2,2], 8))

# # =============================================================================================

# # Majority Element - 2

# def majoirtyElement(nums):
#     count1, count2 = 0, 0
#     ele1, ele2 = float('-inf'), float('-inf')
#
#     for num in nums:
#         if count1 == 0 and ele2 != num:
#             count1 = 1
#             ele1 = num
#         elif count2 == 0 and ele1 != num:
#             count2 = 1
#             ele2 = num
#         elif ele1 == num: count1 += 1
#         elif ele2 == num: count2 += 1
#         else:
#             count1 -= 1
#             count2 -= 1
#
#     res = []
#     count1, count2 = 0, 0
#     for num in nums:
#         if num == ele1: count1 += 1
#         if num == ele2: count2 += 1
#
#     if count1 >= int(len(nums) / 3) + 1: res.append(ele1)
#     if count2 >= int(len(nums) / 3) + 1: res.append(ele2)
#     return res
#
# print(majoirtyElement([3,2,3]))

# # =============================================================================================

# # Longest substring without repeating characters

# def longestSubstring(s):
#     seen = set()
#     l = 0
#     maxLen = 0
#     for r in range(len(s)):
#         while s[r] in seen:
#             seen.remove(s[l])
#             l += 1
#         seen.add(s[r])
#         maxLen = max(maxLen, r - l + 1)
#     return maxLen
#
# print(longestSubstring("abcabcbba"))

# # =============================================================================================
# # Print the Camel case characters

# def func(s):
#     res = []
#     l, r = 0, 1
#     while r < len(s):
#         while r < len(s) and not s[r].isupper():
#             r += 1
#         res.append(s[l:r].swapcase())
#         l = r
#         r += 1
#     return res
#
# s = "aAnThe"
# for word in func(s):
#     print(word)

# # =============================================================================================

# def pattern(n):
#     # code here
#     res = []
#     temp = n
#     while temp > 0:
#         res += [temp]
#         temp -= 5
#     while temp != n:
#         res += [temp]
#         temp += 5
#     return res + [n]
#
#
# print(pattern(16))

# ============================================================================================
# class meeting:
#     def __init__(self, start, end, pos):
#         self.start = start
#         self.end = end
#         self.pos = pos
#
# class solution:
#
#     def maxMeetings(self, n, start, end):
#         meetings = [meeting(start[i], end[i], i + 1) for i in range(n)]
#         meetings.sort(key=lambda x: (x.end, x.pos))
#         count = 1
#         limit = meetings[0].end
#         for i in range(1, n):
#             if meetings[i].start > limit:
#                 limit = meetings[i].end
#                 count += 1
#         return count
#
#
# print(solution().maxMeetings(3, [10,12,20], [20,25,30]))

# ============================================================================================

# def printPattern(n):
#     # Print star pattern
#     # for i in range(n):
#     #     print("*" * (i + 1))
#
#     for i in range(n):
#         print(" " * (n - i - 1), end="")
#         print("*" * (2 * i + 1))
#
# printPattern(3)

# n = int(input("Enter the value of n: "))
# num = 0
# star = 8
# count = 0
#
# for i in range(1, n + 1):
#     # Print the first half of star pattern
#     for j in range(1, star + 1):
#         if i + j <= star + 1:
#             print("*", end="")
#     # Print the numbers
#     num += 1
#     for j in range(1, i + 1):
#         print(num, end="")
#         if i > 1 and count < i:
#             print("*", end="")
#             count += 1
#     # Print the other half of the star pattern
#     for j in range(1, star + 1):
#         if i <= j:
#             print("*", end="")
#     print()
#     count = 1

# =========================================================================
# Count Pairs of numbers

# def countPairs(arr, n, k):
#     mp = {}
#     count = 0
#     for i in range(n):
#         if k - arr[i] in mp: count += mp[k - arr[i]]
#         if arr[i] in mp: mp[arr[i]] += 1
#         else: mp[arr[i]] = 1
#     return count
#
# print(countPairs([1, 5, 7, 1], 4, 6))

# ============================================================================================
# Minimum number of platforms required for railway

# def minimumPlatforms(arrival, departures):
#     # # Brute Force
#     # count = 1
#     # for i in range(len(arrival)):
#     #     curr = 1
#     #     for j in range(i + 1, len(arrival)):
#     #         if (arrival[j] <= arrival[i] <= departures[j]) or (arrival[i] <= arrival[j] <= departures[i]):
#     #             curr += 1
#     #     count = max(count, curr)
#     # return count
#
#     # Optimized o(nlogn)
#     arrival.sort(), departures.sort()
#
#     i, j = 1, 0
#     platform, curr = 1, 1
#
#     while i < len(arrival) and j < len(departures):
#         if arrival[i] <= departures[j]:
#             curr += 1
#             i += 1
#         else:
#             curr -= 1
#             j += 1
#         platform = max(platform, curr)
#     return platform
#
#
# print(minimumPlatforms([900, 945, 955, 1100, 1500, 1800], [920, 1200, 1130, 1150, 1900, 2000]))

# ============================================================================================
# Transform prime
# def isPrime(n):
#     if n <= 1: return False
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0: return False
#     return True
#
# def convertPrime(nums):
#     total = sum(nums)
#     i = 1
#     new_total = total
#     while not isPrime(new_total):
#         new_total = total + i
#         i += 1
#     return i - 1
#
# print(convertPrime([2,4,6,8,12]))

# ============================================================================================
# Job Sequencing problem
# import heapq
# class Job:
#
#     def __init__(self, id, deadline, profit):
#         self.id = id
#         self.deadline = deadline
#         self.profit = profit
#
# def jobSequencing(jobs):
#     # jobs.sort(key=lambda x: x.profit, reverse=True)
#     # max_deadline = jobs[0].deadline
#     # for i in range(1, len(jobs)):
#     #     max_deadline = max(max_deadline, jobs[i].deadline)
#     #
#     # slots = [-1] * (max_deadline + 1)
#     # count, profit = 0, 0
#     #
#     # for i in range(len(jobs)):
#     #     for j in range(jobs[i].deadline, 0, -1):
#     #         if slots[j] == -1:
#     #             slots[j] = i
#     #             count += 1
#     #             profit += jobs[i].profit
#     #             break
#     # return count, profit
#
#     jobs.sort(key=lambda x: x.deadline)
#     total = 0
#     slots = []
#     for job in jobs:
#         total += job.profit
#         heapq.heappush(slots, job.profit)
#         while len(slots) > job.deadline: total -= heapq.heappop(slots)
#
#     return len(slots), total
#
#
#
# print(jobSequencing([Job(1,4,20),
#                      Job(2,1,10),
#                      Job(3,1,40),
#                      Job(4,1,30)]))

# ============================================================================================
# Fractional Knapsack

# class Item:
#
#     def __init__(self, profit, weight):
#         self.profit = profit
#         self.weight = weight
#
# def fractionalKnapsack(sack, W):
#     sack.sort(key=lambda x: (x.profit/x.weight), reverse=True)
#     profit = 0
#
#     for item in sack:
#         if item.weight <= W:
#             W -= item.weight
#             profit += item.profit
#         else:
#             profit += item.profit * (W / item.weight)
#             break
#     return profit
#
# print(fractionalKnapsack([Item(100, 20),
#                           Item(60, 10),
#                           Item(120, 30)], 50))

# ============================================================================================
# Smith Number - number should be composite and also sum of digits == sum of prime factors of that number

# def smithNumber(num):
#     def isPrime(n: int):
#         if n <= 1: return False
#         for i in range(2, int(math.sqrt(n)) + 1):
#             if n % i == 0: return False
#         return True
#
#     def sumDigits(num):
#         temp = num
#         total = 0
#         while temp:
#             digit = temp % 10
#             total += digit
#             temp //= 10
#         return total
#
#     if isPrime(num): return 0
#
#     digitSum = sumDigits(num)
#     sumOfFactors = 0
#     for i in range(2, int(math.sqrt(num)) + 1):
#         if isPrime(i):
#             while num % i == 0:
#                 sumOfFactors += sumDigits(i)
#                 num //= i
#
#     if num > 1 and isPrime(num): sumOfFactors += sumDigits(num)
#     return 1 if digitSum == sumOfFactors else 0
#
# # print(sumDigits(12))
#
# # print(prime_factors(378))
#
# print(smithNumber(378))

# ============================================================================================
# Subarray with sum 0

# def subarraySum(nums):
#     seen = set()
#     total = 0
#     for num in nums:
#         total += num
#         if not total or total in seen: return True
#         seen.add(total)
#     return False
#
# print(subarraySum([4,2,-3,1,6]))

# Longest subarray with sum 0
# def longestSubarraySum(nums):
#     mp = dict({0: -1})
#     total = 0
#     res = 0
#     for i in range(len(nums)):
#         total += nums[i]
#         if total not in mp: mp[total] = i
#         else: res = max(res, i - mp[total])
#     return res
#
# print(longestSubarraySum([15,-2,2,-8,1,7,10,23]))
# ============================================================================================

# Maximum subarray of size k

# def maxSumSubarray(nums, k):
#     if k == len(nums): return sum(nums)
#
#     max_sum = window_sum = sum(nums[:k])
#     for i in range(k, len(nums)):
#         window_sum += nums[i] - nums[i - k]
#         max_sum = max(max_sum, window_sum)
#     return max_sum
#
# print(maxSumSubarray([100, 400, 300, 200], 2))

# ============================================================================================
# Gold Mine Dynamic Programming

# def goldMine(mine):
#     rows, cols = len(mine), len(mine[0])
#
#     dp = [[0] * cols for _ in range(rows)]
#     for i in range(rows):
#         dp[i][cols - 1] = mine[i][cols - 1]
#
#     for j in range(cols - 2, -1, -1):
#         for i in range(rows):
#             right = dp[i][j + 1] if j + 1 < cols else 0
#             up_right = dp[i - 1][j + 1] if i - 1 >= 0 and j + 1 < cols else 0
#             down_right = dp[i + 1][j + 1] if i + 1 < rows and j + 1 < cols else 0
#
#             dp[i][j] = mine[i][j] + max(right, up_right, down_right)
#     max_gold = max(dp[i][0] for i in range(rows))
#     return max_gold
#
#
# print(goldMine([[1, 3, 3],
#                 [2, 1, 4],
#                 [0, 6, 4]]))

# ============================================================================================
# Consecutive's Ones not allowed

# def noConsecutive(n):
#     if n == 1: return 2
#     if n == 2: return 3
#     a, b = 2, 3
#     mod = 10**9 + 7
#     for _ in range(3, n + 1):
#         temp = (a + b) % mod
#         a = b
#         b = temp
#     return b % mod
#
# print(noConsecutive(3))

# ============================================================================================
# Reach the nth point

# def reachPoint(n):
#     mod = 10**9 + 7
#     if n == 1: return 1
#     if n == 2: return 2
#     a, b = 1, 2
#     for _ in range(3, n + 1):
#         temp = (a + b) % mod
#         a = b
#         b = temp
#     return b % mod
#
# print(reachPoint(4))
# ============================================================================================

# Maximum sum without adjacent
# def maxSum(nums):
#     # dp = [0] * len(nums)
#     # dp[0] = nums[0]
#     # for i in range(1, len(nums)):
#     #     incl = dp[i - 2] + nums[i]
#     #     excl = dp[i - 1] + 0
#     #     dp[i] = max(incl, excl)
#     # return dp[len(nums) - 1]
#
#     prev1, prev2 = 0, nums[0]
#     for i in range(1, len(nums)):
#         incl = prev1 + nums[i]
#         excl = prev2 + 0
#         res = max(incl, excl)
#
#         prev1 = prev2
#         prev2 = res
#     return prev2
#
#
# print(maxSum([5, 5, 10, 100, 10, 5]))

# ============================================================================================
# Find the Nth root of number

# def findNthRoot(n, m):
#     def calc(mid, m, n):
#         ans = 1
#         for i in range(1, n + 1):
#             ans *= mid
#             if ans > m: return 2
#         if ans == m: return 1
#         return 0
#
#     low, high = 1, m
#     while low <= high:
#         mid = (low + high) // 2
#         guess = calc(mid, m, n)
#         if guess == 1: return mid
#         elif guess == 0: low = mid + 1
#         else: high = mid - 1
#     return -1
#
# print(findNthRoot(2, 9))

# ============================================================================================
# File Latest version

# def fileVersion(files):
#     latest = -1
#     for file in files:
#         version = int(file[-1])
#         latest = max(latest, version)
#     return latest
#
# print(fileVersion(['FILE_1', 'FILE_3', 'FILE_2']))
# print(fileVersion([]))
# print(fileVersion(['FILE_1', 'FILE_3', 'FILE_2']))

# ============================================================================================
# Maximum average subarray

# def maxAvg(nums, k):
#     # maxAvg = float('-inf')
#     # for i in range(len(nums) - k + 1):
#     #     curr = nums[i:i+k]
#     #     maxAvg = max(sum(curr) / k, maxAvg)
#     # return maxAvg
#
#     window = sum(nums[:k])
#     maxAvg = window
#
#     for i in range(k, len(nums)):
#         window += nums[i] - nums[i - k]
#         maxAvg = max(window, maxAvg)
#     return maxAvg / k
#
#
# print(maxAvg([1, 12, -5, -6, 50, 3], 4))
# ============================================================================================

# Max consecutive ones - |||

# def maxOnes(nums, k):
#     zeros = 0
#     j = 0
#     res = float('-inf')
#     for i in range(len(nums)):
#         if nums[i] == 0:
#             zeros += 1
#         while zeros > k:
#             if nums[j] == 0:
#                 zeros -= 1
#             j += 1
#         res = max(res, i - j + 1)
#     return res
# print(maxOnes([1,1,1,0,0,0,1,1,1,1,0], 2))

# ============================================================================================

# Longest subarray of ones when one zero is removed

# def longestSubarray(nums):
#     i, j, k = 0, 0, 1
#     res = 0
#
#     while i < len(nums):
#         if nums[i] == 0: k -= 1
#         while k < 0:
#             if nums[j] == 0: k += 1
#             j += 1
#         res = max(res, i - j)
#         i += 1
#     return res
#
# print(longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]))

# ============================================================================================

# Find the highest altitude

# def highestAltitude(gain):
#     prefix = 0
#     res = [0]
#     for i in range(len(gain)):
#         prefix += gain[i]
#         res.append(prefix)
#     return max(res)
#
# print(highestAltitude([-5,1,5,0,-7]))

# ============================================================================================

# RecentCalls - Queue

# class RecentCalls:
#
#     def __init__(self):
#         self.queue = []
#
#     def ping(self, t):
#         self.queue.append(t)
#         while self.queue[0] < self.queue[-1] - 3000: self.queue.pop()
#         return len(self.queue)
#
# print(RecentCalls().ping(0))
# print(RecentCalls().ping(1))
# print(RecentCalls().ping(100))
# print(RecentCalls().ping(3001))
# print(RecentCalls().ping(3002))

# ============================================================================================

# def sample(n):
#     res = []
#     for i in range(n):
#         res.append(input(f"enter {i + 1}: "))
#     res = sorted(res, reverse=True)
#     return res
#
# Minimum length of subarray sum
# print(sample(5))

# ============================================================================================

# def maximumSum(nums, target):
#     n = len(nums)
#     min_length = float('inf')
#     left = 0
#     current_sum = 0
#
#     for right in range(n):
#         current_sum += nums[right]
#
#         while current_sum >= target:
#             min_length = min(min_length, right - left + 1)
#             current_sum -= nums[left]
#             left += 1
#
#     return min_length if min_length != float('inf') else 0
#
# print(maximumSum([2,3,1,2,4,3], 7))
