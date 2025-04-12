# ================================================================================================================================
# Find all pairs with a given sum
import math

# Given two unsorted arrays A of size N and B of size M of distinct elements,
# the task is to find all pairs from both arrays whose sum is equal to X.

# def findAllPairs(A, B, N, M, X):
#     B = set(B)
#     A.sort()
#     pairs = []
#     for num in A:
#         if (X - num) in B: pairs.append([num, X - num])
#     pairs.sort(key=lambda x: x[0])
#     return pairs
#
# print(findAllPairs([1, 2, 4, 5, 7], [5, 6, 3, 4, 8], 5, 5, 9))

# ================================================================================================================================
# Minimize the sum of product

# You are given two arrays, A and B, of equal size N. The task is to find the minimum value
# of A[0] * B[0] + A[1] * B[1] + .... + A[N-1] * B[N-1], where shuffling of elements of arrays A and B is allowed.

# def minimumSumProduct(A, B, N):
#     A.sort(); B.sort(reverse=True)
#     res = 0
#     for i in range(N):
#         res += (A[i] * B[i])
#     return res
#
# print(minimumSumProduct([3,1,1], [6,5,4], 3))

# ================================================================================================================================
# Convert the array in Zig-Zag fashion

# Given an array arr of distinct elements of size n, the task is to rearrange the
# elements of the array in a zig-zag fashion so that the converted array should be in the below form:
#
# arr[0] < arr[1]  > arr[2] < arr[3] > arr[4] < . . . . arr[n-2] < arr[n-1] > arr[n].
#
# Note: Modify the given arr[] only, If your transformation is correct, the output will be 1 else the output will be 0.
# Every even indexed element should be less than the odd and every odd indexed element should be greater than even indexed element

# def zigZag(n, arr):
#     for i in range(n - 1):
#         if (i % 2 == 0 and arr[i] > arr[i + 1]) or (i % 2 != 0 and arr[i] < arr[i + 1]):
#             arr[i], arr[i + 1] = arr[i + 1], arr[i]
#         return arr
#
# print(zigZag(7, [4, 3, 7, 8, 6, 2, 1]))

# ================================================================================================================================
# Minimum Jumps

# Given an array arr[] of size n of non-negative integers. Each array element represents the maximum length
# of the jumps that can be made forward from that element. This means if arr[i] = x, then we can
# jump any distance y such that y ≤ x.
# Find the minimum number of jumps to reach the end of the array starting from the first element.
# If an element is 0, then you cannot move through that element.
# Note:  Return -1 if you can't reach the end of the array.

# def minJumps(nums, n):
#     if n <= 1: return -1
#     if nums[0] == 0: return 0
#
#     max_index, steps, jumps = nums[0], nums[0], 1
#
#     for i in range(1, n):
#         if i == n - 1: return jumps
#         max_index = max(max_index, i + nums[i])
#         steps -= 1
#         if steps == 0:
#             jumps += 1
#             if i >= max_index: return -1
#             steps = max_index - i
#     return -1
#
# print(minJumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9], 11))

# ================================================================================================================================
# Minimize the Heights

# Given an array arr[] denoting heights of N towers and a positive integer K.
#
# For each tower, you must perform exactly one of the following operations exactly once.
#
# Increase the height of the tower by K
# Decrease the height of the tower by K
# Find out the minimum possible difference between the height of the shortest and tallest
# towers after you have modified each tower.

# def minimizeHeights(arr, n, k):
#     arr.sort()
#     currMin, currMax = arr[0], arr[n - 1]
#     res = currMax - currMin
#     for i in range(1, n):
#         if arr[i] <= k: continue
#         currMin = min(arr[0] + k, arr[i] - k)
#         currMax = max(arr[n - 1] - k, arr[i - 1] + k)
#         res = min(res, currMax - currMin)
#     return res
#
# print(minimizeHeights([1,5,8,10], 4, 2))

# ================================================================================================================================
# Indexes of unsorted array

# def findIndexes(arr, n, target):
#     if not arr or not target: return -1
#     l, curr = 0, 0
#     for r in range(n):
#         curr += arr[r]
#         while curr > target:
#             curr -= arr[l]
#             l += 1
#         if curr == target: return [l + 1, r + 1]
#     return -1
#
# print(findIndexes([1,0], 2, 1))

