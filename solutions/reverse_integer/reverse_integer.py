class Solution:
    def reverse(self, x: int) -> int:
        sign = '-' if x < 0 else ''
        reversed_ = int(sign + str(abs(x))[::-1])
        if reversed_ > (2 ** 31) - 1 or reversed_ < - (2 ** 31):
            return 0
        return reversed_


def main():
    solution = Solution()
    print(solution.reverse(-320))


if __name__ == '__main__':
    main()
