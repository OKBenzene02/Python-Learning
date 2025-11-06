# # Heap sort
# class Solution:
#     def heapify(self, arr, n, i):
#         large = i
#         l = 2 * i + 1
#         r = 2 * i + 2
#
#         if l < n and arr[i] < arr[l]:
#             large = l
#         if r < n and arr[large] < arr[r]:
#             large = r
#         if large != i:
#             arr[i], arr[large] = arr[large], arr[i]
#             self.heapify(arr, n, large)
#
#     def heapsort(self, arr):
#         n = len(arr)
#         for i in range(n // 2 - 1, -1, -1):
#             self.heapify(arr, n, i)
#         for i in range(n - 1, 0, -1):
#             arr[i], arr[0] = arr[0], arr[i]
#             self.heapify(arr, i, 0)
#
#     def sortArray(self, nums: list) -> list:
#         self.heapsort(nums)
#         return nums
#
# a = Solution()
# print(a.sortArray([5,2,3,1]))

# ===================================================================
# Merge sort

# class MergeSort:
#
#     def mergesort(self, arr):
#         if len(arr) > 1:
#             mid = len(arr) // 2
#             L, R = arr[:mid], arr[mid:]
#             self.mergesort(L)
#             self.mergesort(R)
#
#             i, j, k = 0, 0, 0
#             while i < len(L) and j < len(R):
#                 if L[i] <= R[j]:
#                     arr[k] = L[i]
#                     i += 1
#                 else:
#                     arr[k] = R[j]
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
#         return arr
#
# arr = [12, 11, 13, 5, 6, 7]
# print(MergeSort().mergesort(arr))

# ===================================================================
# Quick Sort using Lomouto partition scheme that uses, last element as pivot.

# class QuickSort:
#
#     def partition(self, arr, lo, hi):
#         pivot = arr[hi]
#
#         i = lo - 1
#
#         for j in range(lo, hi):
#             if arr[j] <= pivot:
#                 i += 1
#                 arr[i], arr[j] = arr[j], arr[i]
#
#
#         arr[i + 1], arr[hi] = arr[hi], arr[i + 1]
#
#         return i + 1
#
#     def quicksort(self, arr, lo, hi):
#         if lo >= hi or lo < 0: return
#         j = self.partition(arr, lo, hi)
#         self.quicksort(arr, lo, j - 1)
#         self.quicksort(arr, j + 1, hi)
#         return arr
#
# arr = [5, 2, 9, 3, 7, 6, 1, 8, 4]
# print(QuickSort().quicksort(arr, 0, len(arr) - 1))

# ===================================================================
# Stack implementation
# from collections import deque
#
# class Stack:
#
#     def __init__(self):
#         self.arr = deque()
#
#     def push(self, a):
#         self.arr.append(a)
#
#     def pop(self):
#         self.arr.pop()
#
#     def isEmpty(self):
#         return True if len(self.arr) == 0 else False
#
#     def size(self):
#         return len(self.arr)
#
#     def show(self):
#         return self.arr
#
# s = Stack()
# s.push(1)
# s.push(2)
# s.push(3)
# s.push(4)
# s.push(5)
# print(s.show())
# s.pop()
# print(s.show())
# print(s.isEmpty())

# ===================================================================
# Queue Implementation

# class Queue:
#
#     def __init__(self):
#         self.arr = deque()
#
#     def enqueue(self, a):
#         self.arr.append(a)
#
#     def dequeue(self):
#         self.arr.popleft()
#
#     def front(self):
#         return self.arr[0]
#
#     def rear(self):
#         return self.arr[-1]
#
#     def show(self):
#         return self.arr
#
# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.enqueue(4)
# q.enqueue(5)
# q.enqueue(6)
# print(q.show())
# q.dequeue()
# q.dequeue()
# print(q.show())

# ===================================================================
# Valid String using stack

