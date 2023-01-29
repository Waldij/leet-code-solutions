from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        raw = []
        for _ in range(rowIndex):
            raw = [1] + [raw[i] + raw[i + 1] for i in range(len(raw) - 1)] + [1]
        return raw


def main():
    solution = Solution()
    print(solution.getRow(24))


if __name__ == '__main__':
    main()
