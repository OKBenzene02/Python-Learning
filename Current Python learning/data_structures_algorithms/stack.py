from typing import List
from collections import deque

# Infix to postfix conversion

# def priority(operator):
#     if operator == '+' or operator == '-':
#         return 1
#     if operator == '*' or operator == '/':
#         return 2
#     if operator == '^':
#         return 3
#     return 0
#
# def infix_to_postfix(s):
#     i = 0; stack = []; ans = ""
#     while i < len(s):
#         if s[i].isalnum():
#             ans += s[i]
#         elif s[i] == '(':
#             stack.append(s[i])
#         elif s[i] == ')':
#             while stack and stack[-1] != '(':
#                 ans += stack.pop()
#             if stack and stack[-1] == '(':
#                 stack.pop()
#         else:
#             while stack and priority(s[i]) <= priority(stack[-1]):
#                 if s[i] == '^' and stack[-1] == '^': break
#                 ans += stack.pop()
#             stack.append(s[i])
#
#         i += 1
#
#     while stack:
#         ans += stack.pop()
#     return ans
#
# print(infix_to_postfix("a+b*(c^d-e)"))

# ================================================================================================================================
# Next greater element - 1

# def next_greater_element(arr):
#     stack = []
#     res = [0] * len(arr)
#     for i in range(len(arr) - 1, -1, -1):
#         while stack and stack[-1] <= arr[i]:
#             stack.pop()
#
#         res[i] = stack[-1] if stack else -1
#         stack.append(arr[i])
#
#     return res
#
# print(next_greater_element([4,12,5,3,1,2,5,3,1,2,4,6])) # [5, -1, 6, 5, -1, 3, 6, 4, -1, 4, -1]

# ================================================================================================================================
# Next greater element - 2

# def next_greater_element(arr):
#     stack = []
#     res = [0] * len(arr)
#     for i in range(2 * len(arr) - 1, -1, -1):
#         ind = i % len(arr)
#         while stack and stack[-1] <= arr[ind]:
#             stack.pop()
#
#         res[ind] = stack[-1] if stack else -1
#         stack.append(arr[ind])
#     return res
#
# print(next_greater_element([2,10,12,1,11]))

# ================================================================================================================================
# Previous smaller element

# def previous_smaller_element(nums):
#     stack = []
#     res = [0] * len(nums)
#     for i in range(len(nums)):
#         while stack and stack[-1] >= nums[i]:
#             stack.pop()
#         res[i] = stack[-1] if stack else -1
#         stack.append(nums[i])
#     return res
#
# print(previous_smaller_element([5,7,9,6,7,4,5,1,3,7])) # [-1, 5, 7, 5, 6, -1, 4, -1, 1, 3]
# print(previous_smaller_element([4,5,2,10,8]))

# ================================================================================================================================
# Next smaller element

# def next_smaller_element(nums):
#     stack = []
#     res = [0] * len(nums)
#     for i in range(len(nums) - 1, -1, -1):
#         while stack and stack[-1] >= nums[i]:
#             stack.pop()
#         res[i] = stack[-1] if stack else -1
#         stack.append(nums[i])
#     return res
#
# print(next_smaller_element([5,7,9,6,7,4,5,1,3,7]))

# ================================================================================================================================
# Sum of subarray's minimum

# def sum_of_subarray_minimum(nums):
#     pse = [0] * len(nums)
#     nse = [0] * len(nums)
#     # Calculating PSE
#     stack = []
#     for i in range(len(nums)):
#         while stack and stack[-1] >= nums[i]:
#             stack.pop()
#         pse[i] = stack[-1] if stack else -1
#         stack.append(i)
#
#     # Calculating NSE
#     stack = []
#     for i in range(len(nums) - 1, -1, -1):
#         while stack and nums[stack[-1]] > nums[i]:
#             stack.pop()
#         nse[i] = stack[-1] if stack else len(nums)
#         stack.append(i)
#
#     res = 0
#     for i in range(len(nums)):
#         res += ((nse[i] - i) * (i - pse[i])) * nums[i]
#     return res
#
# print(sum_of_subarray_minimum([1,4,6,7,3,7,8,1]))

# ================================================================================================================================
# Sum of subarray ranges

# def sum_of_subarray_ranges(nums):
#     n = len(nums)
#
#     # Previous Smaller Element
#     pse = [0] * n
#     # Next Smaller Element
#     nse = [0] * n
#
#     # Previous Smaller Element
#     stack = []
#     for i in range(n):
#         while stack and nums[stack[-1]] >= nums[i]:
#             stack.pop()
#         pse[i] = stack[-1] if stack else -1
#         stack.append(i)
#
#     # Next Smaller Element
#     stack = []
#     for i in range(n - 1, -1, -1):
#         while stack and nums[stack[-1]] > nums[i]:
#             stack.pop()
#         nse[i] = stack[-1] if stack else n
#         stack.append(i)
#
#     smallest = 0
#     for i in range(n):
#         left = i - pse[i]
#         right = nse[i] - i
#         smallest += nums[i] * left * right
#
#     # Previous Greater Element
#     pge = [0] * n
#     # Next Greater Element
#     nge = [0] * n
#
#     # Previous Greater Element
#     stack = []
#     for i in range(n):
#         while stack and nums[stack[-1]] <= nums[i]:
#             stack.pop()
#         pge[i] = stack[-1] if stack else -1
#         stack.append(i)
#
#     # Next Greater Element
#     stack = []
#     for i in range(n - 1, -1, -1):
#         while stack and nums[stack[-1]] < nums[i]:
#             stack.pop()
#         nge[i] = stack[-1] if stack else n
#         stack.append(i)
#
#     largest = 0
#     for i in range(n):
#         left = i - pge[i]
#         right = nge[i] - i
#         largest += nums[i] * left * right
#
#     return (largest - smallest) % (10 ** 9 + 7)
#
# print(sum_of_subarray_ranges([1,4,3,2]))