# ================================================================================================================================
# Zero sum subarrays
# You are given an array arr[] of size n. Find the total count of sub-arrays having their sum equal to 0.
#
# Examples:
#
# Input: n = 6, arr[] = {0,0,5,5,0,0}
# Output: 6
# Explanation: The 6 subarrays are [0], [0], [0], [0], [0,0], and [0,0].

# def zeroSumSubarrays(nums):
#     mp = dict()
#     cum_sum, count = 0,0
#     for num in nums:
#         cum_sum += num
#         if not cum_sum:
#             count += 1
#         if cum_sum in mp:
#             count += mp[cum_sum]
#
#         if cum_sum in mp:
#             mp[cum_sum] += 1
#         else:
#             mp[cum_sum] = 1
#     return count
#
# print(zeroSumSubarrays([0,0,5,5,0,0]))

# ================================================================================================================================
# Rearrange the elements in the array
# Given a sorted array of positive integers. Your task is to rearrange the array elements
# alternatively i.e first element should be max value, second should be min value, third should be second max,
# fourth should be second min and so on.
# Note: Modify the original array itself. Do it without using any extra space. You do not have to return anything.
#
# Example 1:
#
# Input:
# n = 6
# arr[] = {1,2,3,4,5,6}
# Output: 6 1 5 2 4 3
# Explanation: Max element = 6, min = 1,
# second max = 5, second min = 2, and
# so on... Modified array is : 6 1 5 2 4 3.

# def rearrangeElements(nums):
#     nums.sort()
#     l, r = 0, len(nums) - 1
#     outterMax = nums[-1] + 1
#     for i in range(len(nums)):
#         if i % 2 == 0:
#             nums[i] += (nums[r] % outterMax) * outterMax
#             r -= 1
#         elif i % 2 != 0:
#             nums[i] += (nums[l] % outterMax) * outterMax
#             l += 1
#
#     for i in range(len(nums)):
#         nums[i] //= outterMax
#
#     return nums
#
# print(rearrangeElements([10,20,30,40,50,60,70,80,90,100,110]))

# ================================================================================================================================
# kth element of two arrays

# Given two sorted arrays arr1 and arr2 of size N and M respectively and an element K. The task is to
# find the element that would be at the kth position of the final sorted array.
#
# Example 1:
#
# Input:
# arr1[] = {2, 3, 6, 7, 9}
# arr2[] = {1, 4, 8, 10}
# k = 5
# Output:
# 6
# Explanation:
# The final sorted array would be -
# 1, 2, 3, 4, 6, 7, 8, 9, 10
# The 5th element of this array is 6.

# def kthElement(arr1, arr2, t):
#     res = [0] * (len(arr1) + len(arr2))
#     i, j, k = [0] * 3
#     while i < len(arr1) and j < len(arr2):
#         if arr1[i] <= arr2[j]:
#             res[k] = arr1[i]
#             i += 1
#         else:
#             res[k] = arr2[j]
#             j += 1
#         k += 1
#
#     while i < len(arr1):
#         res[k] = arr1[i]
#         i += 1
#         k += 1
#
#     while j < len(arr2):
#         res[k] = arr2[j]
#         j += 1
#         k += 1
#     return res[t - 1]
#
# print(kthElement([2, 3, 6, 7, 9], [1, 4, 8, 10], 5))

# ================================================================================================================================
# Given an array of strings arr[] of length n representing non-negative integers, arrange them in a manner,
# such that, after concatenating them in order, it results in the largest possible number. Since the result
# may be very large, return it as a string.
#
# Examples:
#
# Input: n = 5, arr[] =  {"3", "30", "34", "5", "9"}
# Output: "9534330"
# Explanation: Given numbers are  {"3", "30", "34", "5", "9"}, the arrangement "9534330" gives the largest value.
# The idea is to use comparison based algorithm
# There are two approaches in solving this problem by using inbuilt comparing algorithm from functools
# or we can use an anonymous function which maintains the order of the string by multiplying them with 10

# from functools import cmp_to_key
#
# def largestArrangement(arr):
#     def comp(a, b):
#         return -1 if a + b > b + a else 1
#
#     arr = sorted(arr, key=cmp_to_key(comp))
#     return "".join(arr)
#
#
# print(largestArrangement(["3", "30", "34", "5", "9"]))

# ================================================================================================================================
# Given an array of n distinct elements. Find the minimum number of swaps required to sort the array in strictly increasing order.
#
# Example 1:
#
# Input:
# nums = {2, 8, 5, 4}
# Output:
# 1
# Explanation:
# swap 8 with 4.
# To find the minimum number of swaps we first need to store all the original elements indexes then sort them based on elements
# increasing order then we need to visit the index for element and jump from that element to other element where a cycle forms
# increment the cycle count and if cycle count is greater than 1 then swaps would be cycle - 1

