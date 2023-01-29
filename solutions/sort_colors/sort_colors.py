from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j, k = 0, 0, len(nums) - 1
        while j <= k:
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
                i += 1
            elif nums[j] == 1:
                j += 1
            else:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1


def main():
    solution = Solution()

    nums = [2, 0, 2, 1, 1, 0]
    solution.sortColors(nums)
    assert nums == [0, 0, 1, 1, 2, 2]

    nums = [2, 0, 1]
    solution.sortColors(nums)
    assert nums == [0, 1, 2]


if __name__ == '__main__':
    main()
