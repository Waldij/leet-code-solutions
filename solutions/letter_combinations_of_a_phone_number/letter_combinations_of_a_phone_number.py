from typing import List
from functools import reduce


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digits_letters_map = {
            '2': ('a', 'b', 'c'),
            '3': ('d', 'e', 'f'),
            '4': ('g', 'h', 'i'),
            '5': ('j', 'k', 'l'),
            '6': ('m', 'n', 'o'),
            '7': ('p', 'q', 'r', 's'),
            '8': ('t', 'u', 'v'),
            '9': ('w', 'x', 'y', 'z'),
        }
        variants = tuple(digits_letters_map[digit] for digit in digits)
        combinations = reduce(lambda x, y: tuple(i + j for i in x for j in y), variants)
        return list(combinations)


def main():
    solution = Solution()
    digits = '27'
    print(digits, solution.letterCombinations(digits))


if __name__ == '__main__':
    main()