# def minSwaps(nums):
#     curr_pos = [(nums[i], i) for i in range(len(nums))]
#     curr_pos.sort(key=lambda x: x[0])
#
#     swaps, cycle, visited = 0, 0, [False] * len(nums)
#
#     for i in range(len(nums)):
#         if visited[i] or curr_pos[i][1] == i: continue
#
#         j = i
#         cycle = 0
#         while not visited[j]:
#             visited[j] = True
#             j = curr_pos[j][1]
#             cycle += 1
#
#         if cycle > 0: swaps += (cycle - 1)
#     return swaps
#
# print(minSwaps([10, 19, 6, 3, 5]))

# ================================================================================================================================
# Stock Span Problem

# def stockSpan(nums):
#     n = len(nums)
#     span, stack = [0] * n, []
#
#     for i in range(n):
#         while stack and nums[stack[-1]] <= nums[i]: stack.pop()
#         if not stack: span[i] = i + 1
#         else: span[i] = i - stack[-1]
#         stack.append(i)
#     return span
#
# print(stockSpan([100, 80, 60, 70, 60, 75, 85]))

# ================================================================================================================================
# Swapping pairs to make sum equal

# Given two arrays of integers a[] and b[] of size n and m, the task is to check if a pair of values (one value from each array)
# exists such that swapping the elements of the pair will make the sum of two arrays equal.
#
# Note: Return 1 if there exists any such pair otherwise return -1.
#
# Example 1:
#
# Input: n = 6, m = 4, a[] = {4, 1, 2, 1, 1, 2}, b[] = (3, 6, 3, 3)
# Output: 1
# Explanation: Sum of elements in a[] = 11, Sum of elements in b[] = 15, To get same sum from both arrays,
# we can swap following values: 1 from a[] and 3 from b[]

# Explanation
# Given 2 arrays with elements we need to swap elements from both the arrays such that sum of array1 and sum of array2 are equal
# Swap1 => sum(a) - a[i] + b[j] i.e you are removing an element from a and replacing it with element from b
# Swap2 => sum(b) - b[j] + a[i] i.e you are removing an element from b and replacing it with element from a
# Finally checking if both of the swap results are equal swap1 == swap2
# or simply make a hash of array b
# check from the above swap1 and swap2 equation we derive equation b - a = (sumA - sumB) // 2

# def swapPairs(a, b):
#     sumA, sumB = sum(a), sum(b)
#     diff = sumA - sumB
#     if diff % 2 != 0: return -1
#
#     target = diff // 2
#     seenB = set(b)
#     for num in a:
#         if num - target in seenB: return 1
#     return -1
#
# print(swapPairs([4, 1, 2, 1, 1, 2], [3, 6, 3, 3]))

# ================================================================================================================================
# Find element that appears once in sorted array

# Given a sorted array arr[] of size N. Find the element that appears only once in the array. All other elements
# appear exactly twice.
#
# Example 1:
#
# Input:
# N = 11
# arr[] = {1, 1, 2, 2, 3, 3, 4, 50, 50, 65, 65}
# Output: 4
# Explanation: 4 is the only element that
# appears exactly once.
# Use binary search and find for the even indexes where the element is occurring once

# def findElement(arr):
#     n = len(arr)
#     l, h = 0, n - 1
#     while l < h:
#         mid = (l + h) // 2
#
#         if mid % 2 != 0: mid -= 1
#         if arr[mid] == arr[mid + 1]: l = mid + 2
#         else: h = mid
#     return arr[l]
# 
#
# print(findElement([1, 1, 2, 2, 3, 3, 4, 50, 50, 65, 65]))

# def findSingleElement(arr):
#     xor = arr[0]
#     for num in arr[1:]:
#         xor ^= num
#     return xor
#
# print(findSingleElement([1, 1, 2, 2, 3, 3, 4, 50, 50, 65, 65]))

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
#     r = len(cardPoints) - 1
#     for i in range(k - 1, -1, -1):
#         lsum -= cardPoints[i]
#         rsum += cardPoints[r]
#         maxSum = max(maxSum, lsum + rsum)
#         r -= 1
#     return maxSum
#
# print(maximumPoints([1,2,3,4,5,6,1], 3))

