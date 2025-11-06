# Trie Data Structure - 23-03-17

# class Trie:
#     def __init__(self):
#         self.root = {"*": "*"}
#
#     def add(self, word):
#         curr_node = self.root
#         for letter in word:
#             if letter not in curr_node:
#                 curr_node[letter] = {}
#             curr_node = curr_node[letter]
#         curr_node['*'] = '*'
#
#     def exist(self, word):
#         cur_node = self.root
#         for letter in word:
#             if letter not in cur_node:
#                 return False
#             cur_node = cur_node[letter]
#         return '*' in cur_node
#
#     def startswith(self, prefix):
#         cur_node = self.root
#         for letter in prefix:
#             if letter not in cur_node:
#                 return False
#             cur_node = cur_node[letter]
#         return True

# class TrieNode:
#
#     def __init__(self):
#         self.children = {}
#         self.isEnd = False
# class Trie:
#
#     def __init__(self):
#         self.root = TrieNode()
#
#     def add(self, word):
#         currNode = self.root
#         for char in word:
#             if char not in currNode.children:
#                 currNode.children[char] = TrieNode()
#             currNode = currNode.children[char]
#         currNode.isEnd = True
#
#     def search(self, word):
#         currNode = self.root
#         for char in word:
#             if char not in currNode.children:
#                 return False
#             currNode = currNode.children[char]
#         return currNode.isEnd
#
# t = Trie()
#
# words = ["bad","dad","mad","pad","bad",".ad","b.."]
#
# for word in words:
#     print(f"Searching for words {word}" if "." in word else f"Adding words {word}")
#     t.add(word)
#
# print(t.search("bad"))
# print(t.search("mad"))
# print(t.search(".ad"))
# t.add('shop')
# t.add('hello')
# print(t.startswith('shop'))
# ====================================================================

# Tree Traversals
# from collections import deque, defaultdict
# #
# class Tree:
#
#     def __init__(self):
#         self.graph = defaultdict(list)
#
#     def addEdge(self, u, v):
#         self.graph[u].append(v)
#
#     def bfsTree(self, V, v):
#         level = [0] * (V)
#         visited = [False] * (V)
#         queue = deque()
#         queue.append(v)
#         level[v] = 0
#         visited[v] = True
#
#         while queue:
#             node = queue.popleft()
#             for vertex in self.graph[node]:
#                 adj = vertex
#                 if not visited[adj]:
#                     queue.append(adj)
#                     level[adj] = level[node] + 1
#                     visited[adj] = True
#         print("Nodes", " ", "Level")
#         for i in range(V):
#             print(" ", i,  " --> ", level[i])
#
#
# V = 8
#
# tree = Tree()
# tree.addEdge(0, 0)
# tree.addEdge(0, 2)
# tree.addEdge(1, 3)
# tree.addEdge(1, 4)
# tree.addEdge(1, 5)
# tree.addEdge(2, 5)
# tree.addEdge(2, 6)
# tree.addEdge(6, 7)
#
# # call levels function with source as 0
# tree.bfsTree(V, 0)

# ====================================================================
# Graph Traversals
# Breadth First Search and Depth First Search

# from collections import defaultdict
#
# class Graph:
#
#     def __init__(self):
#         self.graph = defaultdict(list)
#
#     def addEdge(self, u, v):
#         self.graph[u].append(v)
#
#     def bfs(self, s):
#         visited = [False] * (max(self.graph) + 1)
#         queue = []
#         queue.append(s)
#         visited[s] = True
#
#         while queue:
#             s = queue.pop(0)
#             print(s, end=" ")
#
#             for vertex in self.graph[s]:
#                 if visited[vertex] == False:
#                     queue.append(vertex)
#                     visited[vertex] = True
#
#     def dfsUtil(self, v, visited):
#         visited.add(v)
#         print(v, end=" ")
#
#         for vertex in self.graph[v]:
#             if vertex not in visited:
#                 self.dfsUtil(vertex, visited)
#
#     def dfs(self, v):
#         visited = set()
#         self.dfsUtil(v, visited)
#
#
#
# g = Graph()
# g.addEdge(0, 1)
# g.addEdge(0, 2)
# g.addEdge(1, 2)
# g.addEdge(2, 0)
# g.addEdge(2, 3)
# g.addEdge(3, 3)
#
# print("Following is Breadth First Traversal"
#       " (starting from vertex 2)")
# g.bfs(2)
# print()
# print("Following is Depth First Traversal"
#       " (starting from vertex 2)")
# g.dfs(2)

