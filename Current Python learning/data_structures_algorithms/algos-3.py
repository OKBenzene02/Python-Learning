# Maximum Zeros in an array
import math
from typing import List


# def maximumZeros(mat):
#     res = []
#     for i, row in enumerate(mat):
#         temp = [i, row.count(1)]
#         res.append(temp)
#     return max(res, key=lambda x: x[1])
#
# print(maximumZeros([[0,1],[1,0]]))

# =======================================================================
# Maximum Divisibility

# def maximumDivisibility(nums, divisors):
#     max_score, max_div = -1, -1
#     for divisor in divisors:
#         score = 0
#         for num in nums:
#             if num % divisor == 0:
#                 score += 1
#         if score > max_score:
#             max_div = divisor
#             max_score = score
#         if score == max_score:
#             max_div = min(divisor, max_div)
#     return max_div
#
#
# print(maximumDivisibility([12], [10,16]))

# =======================================================================
# Minimum Additions to make a valid string

# def minimumAdditions(s):
#     it = 0
#     res = 0
#     while it < len(s):
#         if s[it:it+3] == 'abc':
#             it += 3
#         elif s[it:it+2] in ['ab', 'ac', 'bc']:
#             res += 1
#             it += 2
#         else:
#             res += 2
#             it += 1
#     return res
#
#
# print(minimumAdditions("aaaaab"))
# =======================================================================

# Kids With the Greatest Number of Candies

# def kidsWithCandies(candies, extraCandies):
#     ele = max(candies)
#     for i, candy in enumerate(candies):
#         if candy + extraCandies >= ele:
#             candies[i] = True
#         else:
#             candies[i] = False
#     return candies
#
# print(kidsWithCandies([12, 1, 12], 10))
# =======================================================================

# Number of Ways to Form a Target String Given a Dictionary

# def numWays(words, target):
#     n, m = len(words[0]), len(target)
#     dp = [0] * (m + 1)
#     dp[0] = 1
#
#     count = [[0] * 26 for _ in range(n)]
#
#     mod = 10**9 + 7
#
#     for i in range(n):
#         for word in words:
#             count[i][ord(word[i]) - ord('a')] += 1
#
#     for i in range(n):
#         for j in range(m - 1, -1, -1):
#             dp[j + 1] += dp[j] * count[i][ord(target[j]) - ord('a')]
#             dp[j + 1] %= mod
#
#     return dp[m]
#
# print(numWays(["acca","bbbb","caca"], "aba"))
# =======================================================================

# Merge Strings Alternately

# def mergeAlternately(word1, word2):
#     res = ""
#     i, j = 0, 0
#     while i < len(word1) and j < len(word2):
#         res += word1[i] + word2[j]
#         i += 1
#         j += 1
#
#     while i < len(word1):
#         res += word1[i]
#         i += 1
#
#     while j < len(word2):
#         res += word2[j]
#         j += 1
#
#     return res
#
#
# print(mergeAlternately("abcd", "pq"))
# =======================================================================

# Where will the ball fall using DFS
# from typing import List
#
# def findBall(grid: List[List[int]]) -> List[int]:
#     def findBallDrop(row, col, grid):
#         if row == len(grid): return col
#
#         nextCol = col + grid[row][col]
#
#         if nextCol < 0 or nextCol > len(grid[0]) - 1 or grid[row][col] != grid[row][nextCol]:
#             return -1
#         return findBallDrop(row + 1, nextCol, grid)
#
#     res = [0 for _ in range(len(grid))]
#     for i in range(len(grid)):
#         res[i] = findBallDrop(0, i, grid)
#     return res
#
# print(findBall([[-1]]))

# =======================================================================

# Multiply strings

# def multiplyStrings(num1, num2):
#     def multiply(a, b):
#         if b == 0: return 0
#         if b % 2 == 0: return multiply(a + a, b // 2)
#         return multiply(a + a, b // 2) + a
#
#     num1, num2 = num1.split(" "), num2.split(" ")
#     a, b = 0, 0
#     for num in num1:
#         if num.isdigit():
#             a = int(num)
#     for num in num2:
#         if num.isdigit():
#             b = int(num)
#
#     return str(multiply(a, b)) if (b > 0 and a > 0) else str(-multiply(abs(a), abs(b)))
#
# print(multiplyStrings("123", "456"))