# ================================================================================================================================
# Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest
# substring without repeating characters.
#
# Example 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# def longestSubstring(s):
#     seen = set(); l = 0; maxLen = 0
#     for r in range(len(s)):
#         while s[r] in seen:
#             seen.remove(s[l])
#             l += 1
#         seen.add(s[r])
#         maxLen = max(maxLen, r - l + 1)
#     return maxLen
#
# print(longestSubstring("cadbzabcd"))

# ================================================================================================================================
# Given a binary array arr of size N and an integer M. Find the maximum number of consecutive 1's produced
# by flipping at most M 0's.
#
# Example 1:
#
# Input:
# N = 3
# arr[] = {1, 0, 1}
# M = 1
# Output:
# 3
# Explanation:
# Maximum subarray is of size 3
# which can be made subarray of all 1 after
# flipping one zero to 1.
# Instead of flipping we simply consider the zero to be a one. Now when we encounter zero we increment zero count. When count of
# zeros exceeds k then shrink the window from left making zeros count at-most k and update the maximum length.

# def maxConsecutiveOnes(nums, k):
#     # The below approach has TC - O(N.k)
#     # l = 0; maxlen = 0; zeros = 0
#     # for r in range(len(nums)):
#     #     if nums[r] == 0: zeros += 1
#     #     while zeros > k:
#     #         if nums[l] == 0: zeros -= 1
#     #         l += 1
#     #     maxlen = max(maxlen, r - l + 1)
#     # return maxlen
#
#     # To reduce the TC to O(N)
#     l = 0; zeros = 0; maxlen = 0
#     for r in range(len(nums)):
#         if nums[r] == 0: zeros += 1
#         if zeros > k:
#             if nums[l] == 0: zeros -= 1
#             l += 1
#         else:
#             maxlen = max(maxlen, r - l + 1)
#     return maxlen
#
# print(maxConsecutiveOnes([1,1,1,0,0,0,1,0,0,1,0,0,0,1,0,1,1,1,1,1,0,0], 3))

# ================================================================================================================================
# Fruits into Baskets

# You only have two baskets, and each basket can only hold a single type of fruit. There is no limit
# on the amount of fruit each basket can hold.
# Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree)
# while moving to the right. The picked fruits must fit in one of the baskets.
# Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
# Explanation - we can use a hashmap to store the element with its frequency.
# Move forward in the array to search for another distinct element if the length of hashmap is more than 2 then start
# shrinking the array from the left

# def fruitsIntoBasket(fruits):
#     # mp = dict(); maxlen = 0; l = 0
#     # for r in range(len(fruits)):
#     #     mp[fruits[r]] = mp.get(fruits[r], 0) + 1
#     #     while len(mp) > 2:
#     #         mp[fruits[l]] -= 1
#     #         if mp[fruits[l]] == 0: mp.pop(fruits[l])
#     #         l += 1
#     #     if len(mp) <= 2:
#     #         maxlen = max(maxlen, r - l + 1)
#     # return maxlen
#
#     mp = dict(); maxlen = 0; l = 0
#     for r in range(len(fruits)):
#         mp[fruits[r]] = mp.get(fruits[r], 0) + 1
#         if len(mp) > 2:
#             mp[fruits[l]] -= 1
#             if mp[fruits[l]] == 0: mp.pop(fruits[l])
#             l += 1
#         if len(mp) <= 2:
#             maxlen = max(maxlen, r - l + 1)
#     return maxlen
#
#
# print(fruitsIntoBasket([3, 1, 2, 2, 2, 2]))

# ================================================================================================================================
# Longest Substring With At Most K Distinct Characters

# Given a string you need to print the size of the longest possible substring that has exactly K unique characters.
# If there is no possible substring then print -1.

# def longestSubstring(s, k):
#     mp = dict(); l = 0; maxlen = 0
#     for r in range(len(s)):
#         mp[s[r]] = mp.get(s[r], 0) + 1
#         while len(mp) > k:
#             mp[s[l]] -= 1
#             if mp[s[l]] == 0: mp.pop(s[l])
#             l += 1
#         if len(mp) == k:
#             maxlen = max(maxlen, r - l + 1)
#     return maxlen
#
# print(longestSubstring("aabacbebebe", 5))

# ================================================================================================================================
# Number of substrings containing three distinct characters

# For each character we can obtain a substring which consists of a,b,c characters.
# When including the character we check from the left whether there is a substring that ends with the current character.
# as inclusion of previous characters counts as seen take the current index to increment the count.