# def DFS(graph, start):
#     visited = set()
#     stack = [start]
#
#     while stack:
#         node = stack.pop()
#         if node not in visited:
#             print(node)  # Process the node
#             visited.add(node)
#             stack.extend([neighbor for neighbor in graph[node] if neighbor not in visited])
#
# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F'],
#     'D': [],
#     'E': ['F'],
#     'F': []
# }
#
# print(DFS(graph, 'A'))

# ====================================================================

# Number of connections possible to make network connected

# from collections import deque, defaultdict
# class Connections:
#
#     def bfs(self, node, adj, visited):
#         queue = deque()
#         queue.append(node)
#         while queue:
#             node = queue.popleft()
#             for vertex in adj[node]:
#                 if not visited[vertex]:
#                     visited[vertex] = True
#                     queue.append(vertex)
#
#     def makeNetwork(self, n, adj):
#         if len(adj) < n - 1:
#             return -1
#
#         graph = defaultdict(dict)
#         for u, v in adj:
#             graph[u][v] = graph[v][u] = u
#
#         connected = 0
#         visited = [False] * n
#         for node in range(n):
#             if not visited[node]:
#                 self.bfs(node, graph, visited)
#                 connected += 1
#
#         return connected - 1
#
# network = Connections()
# print(network.makeNetwork(6, [[0,1],[0,2],[0,3],[1,2],[1,3]]))
# ====================================================================

# Minimum score to a path between two cities

# from collections import defaultdict, deque
#
# class MinCost:
#
#     min_cost = 99999999999
#     def bfs(self, node, graph, n):
#         queue = deque()
#         queue.append(node)
#
#         visited = [False] * (n + 1)
#         visited[node] = True
#
#         while queue:
#             node = queue.popleft()
#             for vertex, score in graph[node].items():
#                 if not visited[vertex]:
#                     queue.append(vertex)
#                     visited[vertex] = True
#                 self.min_cost = min(self.min_cost, score)
#
#     def minCost(self, n: int, roads: list[list]):
#         graph = defaultdict(dict)
#
#         for u, v, w in roads:
#             graph[u][v] = graph[v][u] = w
#
#         self.bfs(1, graph, n)
#
#         return self.min_cost
#
#
# print(MinCost().minCost(4, [[1,2,2],[1,3,4],[3,4,7]]))

# ====================================================================
# Reorder Routes to Make All Paths Lead to the City Zero

# from collections import deque, defaultdict
#
# class Reorder:
#
#     reorder = 0
#     def bfs(self, node, graph, n):
#         queue = deque()
#         queue.append(node)
#
#         visited = [False] * n
#         visited[node] = True
#
#         while queue:
#             node = queue.popleft()
#             for vertex, sign in graph[node]:
#                 if not visited[vertex]:
#                     self.reorder += sign
#                     queue.append(vertex)
#                     visited[vertex] = True
#
#     def reOrder(self, n, paths):
#
#         graph = defaultdict(list)
#         for u, v in paths:
#             graph[u].append((v, 1))
#             graph[v].append((u, 0))
#
#         self.bfs(0, graph, n)
#
#         return self.reorder
#
#
#
# print(Reorder().reOrder(3, [[1,0],[2,0]]))

# ====================================================================

# Count Unreachable Pairs of Nodes in an Undirected Graph

# from collections import deque, defaultdict
#
# class Reorder:
#
#     def bfs(self, node, graph, visited):
#         queue = deque()
#         queue.append(node)
#
#         visited[node] = True
#
#         disconnected = 1
#         while queue:
#             node = queue.popleft()
#             for vertex in graph[node]:
#                 if not visited[vertex]:
#                     queue.append(vertex)
#                     visited[vertex] = True
#                     disconnected += 1
#         return disconnected
#
#     def reOrder(self, n, paths):
#
#         graph = defaultdict(list)
#         for u, v in paths:
#             graph[u].append(v)
#             graph[v].append(u)
#
#
#         visited = [False] * n
#         numberOfPairs, sizeOfComponent, remainingNodes = 0, 0, n
#         for vertex in range(n):
#             if not visited[vertex]:
#                 sizeOfComponent = self.bfs(vertex, graph, visited)
#                 numberOfPairs += sizeOfComponent * (remainingNodes - sizeOfComponent)
#                 remainingNodes -= sizeOfComponent
#
#         return numberOfPairs
#
#
# print(Reorder().reOrder(7, [[0,2],[0,5],[2,4],[1,6],[5,4]]))
# ====================================================================
# Longest Cycle in a graph

