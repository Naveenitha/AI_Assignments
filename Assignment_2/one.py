import heapq
import math

# 8 directions: horizontal, vertical, diagonal
directions = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),          (0, 1),
              (1, -1),  (1, 0), (1, 1)]

# Heuristic: Euclidean distance
def heuristic(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

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


# ------------------- Testing -------------------
if __name__ == "__main__":
    grid = [[0, 0, 0],
            [1, 1, 0],
            [1, 1, 0]]

    length, path = best_first_search(grid)
    print("Best First Search → Path length:", length, "Path:", path if length != -1 else "No Path")
