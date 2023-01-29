from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged


def main():
    solution = Solution()

    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    assert solution.merge(intervals) == [[1, 6], [8, 10], [15, 18]]

    intervals = [[1, 4], [4, 5]]
    assert solution.merge(intervals) == [[1, 5]]


if __name__ == '__main__':
    main()
