1. Array & String Coding Questions
1. Find the second-largest unique element without using sort() or max().
def second_largest(arr):
    largest = None
    second = None

    for num in arr:
        if largest is None or num > largest:
            second = largest
            largest = num

        elif num != largest and (second is None or num > second):
            second = num

    return second

arr = [10, 20, 40, 30, 50, 50]

print("Second largest:", second_largest(arr))


2. Find all pairs in an array whose sum equals a given target.
def find_pairs(arr, target):
    seen = set()
    pairs = set()

    for num in arr:
        complement = target - num

        if complement in seen:
            pairs.add((min(num, complement),
                       max(num, complement)))

        seen.add(num)

    return list(pairs)

arr = [2, 4, 3, 5, 7, 8, 1]
target = 9

print(find_pairs(arr, target))


3. Move all zeros to the end without changing the order of other elements.
def move_zeros(arr):
    result = []

    for num in arr:
        if num != 0:
            result.append(num)

    zeros = len(arr) - len(result)

    result.extend([0] * zeros)

    return result

arr = [0, 1, 0, 3, 12]

print(move_zeros(arr))


4. Find the missing number from an array containing numbers from 1 to N.
def missing_number(arr, n):
    expected = n * (n + 1) // 2
    actual = sum(arr)

    return expected - actual

arr = [1, 2, 4, 5, 6]
n = 6

print("Missing number:", missing_number(arr, n))


5. Find all duplicate elements without using nested loops.
def find_duplicates(arr):
    seen = set()
    duplicates = set()

    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates)

arr = [1, 2, 3, 2, 4, 5, 3, 6]

print(find_duplicates(arr))


6. Find the first non-repeating character in a string.
def first_non_repeating(text):
    frequency = {}

    for char in text:
        frequency[char] = frequency.get(char, 0) + 1

    for char in text:
        if frequency[char] == 1:
            return char

    return None

text = "swiss"

print(first_non_repeating(text))


7. Check whether two strings are anagrams without using sorted().
def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False

    frequency = {}

    for char in s1:
        frequency[char] = frequency.get(char, 0) + 1

    for char in s2:
        if char not in frequency:
            return False

        frequency[char] -= 1

        if frequency[char] < 0:
            return False

    return True

print(are_anagrams("listen", "silent"))


8. Merge two sorted arrays without using sort().
def merge_arrays(a, b):
    i = 0
    j = 0
    result = []

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    result.extend(a[i:])
    result.extend(b[j:])

    return result

a = [1, 3, 5, 7]
b = [2, 4, 6, 8]

print(merge_arrays(a, b))


9. Rotate an array to the right by K positions.
def rotate_array(arr, k):
    if not arr:
        return []

    k = k % len(arr)

    return arr[-k:] + arr[:-k] if k else arr.copy()

arr = [1, 2, 3, 4, 5]

print(rotate_array(arr, 2))


10. Find the intersection of two arrays, including duplicate occurrences.
from collections import Counter

def intersection(a, b):
    count = Counter(a)
    result = []

    for num in b:
        if count[num] > 0:
            result.append(num)
            count[num] -= 1

    return result

a = [1, 2, 2, 3, 4]
b = [2, 2, 3, 5]

print(intersection(a, b))


11. Find the maximum sum of a contiguous subarray.
Using Kadane's Algorithm:
def max_subarray(arr):
    current = arr[0]
    maximum = arr[0]

    for num in arr[1:]:
        current = max(num, current + num)
        maximum = max(maximum, current)

    return maximum

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print("Maximum sum:", max_subarray(arr))


12. Find the longest substring without repeating characters.
def longest_substring(text):
    seen = {}
    left = 0
    maximum = 0

    for right, char in enumerate(text):
        if char in seen and seen[char] >= left:
            left = seen[char] + 1

        seen[char] = right

        maximum = max(maximum, right - left + 1)

    return maximum

text = "abcabcbb"

print(longest_substring(text))


13. Find the longest common prefix among multiple strings.
def common_prefix(words):
    if not words:
        return ""

    prefix = words[0]

    for word in words[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]

            if not prefix:
                return ""

    return prefix

words = ["flower", "flow", "flight"]

print(common_prefix(words))


14. Group a list of strings into anagram groups.
from collections import defaultdict

def group_anagrams(words):
    groups = defaultdict(list)

    for word in words:
        key = tuple(sorted(word))
        groups[key].append(word)

    return list(groups.values())

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(group_anagrams(words))


15. Find the Kth largest element in an unsorted array.
import heapq

def kth_largest(arr, k):
    if k < 1 or k > len(arr):
        return None

    heap = []

    for num in arr:
        heapq.heappush(heap, num)

        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]

