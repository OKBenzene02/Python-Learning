# Median of two sorted arrays using Binary search

# def medianOfTwoSortedArrays(arr1, arr2):
#     n1, n2 = len(arr1), len(arr2)
#     if n1 > n2: return medianOfTwoSortedArrays(arr2, arr1)
#     low, high = 0, n1
#     left = (n1 + n2 + 1) // 2
#     while low <= high:
#         mid1 = (low + high) // 2
#         mid2 = left - mid1
#         l1, l2 = float('-inf'), float('-inf')
#         r1, r2 = float('inf'), float('inf')
#         if mid1 < n1: r1 = arr1[mid1]
#         if mid2 < n2: r2 = arr2[mid2]
#         if mid1 - 1 >= 0: l1 = arr1[mid1 - 1]
#         if mid2 - 1 >= 0: l2 = arr2[mid2 - 1]
#         if l1 <= r2 and l2 <= r1:
#             if (n1 + n2) % 2 == 0: return float((max(l1, l2) + min(r1, r2)) / 2)
#             return float(max(l1, l2))
#         elif l1 > r2: high = mid1 - 1
#         else: low = mid1 + 1
#     return 0
#
# print(medianOfTwoSortedArrays([1,3], [2]))

# ================================================================================================================================
# kth element of two sorted arrays using Binary search

# def kthElement(arr1, arr2, k):
#     n1, n2 = len(arr1), len(arr2)
#     if n1 > n2: return kthElement(arr2, arr1, k)
#     low, high = max(0, k - n2), min(k, n1)
#     left = k
#     n = n1 + n2
#     while low <= high:
#         mid1 = (low + high) // 2
#         mid2 = left - mid1
#         l1, l2 = float('-inf'), float('-inf')
#         r1, r2 = float('inf'), float('inf')
#         if mid1 < n1: r1 = arr1[mid1]
#         if mid2 < n2: r2 = arr2[mid2]
#         if mid1 - 1 >= 0: l1 = arr1[mid1 - 1]
#         if mid2 - 1 >= 0: l2 = arr2[mid2 - 1]
#         if l1 <= r2 and l2 <= r1:
#             return max(l1, l2)
#         elif l1 > r2: high = mid1 - 1
#         else: low = mid1 + 1
#     return 0
#
#
# print(kthElement([2,3,6,7,9], [1,4,8,10], 4))

# ================================================================================================================================
# Maximum number of 1's

# def maximumOnes(ones):
#     def lower_bound(arr):
#         low, high = 0, len(arr) - 1
#         ans = len(arr)
#         while low <= high:
#             mid = low + ((high - low) // 2)
#             if arr[mid] >= 1:
#                 ans = mid
#                 high = mid - 1
#             else:
#                 low = mid + 1
#         return ans
#
#     max_ones = 0; max_index = -1
#     for i, one in enumerate(ones):
#         curr_ones = len(one) - lower_bound(one)
#         if curr_ones > max_ones:
#             max_ones = curr_ones
#             max_index = i
#
#     return max_index, max_ones
#
# print(maximumOnes([[0,1],[1,0]]))

# ================================================================================================================================
# Row with minimum number of 1's

# def minimumNumber(a):
#     min_idx = len(a[0]); min_ones = a[0].count(1)
#     for i in range(1, len(a)):
#         curr_ones = a[i].count(1)
#         if curr_ones <= min_ones:
#             min_idx = min(i + 1, min_idx)
#             min_ones = curr_ones
#     return min_idx
#
# print(minimumNumber([[0,0,0],[0,0,0],[0,0,0]]))

# ================================================================================================================================
# Largest subarray with sum zero

# Perfix sum + hash map method. Calculate the prefix sum for each element encountered.
# maintain a hashmap and add (sum, ind) to the hashmap
# when sum in hashmap then (curr_ind - map[sum])

# def largestSubarrayWithSumZero(nums):
#     mp = dict()
#     pref = 0
#     maxLen = 0
#     for i in range(len(nums)):
#         pref += nums[i]
#         if pref == 0:
#             maxLen = i + 1
#         else:
#             if pref not in mp:
#                 mp[pref] = i
#             maxLen = max(maxLen, i - mp[pref])
#     return maxLen
#
# print(largestSubarrayWithSumZero([1,-1,3,2,-2,-8,1,7,10,2,3]))

# ================================================================================================================================
# Count Subarrays with xor as k

# def countSubarraysWithXOR(nums, k):
#     mp = dict()
#     pref = 0
#     count = 0
#     for i in range(len(nums)):
#         pref ^= nums[i]
#         if pref == k:
#             count += 1
#         count += mp.get(pref ^ k, 0)
#         mp[pref] = mp.get(pref, 0) + 1
#     return count
#
# print(countSubarraysWithXOR([5, 6, 7, 8, 9], 5))

# ================================================================================================================================