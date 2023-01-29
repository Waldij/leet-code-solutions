from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        right_most = {c: i for i, c in enumerate(s)}
        left, right = 0, 0
        result = []
        for i, letter in enumerate(s):
            right = max(right, right_most[letter])
            if i == right:
                result += [right - left + 1]
                left = i + 1
        return result


def main():
    solution = Solution()

    s = "ababcbacadefegdehijhklij"
    assert solution.partitionLabels(s) == [9, 7, 8]


if __name__ == '__main__':
    main()
