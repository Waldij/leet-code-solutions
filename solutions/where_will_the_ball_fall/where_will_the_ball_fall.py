from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        n_rows = len(grid)
        n_cols = len(grid[0])

        def candrop(i, j):
            # Ball falls out of bottom
            if i == n_rows: return j
            # Ball hits right wall due to a lr-leaning
            if j == n_cols - 1 and grid[i][j] == 1: return -1
            # Ball hits left wall due to a rl-leaning
            if j == 0 and grid[i][j] == -1: return -1
            # Ball lands in a V after rolling right
            if grid[i][j] == 1 and grid[i][j + 1] == -1: return -1
            # Ball lands in a V after rolling left
            if grid[i][j] == -1 and grid[i][j - 1] == 1: return -1
            # No end case, continue by increasing y-coord by one and
            # x-coord by 1 or -1 depending on roll direction.
            return candrop(i + 1, j + grid[i][j])

        return [candrop(0, j) for j in range(n_cols)]

def main():
    solution = Solution()
    grid = [[1, 1, 1, -1, -1],
            [1, 1, 1, -1, -1],
            [-1, -1, -1, 1, 1],
            [1, 1, 1, 1, -1],
            [-1, -1, -1, -1, -1]]
    assert solution.findBall(grid) == [1, -1, -1, -1, -1]


if __name__ == '__main__':
    main()