arr = [3, 2, 1, 5, 6, 4]

print(kth_largest(arr, 2))


16. Check whether a given string contains balanced parentheses using a stack.
def balanced(text):
    stack = []

    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in text:
        if char in "({[":
            stack.append(char)

        elif char in ")}]":
            if not stack or stack.pop() != pairs[char]:
                return False

    return len(stack) == 0

text = "{[()]}"

print(balanced(text))


17. Find all subarrays whose sum equals a given target.
def find_subarrays(arr, target):
    result = []

    for start in range(len(arr)):
        total = 0

        for end in range(start, len(arr)):
            total += arr[end]

            if total == target:
                result.append(arr[start:end + 1])

    return result

arr = [1, 2, 3, 2, 1]
target = 3

print(find_subarrays(arr, target))


18. Merge overlapping intervals in a list.
def merge_intervals(intervals):
    if not intervals:
        return []

    intervals = sorted(intervals)

    result = [intervals[0]]

    for start, end in intervals[1:]:
        last = result[-1]

        if start <= last[1]:
            last[1] = max(last[1], end)
        else:
            result.append([start, end])

    return result

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

print(merge_intervals(intervals))


19def search_rotated(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1

        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

arr = [4, 5, 6, 7, 0, 1, 2]

print(search_rotated(arr, 0))


20. Find the longest consecutive sequence in an unsorted array.
def longest_consecutive(arr):
    nums = set(arr)
    longest = 0

    for num in nums:
        if num - 1 not in nums:
            current = num
            length = 1

            while current + 1 in nums:
                current += 1
                length += 1

            longest = max(longest, length)

    return longest

arr = [100, 4, 200, 1, 3, 2]

print(longest_consecutive(arr))


2. Advanced Array & Dynamic Programming
21. Find the trapped rainwater between elevation bars.
Using the Two Pointer Approach
def trap_water(height):
    left = 0
    right = len(height) - 1

    left_max = 0
    right_max = 0
    water = 0

    while left < right:
        if height[left] < height[right]:

            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]

            left += 1

        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]

            right -= 1

    return water


arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

print("Trapped water:", trap_water(arr))


22. Find the median of two sorted arrays in O(log(m+n)) time.
Using Binary Search:
def find_median(a, b):
    if len(a) > len(b):
        return find_median(b, a)

    m = len(a)
    n = len(b)

    left = 0
    right = m

    while left <= right:
        partition_a = (left + right) // 2
        partition_b = (m + n + 1) // 2 - partition_a

        max_left_a = float('-inf') if partition_a == 0 else a[partition_a - 1]
        min_right_a = float('inf') if partition_a == m else a[partition_a]

        max_left_b = float('-inf') if partition_b == 0 else b[partition_b - 1]
        min_right_b = float('inf') if partition_b == n else b[partition_b]

        if max_left_a <= min_right_b and max_left_b <= min_right_a:

            if (m + n) % 2 == 0:
                return (max(max_left_a, max_left_b) +
                        min(min_right_a, min_right_b)) / 2

            return max(max_left_a, max_left_b)

        elif max_left_a > min_right_b:
            right = partition_a - 1

        else:
            left = partition_a + 1

    raise ValueError("Input arrays must be sorted")


a = [1, 3]
b = [2]

print("Median:", find_median(a, b))


23. Find the maximum product of a contiguous subarray.
def max_product(arr):
    maximum = arr[0]
    minimum = arr[0]
    result = arr[0]

    for num in arr[1:]:

        if num < 0:
            maximum, minimum = minimum, maximum

        maximum = max(num, maximum * num)
        minimum = min(num, minimum * num)

        result = max(result, maximum)

    return result


arr = [2, 3, -2, 4]

print("Maximum product:", max_product(arr))


24. Find the smallest missing positive integer from an unsorted array.
def smallest_missing(arr):
    nums = set(arr)

    num = 1

    while num in nums:
        num += 1

    return num


arr = [3, 4, -1, 1]

print("Smallest missing:", smallest_missing(arr))


25. Count the number of subarrays whose sum equals K.
Using Prefix Sum and Dictionary:
def count_subarrays(arr, k):
    prefix_sum = 0
    count = 0

    frequency = {0: 1}

    for num in arr:
        prefix_sum += num

        required = prefix_sum - k

        count += frequency.get(required, 0)

        frequency[prefix_sum] = frequency.get(prefix_sum, 0) + 1

    return count


arr = [1, 2, 3, -2, 2]
k = 3

print("Number of subarrays:", count_subarrays(arr, k))