# def numberOfSubstrings(s):
#     lastSeen = [-1] * 3; count = 0
#     for r in range(len(s)):
#         lastSeen[ord(s[r]) - ord('a')] = r
#         if lastSeen[0] != -1 and lastSeen[1] != -1 and lastSeen[2] != -1: count += min(lastSeen) + 1
#     return count
#
# print(numberOfSubstrings("abcabc"))

# ================================================================================================================================
# Longest repeating character replacement

# Generate all the possible substrings. from l we shrink the window and from r we increase the window size
# check for possible conversion of characters. use max freq of occurring character and subtract from total length of window
# shrink if ( length of window - max freq of character ), update the max length of the window

# def longestRepeatingCharacter(s, k):
#     maxfreq = 0; mp = dict(); l = 0; maxlen = 0
#     for r in range(len(s)):
#         mp[s[r]] = mp.get(s[r], 0) + 1
#         maxfreq = max(maxfreq, mp[s[r]])
#         while (r - l + 1) - maxfreq > k:
#             mp[s[l]] -= 1
#             l += 1
#         maxlen = max(maxlen, r - l + 1)
#     return maxlen
#
# print(longestRepeatingCharacter("AABABBA", 1))

# ================================================================================================================================
# Binary Subarrays With Sum

# For every count subarray or substring problem we always (solve count subarrays <= k) - (solve count subarrays <= k - 1)
# using the longest window concept we increment the count based on the length of the subarray

# def binarySubarraySum(nums, k):
#     def solve(nums, k):
#         maxCount = 0; l = 0; curr = 0
#         for r in range(len(nums)):
#             curr += nums[r]
#             while curr > k:
#                 curr -= nums[l]
#                 l += 1
#             maxCount += (r - l + 1)
#         return maxCount
#     return solve(nums, k) - solve(nums, k - 1)
#
# print(binarySubarraySum([0,0,0,0,0], 0))

# ================================================================================================================================
# Count of nice subarrays

# A nice subarray is defined as the subarray containing k odd integers in it.
# every count subarray problem solve(nums, k) - solve(nums, k - 1)
# use a count to check if its odd or even integer
# when count > k
# remove each element from left and update l pointer
# update the maxCount variable

# def countNiceSubarrays(nums, k):
#     def solve(nums, k):
#         if k < 0: return 0
#         maxCount = 0; l = 0; count = 0
#         for r in range(len(nums)):
#             count += nums[r] % 2
#             while count > k:
#                 count -= nums[l] % 2
#                 l += 1
#             maxCount = (r - l + 1)
#         return maxCount
#     return solve(nums, k) - solve(nums, k - 1)
#
# print(countNiceSubarrays([1,1,2,1,1], 2))

# ================================================================================================================================
# Find the number of subarrays having even sum

# def countSubarraysWithEvenSum(nums):
#     even, currEven, currOdd = 0, 1, 0
#     prefix = 0
#     for num in nums:
#         prefix += num
#         if prefix % 2:
#             even += currOdd
#             currOdd += 1
#         else:
#             even += currEven
#             currEven += 1
#
#     return even
#
# print(countSubarraysWithEvenSum([1, 3, 1, 1]))

# ================================================================================================================================
# Subarray with k different integers

# def subarrayIntegers(nums, k):
#     def solve(nums, k):
#         if k < 0: return 0
#         mp = dict(); l = 0; maxCount = 0
#         for r in range(len(nums)):
#             mp[nums[r]] = mp.get(nums[r], 0) + 1
#             while len(mp) > k:
#                 mp[nums[l]] -= 1
#                 if mp[nums[l]] == 0: mp.pop(nums[l])
#                 l += 1
#             maxCount += (r - l + 1)
#         return maxCount
#     return solve(nums, k) - solve(nums, k - 1)
#
# print(subarrayIntegers([1,2,1,3,4], 3))

# ================================================================================================================================
# Minimum window substring

# Minimum window substring given a string s and target string we need to find the target string in s with minimum window length
# it can be of any order
# Create a frequency map of t
# for each character in s first check character in frequency map -> increase the count
# when count == len(t)
# check minimum length -> (r - l + 1) < minlen then update minlen and start point
# check is s[l] in mp then put that character back and decrement the count

