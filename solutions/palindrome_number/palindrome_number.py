class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


def main():
    solution = Solution()
    print(-121, solution.isPalindrome(-121))


if __name__ == '__main__':
    main()
