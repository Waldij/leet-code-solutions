from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = sum(nums[:3])
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]: continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum_ = sum((nums[i], nums[left], nums[right]))
                if sum_ == target:
                    return sum_
                if abs(sum_ - target) < abs(closest - target):
                    closest = sum_
                if sum_ < target:
                    left += 1
                else:
                    right -= 1
        return closest


def main():
    pass


if __name__ == '__main__':
    main()
