from typing import List


class Solution:

    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[int]:
        indexed = sorted(list(enumerate(nums)), key=lambda x: x[1])
        left, right = 0, (len(nums) - 1)
        while left < right:
            if indexed[left][1] + indexed[right][1] == target:
                return [indexed[left][0], indexed[right][0]]
            elif (indexed[left][1] + indexed[right][1]) < target:
                left += 1
            elif (indexed[left][1] + indexed[right][1]) > target:
                right -= 1

    @staticmethod
    def two_sum_hashmap(nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[nums[i]] = i


def main():
    func = Solution.two_sum_hashmap

    a = [2, 7, 11, 15]
    print(func(a, 9))

    a = [3, 2, 4]
    print(func(a, 6))

    a = [3, 3]
    print(func(a, 6))


if __name__ == '__main__':
    main()
