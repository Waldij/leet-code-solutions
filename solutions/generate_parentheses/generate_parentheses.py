from typing import List


class Solution(object):
    def generateParenthesis(self, N):
        if N == 0: return ['']
        ans = []
        for c in range(N):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(N-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans


def main():
    solution = Solution()
    n = 5
    print(solution.generateParenthesis(n))


if __name__ == '__main__':
    main()
