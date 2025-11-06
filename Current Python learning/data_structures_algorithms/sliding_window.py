from collections import defaultdict, deque
# Maximum sum of subarray

# def maxSumSubarray(nums, k):
#     if not nums: return 0
#     maxSum = sum(nums[:k])
#     curr = maxSum
#     for i in range(k, len(nums)):
#         curr = curr - nums[i - k] + nums[i]
#         maxSum = max(maxSum, curr)
#     return maxSum
#
#
# print(maxSumSubarray([2, 1, 5, 1, 3, 2], 2))

# ================================================================================================================================
# Smallest sum subarray

# def smallestSum(nums, s):
#     minLen = float('inf')
#     curr, l = 0, 0
#     for r in range(len(nums)):
#         curr += nums[r]
#         while curr >= s:
#             minLen = min(minLen, r - l + 1)
#             curr -= nums[l]
#             l += 1
#     return minLen if minLen != float('inf') else 0
#
#
# print(smallestSum([2, 1, 5, 2, 3, 2], 7))

# ================================================================================================================================
# K Sized Subarray Maximum

# def maxSubarray(arr, n, k):
#     if n * k == 0: return []
#     if k == 1: return arr
#     q = deque()
#     maxIdx = 0
#     for i in range(k):
#         while q and arr[i] > arr[q[-1]]:
#             q.pop()
#         q.append(i)
#         if arr[i] > arr[maxIdx]: maxIdx = i
#     res = [arr[maxIdx]]
#
#     for i in range(k, n):
#         while q and q[0] <= i - k:
#             q.popleft()
#         while q and arr[i] > arr[q[-1]]:
#             q.pop()
#         q.append(i)
#         res.append(arr[q[0]])
#     return res
#
#
# print(maxSubarray([1 ,2 ,3 ,1 ,4 ,5 ,2,3,6], 9,3))

# ================================================================================================================================
# Longest subarray with sum k
# uses two pointer -> one pointer l for shrinking; one pointer r for expanding;
# conditional check using while where current sum is greater than k then shrink the window from left.
# update max length when current sum is less than or equal to k and keep expanding.
# Time complexity - O(N + N) where one N is expanding and other is shrinking
# Space complexity - O(1)

# import time
# import random
# def longestSubarray(nums, k):
#     l, r = 0, 0
#     maxLen = 0; curr = 0
#     # res = []
#     start = time.time()
#     while r < len(nums):
#         curr += nums[r]
#         if curr > k:
#             curr -= nums[l]
#             l += 1
#         if curr <= k:
#             maxLen = max(maxLen, r - l + 1)
#             # res.append(nums[l:r+1])
#         r += 1
#     end = time.time()
#     elap = end - start
#     return maxLen, f"{elap:.10f}"
#
# print(longestSubarray([random.randint(1, 1000) for _ in range(1000)], 14))

# ================================================================================================================================
# Maximum points you can obtain from cards

# There are several cards arranged in a row, and each card has an associated number of points.
# The points are given in the integer array cardPoints.
#
# In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.
#
# Your score is the sum of the points of the cards you have taken.
#
# Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

# take leftsum till subarray of size k
# remove each element from left and add one element from right and calculate the maximum sum

# def maximumPoints(cardPoints, k):
#     lsum = 0; rsum = 0; maxSum = 0
#     for i in range(k - 1):
#         lsum += cardPoints[i]
#     maxSum = lsum
#
#     for i in range(k - 1, -1, -1):
#         lsum -= cardPoints[i]
#         rsum += cardPoints[i]
#         maxSum = max(maxSum, lsum + rsum)
#     return maxSum
#
# print(maximumPoints([1,2,3,4,5,6,1], 3))

# ================================================================================================================================

# Longest subarray with atmost k distinct characters

# Take 2 pointers l, r and a hash map for keep a count on unique characters
# Expand window from r
# check if the rth character is in map and then remove the count or pop out the element based
# calculate the maximum length

# def longestSubarrayWithKDistinctCharacters(s, k):
#     l, r = 0, 0
#     mp = dict()
#     maxLen = 0
#     while r < len(s):
#         mp[s[r]] = mp.get(s[r], 0) + 1
#         if len(mp) > k:
#             mp[s[l]] -= 1
#             if mp[s[l]] == 0: mp.pop(s[l])
#             l += 1
#         if len(mp) <= k:
#             maxLen = max(maxLen, r - l + 1)
#         r += 1
#     return maxLen
#
#
# print(longestSubarrayWithKDistinctCharacters("aaabbccd", 2))
