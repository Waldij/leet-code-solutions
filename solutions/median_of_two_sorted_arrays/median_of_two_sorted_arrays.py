from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        from statistics import median
        return median(nums1 + nums2)


def main():
    solution = Solution()
    a = [1, 2]
    b = [3, 4]
    print(solution.findMedianSortedArrays(a, b))


if __name__ == '__main__':
    main()
