from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for val in nums:
            xor ^= val
            print(xor)
        return xor

    def singleNumber1(self, nums: List[int]) -> int:
        hashset = set()
        for val in nums:
            if val not in hashset:
                hashset.add(val)
            else:
                hashset.remove(val)
        return hashset.pop()


def main():
    solution = Solution()
    nums = [4, 4, 5, 5, 1, 2, 2, 1, 7, 8, 8]
    print(nums, solution.singleNumber(nums))


if __name__ == '__main__':
    main()