# from collections import Counter
#
# def minimumWindowSubstring(s, t):
#     mp = Counter(t)
#     l = 0
#     minlen = float('inf')
#     count = 0
#     start = -1
#
#     for r in range(len(s)):
#         if s[r] in mp:
#             if mp[s[r]] > 0:
#                 count += 1
#             mp[s[r]] -= 1
#
#         while count == len(t):
#             if (r - l + 1) < minlen:
#                 minlen = r - l + 1
#                 start = l
#
#             if s[l] in mp:
#                 mp[s[l]] += 1
#                 if mp[s[l]] > 0:
#                     count -= 1
#             l += 1
#     return s[start:start + minlen]
#
# print(minimumWindowSubstring("ADOBECODEBANC", "ABC"))

# ================================================================================================================================
# Binary Search problems

# def firstLastOccurances(nums, x):
#     def lower_bound(nums, x):
#         low, high = 0, len(nums) - 1
#         ans = -1
#         while low <= high:
#             mid = low + ((high - low) // 2)
#             if nums[mid] >= x:
#                 ans = mid
#                 high = mid - 1
#             else:
#                 low = mid + 1
#         return ans
#
#     def upper_bound(nums, x):
#         low, high = 0, len(nums) - 1
#         ans = -1
#         while low <= high:
#             mid = low + ((high - low) // 2)
#             if nums[mid] > x:
#                 ans = mid
#                 high = mid - 1
#             else:
#                 low = mid + 1
#         return ans
#
#     lb = lower_bound(nums, x)
#     if (nums[lb] != x) or (lb == len(nums)): return -1
#     up = upper_bound(nums, x) - 1
#     return f"Indexes {lb, up}, length of window {up - lb + 1}"
#
# print(firstLastOccurances([5,7,7,8,8,10], 8))

# ================================================================================================================================
# Find the minimum in rotated array

# def minimumRotatedSortedArray(nums):
#     low, high = 0, len(nums) - 1
#     ans = float('inf')
#     while low <= high:
#         mid = low + ((high - low) // 2)
#         if nums[low] <= nums[mid]:
#             ans = min(ans, nums[low])
#             low = mid + 1
#         else:
#             ans = min(ans, nums[mid])
#             high = mid - 1
#     return ans
#
#
# print(minimumRotatedSortedArray([3,4,5,1,2]))

# ================================================================================================================================
# Search in rotated sorted array - I

# identify the sorted half's by checking nums[low] <= nums[mid] means left half is sorted
# nums[mid] <= nums[high] means right half is sorted

# def searchRotated(nums, target):
#     low, high = 0, len(nums) - 1
#     while low <= high:
#         mid = low + ((high - low) // 2)
#         if nums[mid] == target: return mid
#         if nums[low] <= nums[mid]:
#             if nums[low] <= target <= nums[mid]: high = mid - 1
#             else: low = mid + 1
#         else:
#             if nums[mid] <= target <= nums[high]: low = mid + 1
#             else: high = mid - 1
#     return -1
#
# print(searchRotated([4,5,6,7,0,1,2], 0))

# ================================================================================================================================
# Search in rotated sorted array - II

# Similar to search in rotated sorted array - I. identify the sorted half's then try to reduce the search space.
# check for edge cases where low, mid and high pointers have the same elements then reduce the low and high pointers

# def searchRotatedArray2(nums, target):
#     low, high = 0, len(nums) - 1
#     while low <= high:
#         mid = low + ((high - low) // 2)
#         if nums[mid] == target: return True
#         if nums[low] == nums[mid] and nums[high] == nums[mid]:
#             low += 1
#             high -= 1
#         if nums[low] <= nums[mid]:
#             if nums[low] <= target <= nums[mid]: high = mid - 1
#             else: low = mid + 1
#         else:
#             if nums[mid] <= target <= nums[high]: low = mid + 1
#             else: high = mid - 1
#     return False
#
# print(searchRotatedArray2([2,5,6,0,0,1,2], 0))

# ================================================================================================================================
# Find out how many times array has been rotated

# def findTimesArrayRotated(nums):
#     low, high = 0, len(nums) - 1
#     index = -1
#     ans = float('inf')
#     while low <= high:
#         mid = low + ((high - low) // 2)
#
#         # Check if the middle element is the smallest
#         if nums[mid] < ans:
#             ans = nums[mid]
#             index = mid
#
#         # If the left side is sorted, move to the unsorted side
#         if nums[low] <= nums[mid]:
#             if nums[low] < ans:
#                 ans = nums[low]
#                 index = low
#             low = mid + 1
#         else:  # If the right side is sorted, move to the unsorted side
#             high = mid - 1
#
#     return index
#
# print(findTimesArrayRotated([3,4,5,1,2]))

