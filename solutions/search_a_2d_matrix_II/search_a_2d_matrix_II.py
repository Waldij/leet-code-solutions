from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """Beats 99%"""
        for row in matrix[::-1]:
            if row[0] <= target:
                if target in row:
                    return True
        return False

    def searchMatrix_ez(self, matrix: List[List[int]], target: int) -> bool:
        return any([target in row for row in matrix])


def main():
    solution = Solution()

    matrix = [[1, 4, 7, 11, 15],
              [2, 5, 8, 12, 19],
              [3, 6, 9, 16, 22],
              [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]]
    assert solution.searchMatrix(matrix, target=5) is True
    assert solution.searchMatrix(matrix, target=20) is False


if __name__ == '__main__':
    main()