# =======================================================================

# Minimum Insertions to make palindromic String

# def palindromicString(s):
#     n = len(s)
#     dp = [0] * n
#
#     for i in range(n - 2, -1, -1):
#         prev = 0
#         for j in range(i + 1, n):
#             temp = dp[j]
#             if s[i] == s[j]:
#                 dp[j] = prev
#             else:
#                 dp[j] = min(dp[j], dp[j - 1]) + 1
#
#             prev = temp
#
#     return dp[n - 1]
#
# print(palindromicString("mbadm"))

# =======================================================================
# Restore array

# def restore(s, k):
#     m, n = len(s), len(str(k))
#     dp, mod = [0] * (m + 1), 10**9+7
#
#     def dfs(start):
#         if dp[start]:
#             return dp[start]
#         if start == m:
#             return 1
#         if s[start] == '0':
#             return 0
#
#         count = 0
#
#         for end in range(start, m):
#             curr = s[start: end + 1]
#             if int(curr) > k:
#                 break
#             count += dfs(end + 1)
#         dp[start] = count % mod
#         return count
#     return dfs(0) % mod
#
# print(restore("1317", 2000))
# =======================================================================

# Smallest Number in Infinite Set

# import heapq
#
# class SmallestInfiniteSet:
#
#     def __init__(self):
#         self.container = list()
#         self.minNum = 1
#     def popSmallest(self) -> int:
#         if self.container:
#             return heapq.heappop(self.container)
#         self.minNum += 1
#         return self.minNum - 1
#     def addBack(self, num: int) -> None:
#         if num not in self.container and self.minNum > num:
#             heapq.heappush(self.container, num)
#
#     def show(self):
#         return self.container
#
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(1)
# obj.addBack(2)
# obj.addBack(3)
# obj.addBack(7)
# obj.addBack(2)
# print(obj.popSmallest())
# print(obj.show())

# =======================================================================
# Longest palindrome by concatenating
# from collections import Counter
#
# def longestPalindrome(words):
#     mp = Counter(words)
#     ans = 0
#     center = False
#
#     for word, count in mp.items():
#         if word[0] == word[1]:
#             if count % 2 == 0:
#                 ans += count
#             else:
#                 ans += count - 1
#                 center = True
#         elif word[0] < word[1]:
#             ans += 2 * min(count, mp[word[0] + word[1]])
#     if center:
#         ans += 1
#     return 2 * ans
#
# print(longestPalindrome(["lc","cl","gg"]))

# =======================================================================

# Task Scheduler

# from collections import Counter, deque
# import heapq
#
# def taskScheduler(tasks, n):
#     mp = Counter(tasks)
#     maxHeap = [-n for n in mp.values()]
#     heapq.heapify(maxHeap)
#
#     time = 0
#     q = deque()
#     while maxHeap or q:
#         time += 1
#
#         if maxHeap:
#             count = 1 + heapq.heappop(maxHeap)
#             if count:
#                 q.append([count, time + n])
#         if q and q[0][1] == time:
#             heapq.heappush(maxHeap, q.popleft()[0])
#     return time
#
# print(taskScheduler(["A","A","A","B","B","B"], 2))
# ============================================================================

# Search in 2d Matrix Part - 1

# def search(matrix, target):
#     if not matrix:
#         return False
#
    # rows, cols = len(matrix), len(matrix[0])
    # low, high = 0, rows * cols - 1
    #
    # while low <= high:
    #     mid = (low + high) // 2
    #     if matrix[mid // cols][mid % cols] == target:
    #         return True
    #     elif matrix[mid // cols][mid % cols] < target:
    #         low = mid + 1
    #     else:
    #         high = mid - 1
    #
    # return False
#
# print(search([[-10,-8,-6,-4,-3],[0,2,3,4,5],[8,9,10,10,12]], 0))