# ================================================================================================================================
# Peak Element

# def peakElement(arr):
#     n = len(arr)
#     if len(arr) == 1: return 0
#     if arr[0] > arr[1]: return 1
#     if arr[n - 1] > arr[n - 2]: return n - 1
#
#     low, high = 1, n - 2
#     while low <= high:
#         mid = low + ((high - low) // 2)
#         if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]: return mid
#         elif arr[mid] > arr[mid - 1]: low = mid + 1
#         else: high = mid - 1
#     return -1
#
# print(peakElement([1,2,1,3,5,6,4]))

# ================================================================================================================================
# Find the sqrt of an integer

# def findSqrt(n):
#     low, high = 1, n
#     ans = 1
#     while low <= high:
#         mid = low + ((high - low) // 2)
#         if mid ** 2 <= n:
#             ans = mid
#             low = mid + 1
#         else:
#             high = mid - 1
#     return ans
#
# print(findSqrt(25))
# print(findSqrt(28))

# ================================================================================================================================
# Find the Nth root

# def findSqrt(n, k):
#     low, high = 1, n
#     ans = 1
#     while low <= high:
#         mid = low + ((high - low) // 2)
#         if mid ** k <= n:
#             ans = mid
#             low = mid + 1
#         else:
#             high = mid - 1
#     return ans
#
# print(findSqrt(25, 3))

# ================================================================================================================================
# Koko eating bananas

# def kokoEatingBananas(pile, h):
#     def solve(pile, k):
#         totalhrs = 0
#         for num in pile:
#             totalhrs += int(num/k) + 1
#         return totalhrs
#
#     low, high = 1, max(pile)
#     ans = -1
#     while low <= high:
#         mid = low + ((high - low) // 2)
#         if solve(pile, mid) <= h:
#             ans = mid
#             high = mid - 1
#         else:
#             low = mid + 1
#     return ans
#
# print(kokoEatingBananas([3,6,7,11], 8))

# ================================================================================================================================
# Minimum days to make M bouquets

# Define the range: low = min(bloomDay), high = max(bloomDay)
# find the consecutive flowers that can be possible to make a bouquet
# m -> number of bouquet's, k -> number of flowers to make a bouquet
# to form a bouquet -> consecCount += 1 when count == k
# True when conseCount >= m
# Use Binary search to find minimum number of days in range of low <= high

# def minimumDaysToBloom(bloomDay, m, k):
#     def consecutiveCount(bloomDay, days, m, k):
#         count, consecCount = 0, 0
#         for bloom in bloomDay:
#             if bloom <= days:
#                 count += 1
#                 if count == k:
#                     consecCount += 1
#                     count = 0
#             else: count = 0
#         return consecCount >= m
#
#     if k * m > len(bloomDay): return -1
#     low, high, ans = min(bloomDay), max(bloomDay), -1
#     while low <= high:
#         mid = low + (high - low) // 2
#         if consecutiveCount(bloomDay, mid, m, k):
#             ans = mid
#             high = mid - 1
#         else: low = mid + 1
#     return ans
#
# print(minimumDaysToBloom([7 ,7 ,7 ,7 ,12,7, 7], 2, 3))

# ================================================================================================================================
# Find the smallest divisor given a threshold

# Similar to the Minimum bouquet problem
# Find the smallest number such that the range defined would be from 1 to max(nums)
# then finding the mid using the mid we find the sum of all the ceil(num / mid)
# then final value should be less than the threshold

# def smallestDivisor(nums, threshold):
#     def sumDivisor(nums, k):
#         res = 0
#         for num in nums:
#             res += math.ceil(num / k)
#         return res
#
#     low, high = 1, max(nums)
#     while low <= high:
#         mid = low + (high - low) // 2
#         if sumDivisor(nums, mid) <= threshold: high = mid - 1
#         else: low = mid + 1
#     return low
#
# print(smallestDivisor([44,22,33,11,1], 5))

# ================================================================================================================================
# Capacity to Ship Packages within D Days

# Capacity to ship packages within given time. starting from day = 1, count minimum number of days such that
# load + weight > capacity then day += 1 and load = weight
# else we can add as much of weight as possible
# calculate the capacity such that low = max(weights); high = sum(weights)
# to check daysRequired(weights, capacity=mid) <= days