# ================================================================================================================================
# Asteroid collision

# def asteroid_collision(asteroids):
#     stack = []
#     for asteroid in asteroids:
#         if asteroid > 0:
#             stack.append(asteroid)
#         else:
#             while stack and stack[-1] < abs(asteroid):
#                 stack.pop()
#             if not stack or stack[-1] < 0:
#                 stack.append(asteroid)
#             if stack[-1] == -asteroid:
#                 stack.pop()
#     return stack
#
# print(asteroid_collision([4,7,1,1,2,-3,-7,17,15,-16]))

# ================================================================================================================================
# Largest rectangle in histogram
#
# def largest_rectangle(histograms):
#     n = len(histograms)
#     nse = [0] * n
#     pse = [0] * n
#
#     # Find NSE for each indexed element
#     stack = []
#     for i in range(n - 1, -1, -1):
#         while stack and histograms[stack[-1]] >= histograms[i]:
#             stack.pop()
#         nse[i] = stack[-1] if stack else n
#         stack.append(i)
#
#     # Find PSE for each indexed element
#     stack = []
#     for i in range(n):
#         while stack and histograms[stack[-1]] >= histograms[i]:
#             stack.pop()
#         pse[i] = stack[-1] if stack else -1
#         stack.append(i)
#
#     # Calculate the area for each rectangle
#     max_area = 1
#     for i in range(n):
#         max_area = max(max_area, histograms[i] * (nse[i] - pse[i] - 1))
#
#     return max_area
#
# print(largest_rectangle([2,1,5,6,2,3]))

# ================================================================================================================================
# Maximal rectangle

# def maximal_rectangle(matrix: List[List[int]]) -> int:
#     res = [[0] * len(matrix[0]) for _ in range(len(matrix))]
#     for i in range(len(matrix[0])):
#         res[0][i] = int(matrix[0][i])
#
#     for i in range(1,len(matrix)):
#         for j in range(len(matrix[0])):
#             if matrix[i][j] == '1' or matrix[i][j] == 1:
#                 res[i][j] += res[i-1][j] + 1
#             else:
#                 res[i][j] = 0
#
#     maxRectangle = 1
#     for i in range(len(res)):
#         maxRectangle = max(maxRectangle, calculate_largest_histogram(res[i]))
#     return maxRectangle
#
#
# def calculate_largest_histogram(histograms: List[int]) -> int:
#     n = len(histograms)
#     pse = [0] * n
#     nse = [0] * n
#
#     stack = []
#     # Calculate the PSE
#     for i in range(len(histograms)):
#         while stack and histograms[stack[-1]] >= histograms[i]:
#             stack.pop()
#         pse[i] = stack[-1] if stack else -1
#         stack.append(i)
#
#     # Calculate the NSE
#     stack = []
#     for i in range(len(histograms) - 1, -1, -1):
#         while stack and histograms[stack[-1]] >= histograms[i]:
#             stack.pop()
#
#         nse[i] = stack[-1] if stack else n
#         stack.append(i)
#
#     max_area = 1
#     for i in range(len(histograms)):
#         max_area = max(max_area, histograms[i] * (nse[i] - pse[i] - 1))
#     return max_area
#
# print(maximal_rectangle([[1,0,1,0,0],
#                           [1,0,1,1,1],
#                           [1,1,1,1,1],
#                           [1,0,0,1,0]]))

# ================================================================================================================================
# Remove k digits

# def remove_k_digits(nums: str, k: int) -> str:
#     stack = []
#     for i in range(len(nums)):
#         while k > 0 and stack and stack[-1] > nums[i]:
#             stack.pop()
#             k -= 1
#         stack.append(nums[i])
#     while k > 0:
#         stack.pop()
#         k -= 1
#
#     result = ''.join(stack).lstrip('0')
#     return result if result else '0'
#
# print(remove_k_digits('100', 1))

# ================================================================================================================================
# Stock span problem

# class StockSpan:
#
#     def __init__(self):
#         self._stack = []
#
#     def next(self, price: int) -> int:
#         span = 1
#         while self._stack and self._stack[-1][0] <= price:
#             span += self._stack.pop()[1]
#         self._stack.append([price, span])
#         return span
#
# obj = StockSpan()
# prices = [100, 80, 60, 70, 60, 75, 85]
# for i in range(len(prices)):
#     print(f'Day - 1, Price {prices[i]}, Span {obj.next(prices[i])}')
# ================================================================================================================================
# Sliding window maximum

# def sliding_window_maximum(nums: List[int], k: int) -> List[int]:
#     res = []
#     queue = deque()
#     for i in range(len(nums)):
#         while queue and queue[0] <= i - k:
#             queue.popleft()
#
#         while queue and nums[queue[-1]] < nums[i]:
#             queue.pop()
#
#         queue.append(i)
#         if i >= k - 1:
#             res.append(nums[queue[0]])
#     return res
#
# print(sliding_window_maximum([1,3,-1,-3,5,3,6,7], 3))

# def sliding_window_maximum(nums: List[int], k) -> List[int]:
#     res = []
#     queue = deque()
#     for i in range(len(nums)):
#         while queue and queue[0] <= i - k:
#             queue.popleft()
#
#         while queue and nums[queue[-1]] < nums[i]:
#             queue.pop()
#
#         queue.append(i)
#         if i >= k - 1:
#             res.append(nums[queue[0]])
#
#     return res
#
# print(sliding_window_maximum([1,3,-1,-3,5,3,6,7], 3))