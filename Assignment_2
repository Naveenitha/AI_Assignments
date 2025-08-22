import heapq
import math

# 8 possible moves (horizontal, vertical, diagonal)
directions = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),          (0, 1),
              (1, -1),  (1, 0), (1, 1)]

# Heuristic: Euclidean Distance
def heuristic(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# -------------------------------
# Part A: Best First Search (Greedy)
# -------------------------------
def best_first_search(grid):
    n = len(grid)
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1, []

    pq = [(heuristic(0, 0, n-1, n-1), 0, 0, [(0, 0)])]  # (h, x, y, path)
    visited = set()

    while pq:
        h, x, y, path = heapq.heappop(pq)
        if (x, y) in visited:
            continue
        visited.add((x, y))

        if (x, y) == (n-1, n-1):
            return len(path), path

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0 and (nx, ny) not in visited:
                new_h = heuristic(nx, ny, n-1, n-1)
                heapq.heappush(pq, (new_h, nx, ny, path + [(nx, ny)]))

    return -1, []


# -------------------------------
# Part B: A* Search
# -------------------------------
def a_star_search(grid):
    n = len(grid)
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1, []

    pq = [(heuristic(0, 0, n-1, n-1), 0, 0, 0, [(0, 0)])]  # (f, g, x, y, path)
    visited = set()

    while pq:
        f, g, x, y, path = heapq.heappop(pq)
        if (x, y) in visited:
            continue
        visited.add((x, y))

        if (x, y) == (n-1, n-1):
            return len(path), path

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0 and (nx, ny) not in visited:
                new_g = g + 1
                new_f = new_g + heuristic(nx, ny, n-1, n-1)
                heapq.heappush(pq, (new_f, new_g, nx, ny, path + [(nx, ny)]))

    return -1, []


# -------------------------------
# Testing with given examples
# -------------------------------
test_cases = [
    [[0, 1],
     [1, 0]],

    [[0, 0, 0],
     [1, 1, 0],
     [1, 1, 0]],

    [[1, 0, 0],
     [1, 1, 0],
     [1, 1, 0]]
]

for i, grid in enumerate(test_cases, 1):
    bfs_len, bfs_path = best_first_search(grid)
    a_len, a_path = a_star_search(grid)

    print(f"\nExample {i}:")
    print(f"Best First Search  → Path length: {bfs_len}, Path: {bfs_path if bfs_len != -1 else ''}")
    print(f"A* Search          → Path length: {a_len}, Path: {a_path if a_len != -1 else ''}")
