class Solution:
    def isValid(self, s: str) -> bool:
        brackets = ('()', '[]', '{}')
        while any([pair in s for pair in brackets]):
            for pair in brackets:
                if pair in s:
                    s = s.replace(pair, '')
        return not bool(s)


def main():
    solution = Solution()
    s = '()[()]{[()()]}'
    print(s, solution.isValid(s))


if __name__ == '__main__':
    main()