26. Find the longest increasing subsequence in an array.
Using Dynamic Programming:
def longest_increasing(arr):
    if not arr:
        return 0

    dp = [1] * len(arr)

    for i in range(len(arr)):
        for j in range(i):

            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


arr = [10, 9, 2, 5, 3, 7, 101, 18]

print("LIS length:", longest_increasing(arr))


27. Solve the Coin Change problem using Dynamic Programming.
Find the minimum number of coins required to make a given amount.
def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)

    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):

            dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[amount] == float('inf'):
        return -1

    return dp[amount]


coins = [1, 2, 5]
amount = 11

print("Minimum coins:", coin_change(coins, amount))


28. Solve the Word Break problem using Dynamic Programming.
Check whether a string can be divided into valid dictionary words.
def word_break(text, dictionary):
    words = set(dictionary)

    dp = [False] * (len(text) + 1)

    dp[0] = True

    for i in range(1, len(text) + 1):

        for j in range(i):

            if dp[j] and text[j:i] in words:
                dp[i] = True
                break

    return dp[len(text)]


text = "applepenapple"

dictionary = ["apple", "pen"]

print(word_break(text, dictionary))


29. Find the minimum number of jumps required to reach the last index.
def min_jumps(arr):
    n = len(arr)

    if n <= 1:
        return 0

    if arr[0] == 0:
        return -1

    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(n - 1):

        farthest = max(farthest, i + arr[i])

        if i == current_end:

            if farthest == current_end:
                return -1

            jumps += 1
            current_end = farthest

            if current_end >= n - 1:
                return jumps

    return -1


arr = [2, 3, 1, 1, 4]

print("Minimum jumps:", min_jumps(arr))


30. Find the maximum profit from buying and selling stocks with multiple transactions.
def max_profit(prices):
    profit = 0

    for i in range(1, len(prices)):

        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]

    return profit


prices = [7, 1, 5, 3, 6, 4]

print("Maximum profit:", max_profit(prices))


3. Data Structures – Stack, Cache & Graphs
31. Implement an LRU Cache with O(1) time complexity for get() and put().
LRU means Least Recently Used. It removes the least recently accessed item when the cache becomes full.
from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):

        if key not in self.cache:
            return -1

        self.cache.move_to_end(key)

        return self.cache[key]

    def put(self, key, value):

        if key in self.cache:
            self.cache.move_to_end(key)

        self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


cache = LRUCache(2)

cache.put(1, 100)
cache.put(2, 200)

print(cache.get(1))

cache.put(3, 300)

print(cache.get(2))
print(cache.get(3))


32. Implement a Min Stack that supports push(), pop(), top() and getMin() in O(1).
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):
        self.stack.append(value)

        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        if not self.stack:
            return None

        value = self.stack.pop()

        if value == self.min_stack[-1]:
            self.min_stack.pop()

        return value

    def top(self):
        if not self.stack:
            return None

        return self.stack[-1]

    def getMin(self):
        if not self.min_stack:
            return None

        return self.min_stack[-1]


s = MinStack()

s.push(5)
s.push(3)
s.push(7)
s.push(2)

print("Minimum:", s.getMin())

s.pop()

print("Top:", s.top())
print("Minimum:", s.getMin())


33. Find the number of islands in a 2D matrix using DFS.
An island is a group of connected land cells represented by 1. Here, horizontal and vertical connections count.
def count_islands(grid):
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    visited = set()

    def dfs(r, c):

        if (r < 0 or r >= rows or
            c < 0 or c >= cols or
            grid[r][c] == 0 or
            (r, c) in visited):
            return

        visited.add((r, c))

        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    count = 0

    for r in range(rows):
        for c in range(cols):

            if grid[r][c] == 1 and (r, c) not in visited:
                count += 1
                dfs(r, c)

    return count


grid = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [0, 0, 1, 0, 1],
    [0, 0, 0, 1, 1]
]

print("Number of islands:", count_islands(grid))


34. Find the shortest path in a weighted graph using Dijkstra's algorithm.
import heapq

def dijkstra(graph, start):

    distances = {node: float('inf') for node in graph}

    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:

        distance, node = heapq.heappop(priority_queue)

        if distance > distances[node]:
            continue

        for neighbor, weight in graph[node].items():

            new_distance = distance + weight

            if new_distance < distances[neighbor]:

                distances[neighbor] = new_distance

                heapq.heappush(
                    priority_queue,
                    (new_distance, neighbor)
                )

    return distances


graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8},
    'D': {'B': 5, 'C': 8}
}

print(dijkstra(graph, 'A'))


