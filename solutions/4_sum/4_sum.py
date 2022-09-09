from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """Based on Two pointers solution"""
        variants = []
        nums = sorted(nums)

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    qad = [nums[i], nums[j], nums[left], nums[right]]
                    if sum(qad) == target:
                        if qad not in variants:
                            variants.append(qad)
                        left += 1
                    elif sum(qad) < target:
                        left += 1
                    else:
                        right -= 1
        return variants

    def fourSum1(self, nums: List[int], target: int) -> List[List[int]]:
        """Intuitive"""
        nums.sort()
        variants = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    for l in range(k + 1, len(nums)):
                        tmp = [nums[i], nums[j], nums[k], nums[l]]
                        if tmp in variants:
                            continue
                        if sum(tmp) == target:
                            variants.append(tmp)
        return variants


def main():
    solution = Solution()
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    print(nums, target)
    print(solution.fourSum(nums, target))

    nums = [2, 2, 2, 2, 2]
    target = 8
    print(nums, target)
    print(solution.fourSum(nums, target))


if __name__ == '__main__':
    main()
