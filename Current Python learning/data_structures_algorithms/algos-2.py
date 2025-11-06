# Last stone
# import heapq
#
# def lastStone(stones):
#     stones = [-num for num in stones]
#     heapq.heapify(stones)
#
#     while len(stones) > 1:
#         first = heapq.heappop(stones)
#         second = heapq.heappop(stones)
#         if abs(second) < abs(first):
#             heapq.heappush(stones, first - second)
#     stones.append(0)
#     return abs(stones[0])
#
# print(lastStone([2,7,4,1,8,1]))

# =======================================================================
# Top k frequent words
# def frequent_words(words, k):
#     mp = {}
#     for word in words:
#         mp[word] = 1 + mp.get(word, 0)
#     mp = sorted(mp, key=lambda x: (-mp[x], x))
#     return mp[:k]
#
# print(frequent_words(["i","love","leetcode","i","love","coding"], 3))

# ========================================================================
# find the Median of the two sorted arrays

# def findMedianSortedArrays(nums1, nums2):
#     i, j, k = 0, 0, 0
#     m, n = len(nums1), len(nums2)
#     temp = [0] * (m + n)
#
#     while (i < m) and (j < n):
#         if nums1[i] <= nums2[j]:
#             temp[k] = nums1[i]
#             i += 1
#         else:
#             temp[k] = nums2[j]
#             j += 1
#         k += 1
#
#     while i < m:
#         temp[k] = nums1[i]
#         i += 1
#         k += 1
#
#     while j < n:
#         temp[k] = nums2[j]
#         j += 1
#         k += 1
#
#     if k % 2 == 0:
#         mid = k // 2
#         return float((temp[mid] + temp[mid - 1]) / 2), temp
#
#     else:
#         mid = k // 2
#         return float((temp[mid])), temp
#
#
# print(findMedianSortedArrays([1, 2, 3, 4, 5], [4, 6, 7, 8]))
# ========================================================================
# Roman to integer

# def roman(s: str):
#     symbols = {
#         'I': 1,
#         'V': 5,
#         'X': 10,
#         'L': 50,
#         'C': 100,
#         'D': 500,
#         'M': 1000,
#     }
#
#     val = 0
#     for i in range(len(s)):
#         left, right = s[i], s[i+1:i+2]
#         if right and symbols[left] < symbols[right]:
#             val -= symbols.get(left)
#         else:
#             val += symbols.get(left)
#
#     return val
#
# print(roman('MCMXCIV'))

# ===============================================================
# Longest common prefix

# def longestCommonPrefix(strs):
#     if not strs: return
#
#     min_char = min(strs, key=len)
#     for i, ch in enumerate(min_char):
#         for oth in strs:
#             if oth[i] != ch:
#                 return min_char[: i]
#     return min_char
#
# print(longestCommonPrefix(["flower","flow","flight"]))

# Approach 2
# def longestCommonPrefix(strs):
#     if not strs: return -1
#
#     prefix = strs[0]
#
#     for s in strs[1:]:
#         while not s.startswith(prefix):
#             prefix = prefix[:-1]
#             if not prefix: return -1
#
#     return prefix
#
# print(longestCommonPrefix(["geeksforgeeks", "geeks", "geek", "geezer"]))
# print(longestCommonPrefix(["d", "d", "d", "d"]))


# ===============================================================
# Valid Parentheses

# def isValid(s: str):
#     stack = []
#     for char in s:
#         if not stack:
#             stack.append(char)
#         else:
#             if (char == ')' and '(' == stack[-1]) or (char == ']' and '[' == stack[-1]) or (char == '}' and '{' == stack[-1]):
#                 stack.pop()
#             else:
#                 stack.append(char)
#
#     return True if not stack else False
#
# print(isValid('{[(}]}'))
# ===============================================================
# Remove duplicates from the array

# def remove(nums: list):
#     l = 1
#     for i in range(len(nums) - 1):
#         if nums[i] != nums[i + 1]:
#             nums[l] = nums[i + 1]
#             l += 1
#     return l
#
# print(remove([0,0,1,1,1,2,2,3,3,4]))

