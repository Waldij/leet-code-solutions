from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """Intuitive"""
        enumerated = [x for x in enumerate(height)]
        max_amount = 0
        for i in range(len(enumerated)):
            for j in enumerated[0:i] + enumerated[i+1:]:
                height_am = min(enumerated[i][1], j[1])
                len_am = abs(enumerated[i][0] - j[0])
                amount = height_am * len_am
                max_amount = amount if amount > max_amount else max_amount

        return max_amount

    def maxArea1(self, height: List[int]) -> int:
        """Two pointer solution"""
        left = 0
        right = len(height) - 1
        max_amount = 0
        while left < right:
            amount = (right - left) * min(height[left], height[right])
            max_amount = amount if amount > max_amount else max_amount
            if height[left] <= height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
        return max_amount


def main():
    a = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    solution = Solution()
    print(solution.maxArea1(a))


if __name__ == '__main__':
    main()
