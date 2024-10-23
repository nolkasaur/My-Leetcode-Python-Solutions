# https://leetcode.com/problems/number-of-islands/
# 316 ms, 24.33 MB

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        res = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def bfs(r, c):
            queue = deque()
            visited.add((r, c))
            queue.append((r, c))
            while queue:
                row, col = queue.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]] # right, left, up, down
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r, c) not in visited:
                        queue.append((r, c))
                        visited.add((r, c))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    res += 1
        return res