# ===============================================================
# Remove Elements from the array

# def remove_element(nums, val):
#     l = 0
#     for i in range(len(nums) - 1):
#         if nums[i] != val:
#             nums[l] = nums[i]
#             l += 1
#     return l, nums
#
# print(remove_element([0,1,2,2,3,0,4,2], 2))
# ===============================================================

# def trace_of_matrix(mat, n):
#     left, right = 0, 0
#     for i in range(n):
#         left += mat[i][i]
#         right += mat[i][n - 1 - i]
#     return f"{left}\n{right}"
#
# def create_and_produce(n):
#     mat = []
#     for i in range(n):
#         tmp = list(map(int, input().split()))
#         mat.append(tmp)
#     return trace_of_matrix(mat, n)
#     # return mat
# n = int(input())
# print(create_and_produce(n))

# ===============================================================
# Length of the last word without using the split method

# def length(s: str):
#     end = len(s) - 1
#     while end > 0 and s[end] == " ":
#         end -= 1
#     beg = end
#     while beg >= 0 and s[beg] != " ":
#         print(s[beg])
#         beg -= 1
#     return beg
#
# print(length("Hello World"))
# ===============================================================
# Can place flower in flowerbed

# def canPlace(arr, n):
#     for i in range(len(arr)):
#         if arr[i] == 0:
#             left_end = (i == 0) or (not arr[i - 1])
#             right_end = (i == len(arr) - 1) or (not arr[i + 1])
#             if left_end and right_end:
#                 arr[i] = 1
#                 n -= 1
#
#     return True if n <= 0 else False
#
# print(canPlace([1,0,0,0,1], 2))

# ===============================================================
# Count maximum sub-arrays with zeros

# def count_zeros(nums):
#     if not nums:
#         return 0
#
#     count, total = 0, 0
#     for num in nums:
#         if num == 0:
#             count += 1
#         if num != 0:
#             count = 0
#         total += count
#     return total
#
#
# print(count_zeros([2,10,2019]))

# ===============================================================
# Minimum time to book a taxi

# def minimumTime(N : int, cur : int, pos, time) -> int:
#     min_time = 9999999999
#     for i in range(N):
#         cur_time = abs(pos[i] - cur) * time[i]
#         min_time = min(cur_time, min_time)
#
#     return min_time
#
# print(minimumTime(3, 4, [1, 5, 6], [2, 3, 1]))

# ===============================================================
# Happy number

# def square(n):
#     temp = n
#     cur_sum = 0
#     while temp > 0:
#         rem = temp % 10
#         cur_sum += rem ** 2
#         temp //= 10
#     return cur_sum
#
# def happy(n):
#     mp = set()
#     while n != 1 and n not in mp:
#         mp.add(n)
#         n = square(n)
#
#     return n == 1
#
# print(happy(2))

# ====================================================================
# Minimum path sum

# def minPathSum(grid: list[list]) -> int:
#     m, n = len(grid), len(grid[0])
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
# print(minPathSum([[1,3,1],[1,5,1],[4,2,1]]))

# ====================================================================
# Longest substring without repeating characters

# def longestChars(s):
#     chars = set()
#     l, res = 0, 0
#
#     for r in range(len(s)):
#         while s[r] in chars:
#             chars.remove(s[l])
#             l += 1
#
#         chars.add(s[r])
#         res = max(res, r - l + 1)
#
#     return res
#
# print(longestChars('bbbbbbb'))
# ====================================================================
# Plus One

# def plusOne(digits):
#     num = 0
#     for i in range(len(digits) - 1, -1, -1):
#         num += (10 ** i) * digits[len(digits) - i - 1]
#     return [int(num) for num in str(num + 1)]
#
# print(plusOne([9]))
# ====================================================================