# Search in 2d Matrix Part - 2

# def search(matrix, target):
#     if not matrix: return
#
#     rows, cols = 0, len(matrix[0]) - 1
#
#     while rows < len(matrix) and cols >= 0:
#         if matrix[rows][cols] == target:
#             return True
#         if matrix[rows][cols] < target:
#             rows += 1
#         else:
#             cols -= 1
#
#     return False
#
# print(search([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20))

# ============================================================================

# Search in Rotated Sorted Array

# def searchRotated(nums, target):
#     if not nums: return
#
#     low, high = 0, len(nums) - 1
#
#     while low <= high:
#         mid = (low + high) // 2
#         if nums[mid] == target:
#             return low
#
#         if nums[low] <= nums[mid]:
#             if nums[low] <= target <= nums[mid]:
#                 high = mid - 1
#             else:
#                 low = mid + 1
#         else:
#             if nums[mid] <= target <= nums[high]:
#                 low = mid + 1
#             else:
#                 high = mid - 1
#     return -1
#
# print(searchRotated([4,5,6,7,0,1,2], 0))

# ============================================================================

# Determine the winner of the bowling game

# def bowling_winner(player1, player2):
#     scores = []; scr1, scr2 = 0, 0
#     for i in range(len(player1)):
#         scr1 = 2 * player1[i] if (i > 0 and player1[i - 1] == 10 or i > 1 and player1[i - 2] == 10) else player1[i]
#         scr2 = 2 * player2[i] if i > 0 and (player2[i - 1] == 10 or i > 1 and player2[i - 2] == 10) else player2[i]
#         scores.append(scr1 - scr2)
#     scrSum = sum(scores)
#     if scrSum > 0: return 1
#     if scrSum < 0: return 2
#     return 0
#
# print(bowling_winner([5, 6, 1, 10], [5, 1, 10, 5]))

# ============================================================================

# First Completely painted row or column

# def completelyPainted(arr, mat):
#     mpr, mpc, mprc, mpcc = {}, {}, {}, {}
#
#     for i in range(len(mat)):
#         for j in range(len(mat[0])):
#             mpr[mat[i][j]] = i
#             mpc[mat[i][j]] = j
#
#     for i in range(len(arr)):
#         n = arr[i]
#         mprc[mpr[n]] = mprc.get(mpr[n], 0) + 1
#         mpcc[mpc[n]] = mpcc.get(mpc[n], 0) + 1
#         if mprc[mpr[n]] == len(mat[0]) or mpcc[mpc[n]] == len(mat):
#             return i
#     return -1
#
# print(completelyPainted([1,3,4,2], [[1,4],[2,3]]))

# ============================================================================

# Subarray with given sum

# def subSum(arr, n, target):
#     l = 0
#     sum = 0
#     for r in range(n):
#         sum += arr[r]
#         while sum > target:
#             sum -= arr[l]
#             l += 1
#         if sum == target:
#             return [l + 1, r + 1]
#     return -1
#
# print(subSum([1,2,3,7,5], 5, 12))

# ============================================================================

# House Robber

# def hosueRobber(nums):
#     dp = [0] * len(nums)
#     dp[0], dp[1] = nums[0], max(nums[0], nums[1])
#     for i in range(2, len(nums)):
#         dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
#     return dp[-1]
#
#
# print(hosueRobber([1,2,3,1]))

# ============================================================================

# Operations to convert White Color to Black Color

# def operationsToConvert(blocks, k):
#     left, right = 0, 0
#     white = 0; res = 10**9
#     while right < len(blocks):
#         if blocks[right] == "W":
#             white += 1
#         elif right - left + 1 == k:
#             res = min(white, res)
#             if blocks[left] == "W":
#                 white -= 1
#             left += 1
#         right += 1
#     return res
#
# print(operationsToConvert('WBWBBBW', 2))

# def secondsToConvert(s):
#     seconds, zero = 0, 0
#     for char in s:
#         if char == "0":
#             zero += 1
#         if char == '1' and zero > 0:
#             seconds = max(seconds + 1, zero)
#     return seconds
#
# print(secondsToConvert('0110101'))

