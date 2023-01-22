from typing import List
from itertools import combinations


class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if len(s) == 0: return [[]]

        def loops(res, tmp, s):
            if len(s) == 0:
                res.append(list(tmp))
                return

            for i in range(1, len(s) + 1):
                if s[:i] == s[:i][::-1]:
                    loops(res, tmp + [s[:i]], s[i:])

        res = []
        loops(res, [], s)

        return res


def main():
    solution = Solution()
    s = 'aab'
    res = solution.partition(s)
    print(res)


if __name__ == '__main__':
    main()
