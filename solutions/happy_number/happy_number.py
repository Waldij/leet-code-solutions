class Solution:
    def isHappy(self, n: int) -> bool:
        prev = []
        while n != 1:
            n = sum([int(c)**2 for c in str(n)])
            if n not in prev:
                prev.append(n)
            else:
                print(prev)
                return False
        return True

    def isHappy_fast(self, n: int) -> bool:
        cycle_members = (4, 16, 37, 58, 89, 145, 42, 20)

        def get_next(number: int) -> int:
            return sum([int(c) ** 2 for c in str(number)])

        while n != 1 and n not in cycle_members:
            n = get_next(n)
        return n == 1


def main():
    solution = Solution()
    assert solution.isHappy_fast(19) is True
    assert solution.isHappy_fast(2) is False


if __name__ == '__main__':
    main()