# ============================================================================

# Shifting Letters

# def shiftingLetters(s, shifts):
#     res = []
#     x = sum(shifts) % 26
#     for i, c in enumerate(s):
#         index = ord(c) - ord('a')
#         res.append(chr(ord('a') + (index + x) % 26))
#         x = (x - shifts[i]) % 26
#     return "".join(res)
#
#
# print(shiftingLetters("abc", [3,5,9]))

# def maximumProductSubArray(nums):
#     maxEle, minEle, res = nums[0], nums[0], nums[0]
#
#     for num in nums[1:]:
#         temp1 = max(num, maxEle * num, minEle * num)
#         temp2 = min(num, maxEle * num, minEle * num)
#         maxEle, minEle = temp1, temp2
#         res = max(res, maxEle)
#     return res
#
# print(maximumProductSubArray([2,3,-2,4]))

# def findDifference(nums1, nums2):
#     temp1 = list(set(nums1) - set(nums2))
#     temp2 = list(set(nums2) - set(nums1))
#     return [temp1, temp2]
#
# print(findDifference([1,2,3], [2,4,6]))

# ============================================================================

# 3Sum closest

# def threeSumClosest(nums, target):
#     nums.sort()
#     res = nums[0] + nums[1] + nums[2]
#     for i in range(len(nums)):
#         l, r = i + 1, len(nums) - 1
#         while l < r:
#             s = nums[i] + nums[l] + nums[r]
#             if abs(s - target) < abs(res - target):
#                 res = s
#             if s < target:
#                 l += 1
#             elif s > target:
#                 r -= 1
#             else:
#                 return res
#     return res
#
# print(threeSumClosest([5,2,7,5], 13))

# ============================================================================
# 3Sum

# def threeSum(nums):
#     nums.sort()
#     res = []
#     for i, num in enumerate(nums):
#         if i > 0 and num == nums[i - 1]:
#             continue
#         l, r = i + 1, len(nums) - 1
#         while l < r:
#             s = num + nums[l] + nums[r]
#             if s > 0:
#                 r -= 1
#             elif s < 0:
#                 l += 1
#             else:
#                 res.append([num, nums[l], nums[r]])
#                 l += 1
#                 while l < r and nums[l] == nums[l - 1]:
#                     l += 1
#
#     return res
#
# print(threeSum([-3,3,4,-3,1,2]))

# ============================================================================

# Dota2 Senator
from collections import deque

# def senator(senate):
#     n = len(senate); rad = deque(); dire = deque()
#     for i, char in enumerate(senate):
#         if char == "R":
#             rad.append(i)
#         else:
#             dire.append(i)
#
#     while rad and dire:
#         r, d = rad.popleft(), dire.popleft()
#         if r < d:
#             rad.append(n + r)
#         else:
#             dire.append(n + d)
#     return "Radiant" if len(rad) > len(dire) else "Dire"
#
# print(senator("DR"))

# ============================================================================

# Maximum Number of Vowels in a Substring of Given Length

# def maxVowels(s, k) -> int:
#     l = 0
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     res, count = 0, 0
#     for r in range(len(s)):
#         count += 1 if s[r] in vowels else 0
#         if r - l + 1 > k:
#             print(r, l)
#             count -= 1 if s[l] in vowels else 0
#             l += 1
#         res = max(res, count)
#     return res
#
# print(maxVowels('abciiidef', 3))

# ============================================================================
# Number of Subsequences That Satisfy the Given Sum Condition

# def subsequencesSum(nums, target):
#     nums.sort()
#     l, r = 0, len(nums) - 1
#     res = 0; mod = 10 ** 9 + 7
#     while l <= r:
#         if nums[l] + nums[r] > target:
#             r -= 1
#         else:
#             res += pow(2, r - l, mod)
#             l += 1
#     return res % mod
#
# print(subsequencesSum([3,5,6,7], 9))

# ============================================================================

# Permutations

