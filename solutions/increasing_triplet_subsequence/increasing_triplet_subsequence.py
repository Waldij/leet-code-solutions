from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False

    def increasingTriplet_(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                for k in range(j, len(nums)):
                    if nums[i] < nums[j] < nums[k]:
                        return True
        return False


def main():
    solution = Solution()

    nums = [1, 2, 3, 4, 5]
    assert solution.increasingTriplet(nums) is True

    nums = [5, 4, 3, 2, 1]
    assert solution.increasingTriplet(nums) is False

    nums = [2, 1, 5, 0, 4, 6]
    assert solution.increasingTriplet(nums) is True

    nums = [20, 100, 10, 12, 5, 13]
    assert solution.increasingTriplet(nums) is True


if __name__ == '__main__':
    main()