# def minCostTickets(costs, days):
#     dp = [0] * 366
#
#     days = set(days)
#     for i in range(1, 366):
#         if i not in days:
#             dp[i] = dp[i - 1]
#         else:
#             dp[i] = min(dp[i - 1] + costs[0], dp[max(i - 7, 0)] + costs[1], dp[max(i - 30, 0)] + costs[2])
#
#     return dp[365]
#
# print(minCostTickets([2,7,15], [1,4,6,7,8,20]))

# ====================================================================
# Reducing Dishes

# def reduceDishes(satisfaction):
#     satisfaction.sort(reverse=True)
#
#     res, curr = 0, 0
#     for i in range(len(satisfaction)):
#         curr += satisfaction[i]
#         if curr < 0:
#             break
#         res += curr
#
#     return res
#
# print(reduceDishes([-1,-8,0,5,-9]))
# ====================================================================
# Single Num
#
# def singleNum(nums):
#     temp = 0
#     for num in nums:
#         temp ^= num
#
#     return temp
#
# print(singleNum([4,1,2,1,2]))
# ====================================================================
# Missing Number

# def missingNumber(nums):
#     xor = len(nums)
#     for i in range(len(nums)):
#         xor ^= i
#         xor ^= nums[i]
#     return xor
#
# print(missingNumber([3,0,1]))
# ====================================================================
# Majority Element

# def major(nums):
#     """Approach 1"""
#     # mp = {}
#     # for num in nums:
#     #     mp[num] = 1 + mp.get(num, 0)
#     #
#     # for key, val in mp.items():
#     #     if val > (len(nums) // 2):
#     #         return key
#     # return -1
#     """Approach 2 - Moore's Algorithm"""
#     n = len(nums)
#     count = 0
#     element = None
#     for num in nums:
#         if count == 0:
#             count += 1
#             element = num
#         if num == element: count += 1
#         else: count -= 1
#
#     new_count = 0
#     for num in nums:
#         if element == num:
#             new_count += 1
#
#     if new_count > (n // 2): return element
#     return -1
#
#
# print(major([3,2,3]))
# ====================================================================
# Pascals Triangle

# def pascalTriangle(n):
#     l = []
#
#     for i in range(1, n + 1):
#         c = 1
#         temp = []
#         for j in range(1, i + 1):
#             temp.append(c)
#             c = c * (i - j) // j
#         l.append(temp)
#
#     return l
#
# print(pascalTriangle(5))

# ====================================================================
# Scrambled Strings
# mp = {}
#
# def isScramble(s1: str, s2: str) -> bool:
#     n = len(s1)
#
#     if s1 == s2:
#         return True
#
#     a, b, c = [0] * 26, [0] * 26, [0] * 26
#     if (s1 + s2) in mp:
#         return mp[s1 + s2]
#
#     for i in range(1, n):
#         j = n - i
#         a[ord(s1[i - 1]) - ord('a')] += 1
#         b[ord(s2[i - 1]) - ord('a')] += 1
#         c[ord(s2[j]) - ord('a')] += 1
#         if a == b and isScramble(s1[:i], s2[:i]) and isScramble(s1[i:], s2[i:]):
#             mp[s1 + s2] = True
#             return True
#         if a == c and isScramble(s1[:i], s2[j:]) and isScramble(s1[i:], s2[:j]):
#             mp[s1 + s2] = True
#             return True
#
#     mp[s1 + s2] = False
#     return False
#
# print(isScramble("great", "rgeat"))

# =============================================================================================
# Convert Array into 2d Array where each dimension should have distinct elements

# def array2d(nums):
#     arr, mp = [], {}
#     for num in nums:
#         mp[num] = mp.get(num, 0) + 1
#
#     n = max(mp.values())
#     for _ in range(n):
#         temp = []
#         for key in mp.copy():
#             temp.append(key)
#             mp[key] -= 1
#             if mp[key] == 0:
#                 mp.pop(key)
#         arr.append(temp)
#
#     return arr
#
# print(array2d([1,2,3,4]))
# =============================================================================================
# Mice And Cheese maximum rewarding based on heaps (Priority Queues)

