from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        cycle = (self.cut_top, self.cut_right, self.cut_bottom, self.cut_left)
        res = []
        step = 0
        while not self.matrix_is_empty(matrix):
            res += cycle[step](matrix)
            step = step + 1 if step < 3 else 0
        return res

    def matrix_is_empty(self, matrix: List[List[int]]) -> bool:
        return all([not bool(row) for row in matrix])

    def cut_top(self, matrix: List[List[int]]) -> list[int]:
        return matrix.pop(0)

    def cut_right(self, matrix: List[List[int]]) -> list[int]:
        return [row.pop(-1) for row in matrix]

    def cut_bottom(self, matrix: List[List[int]]) -> list[int]:
        return matrix.pop()[::-1]

    def cut_left(self, matrix: List[List[int]]) -> list[int]:
        return [row.pop(0) for row in matrix][::-1]


def main():
    solution = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert solution.spiralOrder(matrix) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    assert solution.spiralOrder(matrix) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6,
                                            7]
    matrix = [[7], [9], [6]]
    assert solution.spiralOrder(matrix) == [7, 9, 6]


if __name__ == '__main__':
    main()