# def permutations(nums):
#     nums.sort()
#     res = []; mp = {}
#     for i in range(len(nums)):
#         mp[i] = 0
#
#     def solve(nums, visit, temp, res):
#         if len(temp) == len(nums):
#             res.append(list(temp))
#             return
#         for i in range(len(nums)):
#             # if i > 0 and nums[i] == nums[i - 1]:
#             #     continue
#             if not visit[i]:
#                 visit[i] = 1
#                 temp.append(nums[i])
#                 solve(nums, visit, temp, res)
#                 temp.pop()
#                 visit[i] = 0
#     solve(nums, mp, [], res)
#     return res
#
# print(permutations([1,1,2]))\

# Permutations with swapping

# def permutate(nums):
#     nums.sort()
#     res = []
#     mp = {}
#     for i in range(len(nums)):
#         mp[i] = 0
#
#     def solve(nums, visit, temp, ans):
#         if len(temp) == len(nums):
#             ans.append(list(temp))
#             return
#         for i in range(len(nums)):
#             if visit[i]: continue
#             if i > 0 and nums[i] == nums[i - 1] and not visit[i - 1]: continue
#             visit[i] = 1
#             temp.append(nums[i])
#             solve(nums, visit, temp, ans)
#             visit[i] = 0
#             temp.pop()
#     solve(nums, mp, [], res)
#     return res
#
#
# print(permutate([1,1,2]))


# def distinctDiff(nums):
#     prefix = [0] * len(nums)
#     suffix = [0] * len(nums)
#     prefix[0] = 1
#     for i in range(1, len(nums)):
#         prefix[i] = len(set(nums[:i+1]))
#     for i in range(len(nums) - 1):
#         suffix[i] = len(set(nums[i + 1: ]))
#
#     return [prefix[i] - suffix[i] for i in range(len(nums))]
#
# print(distinctDiff([3,2,3,4,2]))

# ==========================================================================
# Frequency Tracker

# from collections import defaultdict
# class FrequencyTracker:
#
#     def __init__(self):
#         self.cnter = defaultdict(int)
#         self.freq = defaultdict(int)
#
#     def add(self, number: int) -> None:
#         self.cnter[number] += 1
#         cnt = self.cnter[number]
#         self.freq[cnt] += 1
#         self.freq[cnt-1] -= 1
#
#     def deleteOne(self, number: int) -> None:
#         if self.cnter[number]:
#             self.cnter[number] -= 1
#             cnt = self.cnter[number]
#             self.freq[cnt] += 1
#             self.freq[cnt+1] -= 1
#
#     def hasFrequency(self, frequency: int) -> bool:
#         return True if self.freq[frequency] else False
#
#
# obj = FrequencyTracker()
#
# obj.add(3)
# obj.add(3)
# print(obj.hasFrequency(2))
# ==========================================================================

# Number of Adjacent Elements With the Same Color

# def sameColor(n, queries):
#     nums, c = [0] * n, 0
#     for i, color in queries:
#         pre, nex = nums[i - 1] if i > 0 else 0, nums[i + 1] if i < n - 1 else 0
#         if nums[i] and nums[i] == pre: c -= 1
#         if nums[i] and nums[i] == nex: c -= 1
#         nums[i] = color
#         if nums[i] == pre: c += 1
#         if nums[i] == nex: c += 1
#         yield c
#
# sameColor(4, [[0,2],[1,2],[3,1],[1,1],[2,1]])

# ==========================================================================

#  Make Costs of Paths Equal in a Binary Tree
# def minIncrements(n: int, cost: List[int]) -> int:
#     res = 0
#     def dfs(i, res):
#         if i >= len(cost): return 0
#         a, b = dfs(2 * i + 1, res), dfs(2 * i + 2, res)
#         res += abs(a - b)
#         return cost[i] + max(a, b)
#     dfs(0, res)
#     return res
#
# print(minIncrements(7, [1,5,2,2,3,3,1]))

# ==========================================================================

