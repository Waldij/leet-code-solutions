from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest = min(strs, key=lambda x: len(x))
        for i in range(len(smallest), 0, -1):
            if all([str_.startswith(smallest[:i]) for str_ in strs]):
                return smallest[:i]
        return ''


def main():
    solution = Solution()
    strs = ["reflower","flow","flight"]
    print(strs, solution.longestCommonPrefix(strs))


if __name__ == '__main__':
    main()