# import heapq
# def miceCheese(nums1, nums2, k):
#     res = 0
#     heap = []
#     for i in range(len(nums1)):
#         heapq.heappush(heap, (nums2[i] - nums1[i], i))
#
#     visited = set()
#     while k:
#         _, idx = heapq.heappop(heap)
#         visited.add(idx)
#         res += nums1[idx]
#         k -= 1
#
#     for i, val in enumerate(nums2):
#         if i in visited:
#             continue
#         res += val
#     return res
#
#
# print(miceCheese([1,1,3,4], [4,4,1,1], 2))

# =============================================================================================
# Longest Balanced Substring of a Binary String

# def longest(s):
#     n, res = 0, 0
#     while n < len(s):
#         ones, zeros = 0, 0
#         while n < len(s) and s[n] == '0':
#             n += 1
#             zeros += 1
#         while n < len(s) and s[n] == '1':
#             n += 1
#             ones += 1
#         res = max(res, 2 * min(ones, zeros))
#     return res
#
# print(longest('01000111'))

# =============================================================================================
# Successful Pairs of Spells and Potions

# def spellsNpotions(spells, potions, success):
#     res = []
#     potions.sort()
#     n = len(potions)
#     for spell in spells:
#         low, high = 0, n
#         while low < high:
#             mid = (low + high) // 2
#             if spell * potions[mid] >= success:
#                 high = mid
#             else:
#                 low = mid + 1
#         res.append(n - high)
#     return res
#
#
# print(spellsNpotions([3,1,2], [8,5,8], 16))
# =============================================================================================
# Minimum Boats to save

# def save(people, k):
#     people = sorted(people)
#     l, r = 0, len(people) - 1
#     count = 0
#     while l <= r:
#         count += 1
#         if people[l] + people[r] <= k:
#             l += 1
#         r -= 1
#
#     return count
#
# print(save([3,2,2,1], 3))

# =============================================================================================
# Optimal Partition of String

# def partition(s):
#     mp, seen = {}, set()
#     res = 0
#     for char in s:
#         mp[char] = mp.get(char, 0) + 1
#
#     length = max(mp.values())
#
#     for _ in range(length):
#         part = ''
#         for key in mp.copy():
#             part += key
#             mp[key] -= 1
#             if mp[key] == 0:
#                 mp.pop(key)
#             if part in seen:
#                 seen = set()
#                 res += 1
#             seen.add(part)
#     return res + 1
#
#     seen, res = set(), 0
#
#     for char in s:
#         if char in seen:
#             res += 1
#             seen = set()
#         seen.add(char)
#     return res + 1
#
# print(partition("gizfdfri"))
# print(partition("ssssss"))

# =================================================================
# Minimize Maximum of Array

# def check(nums, mid):
#     curr = 0
#     for num in nums:
#         if num <= mid:
#             curr += (mid - num)
#         else:
#             if curr < num - mid:
#                 return False
#             else:
#                 curr -= (num - mid)
#     return True
#
# def minimizeArrayValue(nums):
#     low, high = 0, max(nums)
#     while low < high:
#         mid = (low + high) // 2
#         if check(nums, mid):
#             high = mid
#         else:
#             low = mid + 1
#     return low
#
#
# print(minimizeArrayValue([3, 7, 1, 6]))
# =================================================================

# Zig Zag conversion

# def zigzag(s, rows):
#     if rows == 1:
#         return s
#
#     res = ""
#     for row in range(rows):
#         increment = (rows - 1) * 2
#         for i in range(row, len(s), increment):
#             res += s[i]
#             if (row > 0) and (row < rows - 1) and (i + increment - 2 * row) < len(s):
#                 res += s[i + increment - 2 * row]
#     return res
#
# print(zigzag("PAYPALISHIRING", 3))

# def zigZagConversion(s, rows):
#     if rows == 1 or rows >= len(s) - 1: return s
#     L = [''] * rows
#     index, step = 0, 1
#     for char in s:
#         L[index] += char
#         if index == 0: step = 1
#         elif index == rows - 1: step = -1
#         index += step
#     return "".join(L)
#
# print(zigZagConversion('PAYPALISHIRING', 3))