# from collections import deque, defaultdict
#
# class LongestCycle:
#
#     ans = -1
#
#     def dfs(self, node, edges, dist, visited):
#         visited[node] = True
#         adj = edges[node]
#
#         if adj != -1 and not visited[adj]:
#             dist[adj] = dist.get(node) + 1
#             self.dfs(adj, edges, dist, visited)
#
#         elif adj != -1 and dist.get(adj):
#             self.ans = max(self.ans, dist.get(node) - dist.get(adj) + 1)
#
#     def longestCycle(self, edges):
#         n = len(edges)
#         visited = [False] * n
#         for vertex in range(n):
#             if not visited[vertex]:
#                 dist = {}
#                 dist[vertex] = 1
#                 self.dfs(vertex, edges, dist, visited)
#
#         return self.ans
#
#
# print(LongestCycle().longestCycle([3,3,4,2,3]))

# ====================================================================

# Disjoint Union Set

# class UnionFind:
#
#     def __init__(self, N):
#         self.parent = [i for i in range(N)]
#         self.rank = [1] * N
#
#     def find(self, p):
#         if p != self.parent[p]:
#             self.parent[p] = self.find(self.parent[p])
#         return self.parent[p]
#
#     def union(self, p, q):
#         p_node, q_node = self.find(p), self.find(q)
#         if p_node == q_node: return False
#         if self.rank[p_node] > self.rank[q_node]:
#             p_node, q_node = q_node, p_node
#         self.parent[p_node] = q_node
#         self.rank[q_node] += self.rank[p_node]
#         return True
#
#
# def distanceLimitedPaths(n, edgeList, queries):
#     queries = sorted((w, p, q, i) for i, (p, q, w) in enumerate(queries))
#     edgeList = sorted((w, u, v) for u, v, w in edgeList)
#
#     uf = UnionFind(n)
#     ans = [None] * len(queries)
#
#     j = 0
#     for w, p, q, i in queries:
#         while j < len(edgeList) and edgeList[j][0] < w:
#             _, u, v = edgeList[j]
#             uf.union(u, v)
#             j += 1
#         ans[i] = uf.find(p) == uf.find(q)
#     return ans
#
#
# print(distanceLimitedPaths(3, [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], [[0,1,2],[0,2,5]]))

# ====================================================================

# Rotting Oranges

# from collections import deque
# def rottingOranges(grid):
#     queue = deque()
#     fresh, time = 0, 0
#
#     rows, cols = len(grid), len(grid[0])
#     for r in range(rows):
#         for c in range(cols):
#             if grid[r][c] == 1:
#                 fresh += 1
#             if grid[r][c] == 2:
#                 queue.append([r, c])
#
#     directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
#     while queue and fresh > 0:
#         for i in range(len(queue)):
#             r, c = queue.popleft()
#             for dr, dc in directions:
#                 row, col = dr + r, dc + c
#                 if row < 0 or row == len(grid) or col < 0 or col == len(grid[0]) or grid[row][col] != 1:
#                     continue
#                 grid[row][col] = 2
#                 queue.append([row, col])
#                 fresh -= 1
#         time += 1
#     return time if fresh == 0 else -1
#
# print(rottingOranges([[2,1,1],[1,1,0],[0,1,1]]))

# ====================================================================

# Pacific Atlantic Water Flow

# def pacificAtlantic(heights):
#     rows, cols = len(heights), len(heights[0])
#     pac, atl = set(), set()
#
#     def dfs(r, c, visited, prevHeight):
#         if (r,c) in visited or r < 0 or c < 0 or r == rows or c == cols or heights[r][c] < prevHeight:
#             return
#         visited.add((r, c))
#         dfs(r + 1, c, visited, heights[r][c])
#         dfs(r - 1, c, visited, heights[r][c])
#         dfs(r, c + 1, visited, heights[r][c])
#         dfs(r, c - 1, visited, heights[r][c])
#
#
#     for c in range(cols):
#         dfs(0, c, pac, heights[0][c])
#         dfs(rows - 1, c, atl, heights[rows - 1][c])
#
#     for r in range(rows):
#         dfs(r, 0, pac, heights[r][0])
#         dfs(r, cols - 1, atl, heights[r][cols - 1])
#
#     res = []
#     for r in range(rows):
#         for c in range(cols):
#             if (r, c) in pac and (r, c) in atl:
#                 res.append([r, c])
#
#     return res
#
#
# print(pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
# ====================================================================

# Similar Strings - Disjoint Set Union Find