# Diagonal Sum
# def diagonalSum(mat: List[List[int]]) -> int:
#     res = 0
#     for i in range(len(mat)):
#         res += mat[i][i]
#         res += mat[i][-1-i]
#     return res - mat[len(mat)//2][len(mat)//2] if len(mat) % 2 != 0 else res
#
# mat = [[1,1,1,1],
#        [1,1,1,1],
#        [1,1,1,1],
#        [1,1,1,1]]
#
# print(diagonalSum(mat))

# ==========================================================================
# Interval Questions

# def insertIntervals(intervals, newInterval):
#     if not intervals: return [newInterval]
#
#     merge = False
#     temp = []
#
#     for interval in intervals:
#         if not merge and newInterval[0] < interval[0]:
#             temp.append(newInterval)
#         temp.append(interval)
#
#     if not merge:
#         temp.append(newInterval)
#
#     res = []
#     for interval in temp:
#         if res and interval[0] <= res[-1][-1]:
#             res[-1][-1] = max(interval[1], res[-1][-1])
#         else:
#             res += [interval]
#     return res
#
# print(insertIntervals([[1,3],[6,9]], [2,5]))

# ==========================================================================
# Merge Intervals

# def mergeIntervals(intervals):
#     intervals.sort(key=lambda x: x[0])
#     merged = []
#     for interval in intervals:
#         if not merged or merged[-1][-1] < interval[0]:
#             merged.append(interval)
#         else:
#             merged[-1][-1] = max(merged[-1][-1], interval[-1])
#
#     return merged
#
# # n = int(input())
# # nums = []
# # for _ in range(n):
# #     a, b = [int(num) for num in input().split(" ")]
# #     nums.append([a, b])
#
# # print(nums)
# print(mergeIntervals([[1,3],[2,6],[8,10],[15,18]]))

# # ==========================================================================

# # Teemo's Attack

# def teemoAttack(timeSeries, duration):
#     n, out = len(timeSeries), 0
#     if not n: return 0
#     for i in range(n - 1):
#         out += min(timeSeries[i + 1] - timeSeries[i], duration)
#     return out + duration
#
#
# print(teemoAttack([1,2], 2))

# # ==========================================================================

# # Spiral Matrix

# def spiralOrder(matrix):
#     if not matrix: return []
#     res = []
#     rows, cols = len(matrix), len(matrix[0])
#     top, left = 0, 0
#     bottom, right = rows - 1, cols - 1
#     while top <= bottom and left <= right:
#         for i in range(left, right + 1):
#             res.append(matrix[top][i])
#         top += 1
#
#         for i in range(top, bottom + 1):
#             res.append(matrix[i][right])
#         right -= 1
#
#         if top <= bottom:
#             for i in range(right, left - 1, - 1):
#                 res.append(matrix[bottom][i])
#             bottom -= 1
#
#         if left <= right:
#             for i in range(bottom, top - 1, -1):
#                 res.append(matrix[i][left])
#             left += 1
#     return res
#
# print(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))

# # Spiral Matrix 2

# def spiralMatrix(n):
#     temp = [[0] * n for _ in range(n)]
#     x, y, dx, dy = 0, 0, 0, 1
#     for k in range(n * n):
#         temp[x][y] = k + 1
#         if temp[(x + dx) % n][(y + dy) % n]:
#             dx, dy = dy, -dx
#         x += dx
#         y += dy
#     return temp
#
#
# print(spiralMatrix(3))

# # ==========================================================================

# # Solving Questions With Brainpower

# def solvingQuestions(questions):
#     n = len(questions)
#     dp = [0] * n
#     def dfs(i):
#         if i >= n:
#             return 0
#         if dp[i]:
#             return dp[i]
#         points, skip = questions[i]
#         dp[i] = max(dfs(i + 1), dfs(i + 1 + skip) + points)
#         return dp[i]
#     return dfs(0)
#
# print(solvingQuestions([[3,2],[4,3],[4,4],[2,5]]))

# # ==========================================================================

# # Number of Provinces