# =================================================================
# Longest Palindromic Substring

# def palindrome(s):
#     res = ''
#     max_len = 0
#     for i in range(len(s)):
#         l, r = i, i
#         while l >= 0 and r < len(s) and s[l] == s[r]:
#             if r - l + 1 > max_len:
#                 res = s[l:r + 1]
#                 max_len = r - l + 1
#             l -= 1
#             r += 1
#
#         l, r = i, i + 1
#         while l >= 0 and r < len(s) and s[l] == s[r]:
#             if r - l + 1 > max_len:
#                 res = s[l:r + 1]
#                 max_len = r - l + 1
#             l -= 1
#             r += 1
#
#     return res
#
# print(palindrome('babad'))

# =================================================================
# Container with most water

# def container(height):
#     l, r = 0, len(height) - 1
#     min_water = 0
#     while l < r:
#         step = r - l
#         min_water = max(step * min(height[r], height[l]), min_water)
#         if height[l] < height[r]:
#             l += 1
#         else:
#             r -= 1
#
#     return min_water
#
# print(container([1,8,6,2,5,4,8,3,7]))

# =======================================================================
# Transpose of a matrix - reverse order (Rotate Image)

# def rotateImage(matrix):
#     l, r = 0, len(matrix) - 1
#     while l < r:
#         matrix[l], matrix[r] = matrix[r], matrix[l]
#         l += 1
#         r -= 1
#
#     for i in range(len(matrix)):
#         for j in range(i):
#             matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
#
#
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# rotateImage(matrix)
# print(matrix)

# Rotate image Easy - check whether the given matrix when rotated can give target matrix

# def checkMatrix(nums, target):
#     if nums == target:
#         return True
#
#     deg = 4
#     while deg:
#         l, r = 0, len(nums) - 1
#         while l < r:
#             nums[l], nums[r] = nums[r], nums[l]
#             l += 1
#             r -= 1
#         for i in range(len(nums)):
#             for j in range(i):
#                 nums[i][j], nums[j][i] = nums[j][i], nums[i][j]
#         if nums == target:
#             return True
#         deg -= 1
#
#     return False
#
# print(checkMatrix([[0,0,0],[0,1,0],[1,1,1]], [[1,1,1],[0,1,0],[0,0,0]]))
# =======================================================================
# Gas Station

# def checkStation(gas, cost):
#     trip, idx = 0, 0
#     for i in range(len(gas)):
#         trip += gas[i] - cost[i]
#         if trip < 0:
#             idx = i + 1
#             trip = 0
#     return idx if trip >= 0 else -1
#
#
# print(checkStation([1,2,3,4,5], [3,4,5,1,2]))

# =======================================================================
# Combination Sum

# def solve(candidate, curr, path, res):
#     if curr == 0:
#         res.append(path)
#         return
#     if curr < 0:
#         return
#
#     for i in range(len(candidate)):
#         solve(candidate[i:], curr - candidate[i], path + [candidate[i]], res)
#
# def SumUp(candidates, targetSum):
#     res = []
#     solve(candidates, targetSum, [], res)
#     return res
#
# print(SumUp([2, 3, 5], 8))
# =======================================================================
# Coin Change Problem

# def coinChange(coins, amount):
#     # dp = [[0] * (amount + 1)] * (len(coins) + 1)
#     # for i in range(1, amount + 1):
#     #     dp[0][i] = float('inf')
#     #
#     # for c, coin in enumerate(coins, 1):
#     #     for r in range(1, amount + 1):
#     #         if coin == amount:
#     #             dp[c][r] = 1
#     #         elif coin > amount:
#     #             dp[c][r] = dp[c - 1][r]
#     #         else:
#     #             dp[c][r] = min(dp[c - 1][r], 1 + dp[c][r - coin])
#     #
#     # return dp[-1][-1]
#
#     dp = [float('inf')] * (amount + 1)
#     dp[0] = 0
#     for coin in coins:
#         for i in range(coin, amount + 1):
#             dp[i] = min(dp[i], 1 + dp[i - coin])
#     return dp[amount] if dp[amount] != float('inf') else -1
#
#
# print(coinChange([281,20,251,251], 7323))