# def capacityToShip(weights, days):
#     def daysRequired(weights, capacity):
#         days, load = 1, 0
#         for weight in weights:
#             if load + weight > capacity:
#                 days += 1
#                 load = weight
#             else: load += weight
#         return days
#
#     low, high = max(weights), sum(weights)
#     while low <= high:
#         mid = low + (high - low) // 2
#         if daysRequired(weights, mid) <= days: high = mid - 1
#         else: low = mid + 1
#     return low
#
# print(capacityToShip([1,2,3,4,5,6,7,8,9,10], 5))

# ================================================================================================================================
# Kth missing number

# Confusing topic....
# to find missing arr = [4] missing would be 1,2,3,5,6,.... now find kth number from the missing numbers.
# find the range in which the kth missing occurs -> first find missing at each index like [2,5,7] number of missing would be
# [1, 3, 4] how? -> arr[i] - (i + 1).. ez...
# now if missing at that index < k then increase your search space => low = mid + 1
# now if missing at that index > k then reduce your search space => high = mid - 1
# high will be index after which we can find the missing value
# missing will be arr[high] - (high + 1)
# more = k - missing
# finally arr[high] + more

# def kthmissingNumber(nums, k):
#     low, high = 0, len(nums) - 1
#     while low <= high:
#         mid = low + (high - low) // 2
#         missing = nums[mid] - (mid + 1)
#         if missing < k: low = mid + 1
#         else: high = mid - 1
#
#     missing = nums[high] - (high + 1)
#     more = k - missing
#     return nums[high] + more
#
# print(kthmissingNumber([2,3,4,7,11], 5))

# ================================================================================================================================
# Aggressive cows

# def aggressiveCows(stalls, cows):
#     stalls.sort()
#     def canPlaceCows(stalls, dist, cows):
#         countCows, minDist = 1, stalls[0]
#         for i in range(1, len(stalls)):
#             if stalls[i] - minDist >= dist:
#                 countCows += 1
#                 minDist = stalls[i]
#         return countCows >= cows
#
#     low, high = 0, (stalls[-1] - stalls[0])
#     ans = -1
#     while low <= high:
#         mid = low + (high - low) // 2
#         if canPlaceCows(stalls, mid, cows):
#             ans = mid
#             low = mid + 1
#         else:
#             high = mid - 1
#     return ans
#
# print(aggressiveCows([0,3,4,7,10,9], 4))

# ================================================================================================================================
# Allocate number books

# def allocateBooks(arr, n):
#     def isPossible(arr, n, max_pages):
#         students = 1
#         curr = 0
#         for num in arr:
#             if num + curr > max_pages:
#                 curr = num
#                 students += 1
#
#                 if students > n: return False
#             else:
#                 curr += num
#         return True
#
#     if n > len(arr): return -1
#     l, h = max(arr), sum(arr)
#     res = h
#     while l <= h:
#         mid = (l + h) // 2
#         if isPossible(arr, n, mid):
#             res = mid
#             h = mid - 1
#         else:
#             l = mid + 1
#     return res
#
# print(allocateBooks([25, 26, 28, 49, 24], 4))  # Expected output: 49

# ================================================================================================================================
# Painters Partition

# def paintersPartition(arr, k, n):
#     def isPossible(arr, k, maxN):
#         painter = 1
#         curr = 0
#         for num in arr:
#             if num + curr > maxN:
#                 curr = num
#                 painter += 1
#                 if painter > k: return False
#             else:
#                 curr += num
#         return True
#
#     low, high = max(arr), sum(arr)
#     res = -1
#     while low <= high:
#         mid = low + (high - low) // 2
#         if isPossible(arr, k, maxN=mid):
#             res = mid
#             high = mid - 1
#         else: low = mid + 1
#     return res
#
# print(paintersPartition([10, 20, 30, 40], 2, 4))

# ================================================================================================================================
# Minimise Maximum distance between gas stations

# def minimiseMaximumGasStations(stations, k):
#     def countOfGasStations(stations, dist):
#         count = 0
#         for i in range(1, len(stations)):
#             gap = stations[i] - stations[i - 1]
#             count += int(gap // dist)
#         return count
#
#     low, high = 0, max([stations[i + 1] - stations[i] for i in range(len(stations) - 1)])
#     ans = -1
#     while (high - low) > 1e-6:
#         mid = (high + low) / 2.0
#         count = countOfGasStations(stations, mid)
#         if count > k: low = mid
#         else:
#             ans = mid
#             high = mid
#     return ans
#
# print(minimiseMaximumGasStations([1,2,3,4,5], 4))

