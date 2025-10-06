import heapq

class Solution:
    def swimInWater(self, grid):
        n = len(grid)
        visited = [[False]*n for _ in range(n)]
        min_heap = [(grid[0][0], 0, 0)]  # (elevation, x, y)
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        max_elevation = 0

        while min_heap:
            elevation, x, y = heapq.heappop(min_heap)
            max_elevation = max(max_elevation, elevation)
            if x == n-1 and y == n-1:
                return max_elevation
            visited[x][y] = True
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    heapq.heappush(min_heap, (grid[nx][ny], nx, ny))
                    visited[nx][ny] = True