# =======================================================================
# Prime Diagonal

# def isPrime(n):
#     if n <= 2 or n % 2 == 0:
#         return n == 2
#     for i in range(3, int(math.sqrt(n)) + 1, 2):
#         if n % i == 0:
#             return False
#     return True
# def diagPrime(nums):
#     res = 0
#     for i in range(len(nums)):
#         if isPrime(nums[i][i]):
#             res = max(res, nums[i][i])
#         if isPrime(nums[i][len(nums) - 1 - i]):
#             res = max(res, nums[i][len(nums) - 1 - i])
#     return res
#
# print(diagPrime([[1, 1, 1], [1, 1, 1], [1, 1, 1]]))
# =======================================================================
# Sum of Distances

# def sumOfDist(nums):
#     res = []
#     mp, indices = dict(), dict()
#
#     for i, num in enumerate(nums):
#         mp[num] = mp.get(num, 0) + 1
#         if num not in indices:
#             indices[num] = i
#         else:
#             indices[num] += i
#
#     for i in range(len(nums)):
#         res.append(indices[nums[i]] - mp[nums[i]] * i)
#         indices[nums[i]] -= 2 * i
#         mp[nums[i]] -= 2
#     return res
#
#
# print(sumOfDist([0,5,3]))
# =======================================================================
# Minimize the maximum difference of pairs

# def minimizeMax(nums, p):
#     if p == 0:
#         return 0
#
#     def check(mid):
#         count = 0
#         visitedPre = 0
#         for d in diff:
#             if d <= mid:
#                 if visitedPre == 0:
#                     count += 1
#                     visitedPre = 1
#                 else:
#                     visitedPre = 0
#             else:
#                 visitedPre = 0
#         return count >= p
#     nums.sort()
#     diff = [nums[i] - nums[i - 1] for i in range(1, len(nums))]
#     low = min(diff) - 1
#     high = nums[-1] - nums[0]
#     while low + 1 < high:
#         mid = (low + high) // 2
#         if check(mid):
#             high = mid
#         else:
#             low = mid
#     return high
#
# print(minimizeMax([10,1,2,7,1,3], 2))

# ===================================================
# Largest Color Value in a directed Graph

# from collections import defaultdict
# def largestPathValue(colors, edges):
#     adj = defaultdict(list)
#     for src, dst in edges:
#         adj[src].append(dst)
#
#     def dfs(node):
#         if node in path:
#             return float('inf')
#         if node in visit:
#             return 0
#
#         visit.add(node)
#         path.add(node)
#
#         colorIdx = ord(colors[node]) - ord('a')
#         count[node][colorIdx] = 1
#
#         for vertex in adj[node]:
#             if dfs(vertex) == float('inf'):
#                 return float('inf')
#             for c in range(26):
#                 count[node][c] = max(count[node][c], (1 if c == colorIdx else 0) + count[vertex][c])
#         path.remove(node)
#         return max(count[node])
#
#     n, res = len(colors), 0
#     visit, path = set(), set()
#     count = [[0] * 26] * n
#     for i in range(n):
#         res = max(dfs(i), res)
#     return -1 if res == float('inf') else res
#
# print(largestPathValue("abaca", [[0,1],[0,2],[2,3],[3,4]]))
# ================================================================================

# Remove Stars from String

# def remove(s):
#     res = []
#
#     for char in s:
#         if char != '*':
#             res += char
#         else:
#             res.pop()
#
#     return "".join(res)
#
# print(remove('erase*****'))
# ================================================================================
# Simplify path