35. Detect a cycle in a directed and undirected graph.
A. Directed graph – DFS
def has_cycle_directed(graph):

    visited = set()
    path = set()

    def dfs(node):

        visited.add(node)
        path.add(node)

        for neighbor in graph[node]:

            if neighbor not in visited:
                if dfs(neighbor):
                    return True

            elif neighbor in path:
                return True

        path.remove(node)

        return False

    for node in graph:
        if node not in visited:
            if dfs(node):
                return True

    return False


graph = {
    0: [1],
    1: [2],
    2: [0],
    3: []
}

print(has_cycle_directed(graph))

B. Undirected graph – DFS
def has_cycle_undirected(graph):

    visited = set()

    def dfs(node, parent):

        visited.add(node)

        for neighbor in graph[node]:

            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True

            elif neighbor != parent:
                return True

        return False

    for node in graph:
        if node not in visited:
            if dfs(node, None):
                return True

    return False


graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1],
    3: []
}

print(has_cycle_undirected(graph))


36. Implement topological sorting for a directed acyclic graph.
Using Kahn's Algorithm:
from collections import deque

def topological_sort(graph):

    indegree = {node: 0 for node in graph}

    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1

    queue = deque()

    for node in graph:
        if indegree[node] == 0:
            queue.append(node)

    result = []

    while queue:

        node = queue.popleft()

        result.append(node)

        for neighbor in graph[node]:

            indegree[neighbor] -= 1

            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(result) != len(graph):
        return None

    return result


graph = {
    5: [2, 0],
    4: [0, 1],
    2: [3],
    3: [1],
    1: [],
    0: []
}

print(topological_sort(graph))


4. Backtracking & Binary Trees
37. Solve the N-Queens problem using backtracking.
The N-Queens problem places N queens on an N × N chessboard so that no two queens attack each other.
def solve_n_queens(n):

    board = [["."] * n for _ in range(n)]

    solutions = []

    columns = set()
    diagonal1 = set()
    diagonal2 = set()

    def backtrack(row):

        if row == n:
            solutions.append(
                ["".join(line) for line in board]
            )
            return

        for col in range(n):

            if (col in columns or
                row - col in diagonal1 or
                row + col in diagonal2):
                continue

            board[row][col] = "Q"

            columns.add(col)
            diagonal1.add(row - col)
            diagonal2.add(row + col)

            backtrack(row + 1)

            board[row][col] = "."

            columns.remove(col)
            diagonal1.remove(row - col)
            diagonal2.remove(row + col)

    backtrack(0)

    return solutions


solutions = solve_n_queens(4)

print("Total solutions:", len(solutions))

for solution in solutions:
    for row in solution:
        print(row)
    print()


38. Generate all permutations of a given string or array without duplicates.
def permutations(arr):

    arr = sorted(arr)

    result = []
    used = [False] * len(arr)

    def backtrack(path):

        if len(path) == len(arr):
            result.append(path.copy())
            return

        for i in range(len(arr)):

            if used[i]:
                continue

            if i > 0 and arr[i] == arr[i - 1] and not used[i - 1]:
                continue

            used[i] = True

            path.append(arr[i])

            backtrack(path)

            path.pop()

            used[i] = False

    backtrack([])

    return result


arr = [1, 1, 2]

print(permutations(arr))


39. Serialize and deserialize a binary tree.
Serialization converts a binary tree into a string. Deserialization reconstructs the original tree.
class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def serialize(root):

    values = []

    def dfs(node):

        if node is None:
            values.append("#")
            return

        values.append(str(node.value))

        dfs(node.left)
        dfs(node.right)

    dfs(root)

    return ",".join(values)


def deserialize(data):

    values = iter(data.split(","))

    def dfs():

        value = next(values)

        if value == "#":
            return None

        node = Node(int(value))

        node.left = dfs()
        node.right = dfs()

        return node

    return dfs()


# Create a binary tree

root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.right.left = Node(4)
root.right.right = Node(5)

# Serialize

data = serialize(root)

print("Serialized:", data)

# Deserialize

new_root = deserialize(data)

print("Deserialized root:", new_root.value)


40. Find the lowest common ancestor of two nodes in a binary tree.
The Lowest Common Ancestor (LCA) is the lowest node that has both given nodes as descendants.
class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def lowest_common_ancestor(root, p, q):

    if root is None:
        return None

    if root == p or root == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)

    right = lowest_common_ancestor(root.right, p, q)

    if left and right:
        return root

    return left if left else right


# Create binary tree

root = Node(3)

root.left = Node(5)
root.right = Node(1)

root.left.left = Node(6)
root.left.right = Node(2)

root.right.left = Node(0)
root.right.right = Node(8)

p = root.left
q = root.right

result = lowest_common_ancestor(root, p, q)

if result:
    print("Lowest Common Ancestor:", result.value)
else:
    print("LCA not found")





















