# def valid(s):
#     zero, one = 0, 0
#     stop = 0
#     if s.count('0') == s.count('1'):
#         for char in s:
#             if char == '1':
#                 one += 1
#             if char == '0':
#                 zero += 1
#             if zero >= one:
#                 continue
#             else:
#                 stop = 1
#                 break
#         if stop:
#             return 'no'
#         else:
#             return 'yes'
#
#     else:
#         return 'no'
#
#
# t = int(input())
# ans = []
# for _ in range(t):
#     n = int(input())
#     s = input()
#     ans.append(valid(s))
#
# for res in ans:
#     print(res)

# ===================================================================
# Ticket Counter problem using Deque

# def ticket_counter(n, k):
#     arr = deque(num for num in range(1, n + 1))
#     while len(arr) != 1:
#         for _ in range(k):
#             if len(arr) == 1: break
#             arr.popleft()
#         for _ in range(k):
#             if len(arr) == 1: break
#             arr.pop()
#
#     return arr[-1]
#
# t = int(input())
# ans = []
# for _ in range(t):
#     n, k = input().split()
#     ans.append(ticket_counter(int(n), int(k)))
#
#
# for res in ans:
#     print(res)

# ===================================================================
# Priority Queue, Geek and Contest ||
# import heapq
#
# def geek_marks(arr):
#     temp = []
#     for i in range(len(arr)):
#         heapq.heappush(temp, [arr[i], i + 1])
#     heapq.heapify(temp)
#     res = [0] * len(temp)
#     for i in range(len(temp) - 1, -1, -1):
#         res[i] = heapq.heappop(temp)[1]
#
#     return res
#
# t = int(input())
# ans = []
# for _ in range(t):
#     n = int(input())
#     arr = [int(num) for num in input().split()]
#     ans.append(geek_marks(arr))
# for i in ans:
#     for res in i:
#         print(res, end=" ")
#     print()

# ===============================================================
# Good Numbers using Queue
# from collections import deque
#
# def good_numbers(n):
#     queue = deque()
#     queue.append('1')
#     queue.append('2')
#     n -= 1
#     while n > 0:
#         s = queue[0]
#         queue.popleft()
#         queue.append(s + '1')
#         queue.append(s + '2')
#         n -= 1
#
#     return queue[0]
#
# t = int(input())
# ans = []
# for _ in range(t):
#     n = int(input())
#     res = good_numbers(n)
#     ans.append(res)
#
# for res in ans:
#     print(res)
# ===============================================================
# GeeksForGeeks problem using Queue

# from collections import deque
# def questions(n):
#     queue = deque(num for num in range(1, n + 1))
#     for _ in range(n):
#         if len(queue) == 1:
#             break
#         ele = queue.popleft()
#         queue.popleft()
#         queue.append(ele)
#
#     return queue[0]
#
#
# t = int(input())
# ans = []
# for _ in range(t):
#     n = int(input())
#     res = questions(n)
#     ans.append(res)
#
# for res in ans:
#     print(res)

# ===============================================================
# String pr, rp

# def pr_rp(x, y, s):
#     s1, s2 = 'pr', 'rp'
#     if x < y:
#         x, y = y, x
#         s1, s2 = s2, s1
#     stack = []
#     ans = 0
#     for i in range(len(s) - 1, -1, -1):
#         curr, first, second = s[i], s1[0], s1[1]
#         if stack and curr == first and stack[-1] == second:
#             stack.pop()
#             ans += x
#
#         else:
#             stack.append(curr)
#
#     new_stack = []
#     while len(stack) > 0:
#         new_stack.append(stack.pop())
#
#     new_str = "".join(new_stack)
#
#     for i in range(len(new_str) - 1, -1, -1):
#         curr, first, second = new_str[i], s2[0], s2[1]
#         if stack and curr == first and stack[-1] == second:
#             stack.pop()
#             ans += y
#
#         else:
#             stack.append(curr)
#
#     return ans
#
# print(pr_rp(5, 4, 'prabppprrr'))