# def simplifyPath(path):
#     p, res = path.split('/'), []
#     for i in range(len(p)):
#         if res and p[i] == '..':
#             res.pop()
#         elif not p[i] == "" and not p[i] == '.' and not p[i] == '..':
#             res.append(p[i])
#     if not res:
#         return '/'
#     return '/' + '/'.join(res)
#
# print(simplifyPath('/a/./b/../../c/'))

# =============================================================================
# Transpose of a matrix

# def transpose(matrix):
#     m, n = len(matrix[0]), len(matrix)
#     temp = [[None] * n for _ in range(m)]
#     for i in range(m):
#         for j in range(n):
#             temp[i][j] = matrix[j][i]
#     return temp
#
# print(transpose([[[5],[8]]]))

# =============================================================================
# Asteroid Collision

# def collision(asteroids):
#     stack = []
#     for num in asteroids:
#         if num > 0:
#             stack.append(num)
#         else:
#             while stack and 0 < stack[-1] < abs(num):
#                 stack.pop()
#             if not stack or stack[-1] < 0:
#                 stack.append(num)
#             if stack[-1] == -num:
#                 stack.pop()
#     return stack
#
#
# print(collision([10, 2, -5]))

# def collision(asteroids):
#     stack = []
#     for i in range(len(asteroids)):
#         if asteroids[i] > 0 or not stack or stack[-1] < 0:
#             stack.append(asteroids[i])
#         elif stack[-1] <= -asteroids[i]:
#             if stack[-1] < -asteroids[i]:
#                 i -= 1
#             stack.pop()
#
#     return stack
#
# print(collision([10, 2, -5]))

# def asteroidCollisions(asteroids):
#     stack = []
#     for asteroid in asteroids:
#         while stack and stack[-1] > 0 and asteroid < 0:
#             if stack[-1] + asteroid == 0: stack.pop()
#             if stack[-1] + asteroid > 0: break
#             else:
#                 stack.pop()
#                 break
#         else: stack.append(asteroid)
#     return stack
#
# print(asteroidCollisions([10, 2, -5]))

# ============================================================================
# Validate the stack sequences

# def validate(pushed, popped):
#     stack = []; i = 0
#     for num in pushed:
#         stack.append(num)
#         while stack and stack[-1] == popped[i]:
#             stack.pop()
#             i += 1
#     return not stack
#
#
# print(validate([1,2,3,4,5], [4,3,5,1,2]))
# ============================================================================

# Longest Common SubSequence

# def longestCommonSubsequence(s1, s2):
#     dp = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
#
#     for i in range(len(s1) - 1, -1, -1):
#         for j in range(len(s2) - 1, -1, -1):
#             if s1[i] == s2[j]:
#                 dp[i][j] = 1 + dp[i + 1][j + 1]
#             else:
#                 dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
#
#     return dp[0][0]
#
# print(longestCommonSubsequence('abcde', 'ace'))


# def longestCommonSubsequence(s):
#     s1, s2 = s, s[::-1]
#     dp = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
#
#     for i in range(len(s1) - 1, -1, -1):
#         for j in range(len(s2) - 1, -1, -1):
#             if s1[i] == s2[j]:
#                 dp[i][j] = 1 + dp[i + 1][j + 1]
#             else:
#                 dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
#
#     return dp[0][0]
#
# print(longestCommonSubsequence('cbba'))
# ============================================================================
# Maximum value of K coins from pile

# def maximumKvalue(piles, k):
#     n = len(piles)
#     dp = [[-1] * (k + 1) for _ in range(n)]
#     def dfs(i, coins):
#         if i == n:
#             return 0
#
#         if dp[i][coins] != -1:
#             return dp[i][coins]
#
#         dp[i][coins] = dfs(i + 1, coins)
#         curPile = 0
#         for j in range(min(coins, len(piles[i]))):
#             curPile += piles[i][j]
#             dp[i][coins] = max(dp[i][coins], curPile + dfs(i + 1, coins - j - 1))
#         return dp[i][coins]
#
#     return dfs(0, k)
#
#
# print(maximumKvalue([[1,100,3],[7,8,9]], 2))

# ============================================================================

