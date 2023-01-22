from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]


def main():
    solution = Solution()
    nums = [2, 2, 1, 1, 1, 2, 2]
    assert solution.majorityElement(nums) == 2


if __name__ == '__main__':
    main()