# def numberOfProvinces(isConnected):
#     n = len(isConnected)
#     seen = set()
#     res = 0
#     def dfs(node):
#         for ver, adj in enumerate(isConnected[node]):
#             if adj and ver not in seen:
#                 seen.add(ver)
#                 dfs(ver)
#
#     for vertex in range(n):
#         if vertex not in seen:
#             dfs(vertex)
#             res += 1
#     return res
#
#
# print(numberOfProvinces([[1,1,0],[1,1,0],[0,1,1]]))

# # ==========================================================================

# # Minimum consecutive cards to pickup

# def consecutiveCards(cards):
#     mp = dict()
#     res = 999999999999
#     for i, card in enumerate(cards):
#         if card in mp and i - mp[card] + 1 < res: res = i - mp[card] + 1
#         mp[card] = i
#     if res == 999999999999: return -1
#     return res
#
#
# print(consecutiveCards([3, 4, 2, 3, 4, 7]))

# # ==========================================================================

# # Remove digit from String Number to maximize the result

# def maximizeStringResult(s, digit):
#     res = -1
#     for i, num in enumerate(s):
#         if s[i] == digit:
#             res = max(res, int(s[:i] + s[i + 1:]))
#     return str(res)
#
# print(maximizeStringResult('1231', '1'))

# # ==========================================================================

# # Instersection of multiple arrays

# def arrayInstersections(nums):
#     mp = dict(); res = []
#     for num in nums:
#         for i in num:
#             if i in mp:
#                 mp[i] += 1
#             else:
#                 mp[i] = 1
#     for i, k in mp.items():
#         if k == len(nums):
#             res.append(i)
#     return res
#
# print(arrayInstersections([[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]))

# # ==========================================================================

# # Find the Losers of the Circular Game
# import math
# def findLosers(n, k):
#     seen = [False] * n
#     res = []
#     i = 1; idx = 0
#     while not seen[i - 1]:
#         seen[i - 1] = True
#         idx += k
#         i = (i + idx) % n
#         if i == 0:
#             i = n
#
#     for i in range(n):
#         if not seen[i]:
#             res.append(i+1)
#
#     return sorted(res)
#
#
# print(findLosers(5, 2))

# # ==========================================================================

# # Neighbouring bitwise XOR

# def neighbouringXOR(derived):
#     toggle = 0
#     for bit in derived:
#         if bit == 1: toggle = (toggle + 1) % 2
#     return toggle == 0
#
# print(neighbouringXOR([0, 0]))

# # ==========================================================================

# # Removing Duplicates fron the Sorted Array - 2

# def removeDuplicates(nums):
#     # i = 0
#     # for num in nums:
#     #     if i < 2 or num > nums[i - 2]:
#     #         nums[i] = num
#     #         i += 1
#     # return i
#
#     tort = 2; hare = 2
#     while hare < len(nums):
#         if nums[tort - 2] != nums[hare]:
#             nums[tort] = nums[hare]
#             tort += 1
#         hare += 1
#     return tort
#
# print(removeDuplicates(nums=[0,0,1,1,1,1,2,3,3]))
# # ==========================================================================

# # Reverse the words in string

# def reverseStrings(s):
#     words = s.split(" ")
#     new_words = []
#     for word in words:
#         if not word: continue
#         else:
#             new_words.append(word)
#     return " ".join(new_words[::-1])
#
#
# print(reverseStrings("hello  world"))

# # ==========================================================================
# Longest palindromic substring
# def longestPalindromicSubstr(s):
#     res = ''
#     max_len = 0
#     for i in range(len(s)):
#         l, r = i, i
#         while l >= 0 and r < len(s) and s[l] == s[r]:
#             if (r - l + 1) > max_len:
#                 res = s[l:r + 1]
#                 max_len = r - l + 1
#             l -= 1
#             r += 1
#
#         l, r, = i, i + 1
#         while l >= 0 and r < len(s) and s[l] == s[r]:
#             if (r - l + 1) > max_len:
#                 res = s[l:r + 1]
#                 max_len = r - l + 1
#             l -= 1
#             r += 1
#
#     return res
#
# print(longestPalindromicSubstr("babbad"))