# class UnionFind:
#
#     def __init__(self, N):
#         self.parent = [i for i in range(N)]
#         self.rank = [0] * N
#
#     def find(self, x):
#         while x != self.parent[x]:
#             x = self.parent[x]
#         return x
#
#     def union(self, x, y):
#         root1, root2 = self.find(x), self.find(y)
#         if root1 == root2: return
#         if self.rank[root1] > self.rank[root2]:
#             self.parent[root2] = root1
#         else:
#             self.parent[root1] = root2
#             if self.rank[root1] == self.rank[root2]:
#                 self.rank[root2] += 1
#
# def numSimilarGroups(a):
#     n = len(a)
#     uf = UnionFind(n)
#     for i in range(n):
#         for j in range(i + 1, n):
#             if sum(a[i][k] != a[j][k] for k in range(len(a[i]))) in (0, 2):
#                 uf.union(i, j)
#     return len(set(uf.find(i) for i in range(n)))
#
# print(numSimilarGroups(["tars","rats","arts","star"]))
# ====================================================================

# Remove Max Number of Edges to Keep Graph Fully Traversable

# def maxNumEdges(n, edges):
#     root = list(range(n + 1))
#     res, e1, e2 = 0, 0, 0
#     def find(x):
#         if x != root[x]:
#             root[x] = find(root[x])
#         return root[x]
#
#     def union(x, y):
#         x, y = find(x), find(y)
#         if x == y: return 0
#         root[x] = y
#         return 1
#
#     for w, u, v in edges:
#         if w == 3:
#             if union(u, v):
#                 e1 += 1
#                 e2 += 1
#             else:
#                 res += 1
#     root0 = root[:]
#
#     for w, u, v in edges:
#         if w == 1:
#             if union(u, v):
#                 e1 += 1
#             else:
#                 res += 1
#
#     root = root0
#     for w, u, v in edges:
#         if w == 2:
#             if union(u, v):
#                 e2 += 1
#             else:
#                 res += 1
#
#     return res if e1 == e2 == n - 1 else -1
#
# print(maxNumEdges(4, [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]))

# # Search Suggestion Systems
# from collections import defaultdict
# class TrieNode:
#
#     def __init__(self):
#         self.children = defaultdict(TrieNode)
#         self.suggest = []
#
#     def addSuggestion(self, product):
#         if len(self.suggest) < 3:
#             self.suggest.append(product)
#
# def suggestProduct(products, searchWord):
#     products.sort()
#     root = TrieNode()
#     for prod in products:
#         currNode = root
#         for char in prod:
#             currNode = currNode.children[char]
#             currNode.addSuggestion(prod)
#
#     res, curr = [], root
#     for char in searchWord:
#         curr = curr.children[char]
#         res.append(curr.suggest)
#     return res
#
# print(suggestProduct(["mobile","mouse","moneypot","monitor","mousepad"], "mouse"))

# ====================================================================
# Evaluate division
# from typing import List
# from collections import defaultdict, deque
# def evalDivision(equations: List[List[str]], values: List[float], queries: List[List[str]]):
#     graph = defaultdict(dict)
#     for (x, y), val in zip(equations, values):
#         graph[x][y] = val
#         graph[y][x] = 1 / val
#
#     def dfs(x, y, visited):
#         if x not in graph or y not in graph: return -1.0
#
#         if y in graph[x]: return graph[x][y]
#         for vals in graph[x]:
#             if vals not in visited:
#                 visited.add(vals)
#                 temp = dfs(vals, y, visited)
#                 if temp == -1: continue
#                 else: return temp * graph[x][vals]
#         return -1
#
#     res = []
#     for query in queries:
#         res.append(dfs(query[0], query[1], set()))
#     return res
#
# print(evalDivision(equations = [["a","b"],["b","c"]],
#                    values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))

# ====================================================================
# Course Schedule
# from collections import defaultdict
#
# def courseSchedule(numCourses, prerequisites):
#     courseMap = defaultdict(list)
#     for crs, pre in prerequisites:
#         courseMap[crs].append(pre)
#
#     visited = set()
#     def dfs(crs):
#         if crs in visited: return False
#         if courseMap[crs] is []: return True
#         visited.add(crs)
#         for pre in courseMap[crs]:
#             if not dfs(pre): return False
#         visited.remove(crs)
#         courseMap[crs] = []
#         return True
#
#     for crs in range(numCourses):
#         if not dfs(crs): return False
#     return True
#
#
# print(courseSchedule(2, [[0, 1]]))
