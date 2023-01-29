from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        previous_end, counter = None, 0
        for start, end in intervals:
            if not previous_end or start >= previous_end:
                previous_end = end
            else:
                counter += 1
        return counter


def main():
    solution = Solution()

    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    assert solution.eraseOverlapIntervals(intervals) == 1

    intervals = [[1, 2], [1, 2], [1, 2]]
    assert solution.eraseOverlapIntervals(intervals) == 2

    intervals = [[1, 2], [2, 3]]
    assert solution.eraseOverlapIntervals(intervals) == 0

    intervals = [[1, 100], [11, 22], [1, 11], [2, 12]]
    assert solution.eraseOverlapIntervals(intervals) == 2


if __name__ == '__main__':
    main()
