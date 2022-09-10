class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        slices = [''] * numRows
        index, step = 0, 1
        for char in s:
            slices[index] += char
            if index == 0:
                step = 1
            if index == numRows - 1:
                step = -1
            index += step
        return ''.join(slices)


def main():
    s = 'PAYPALISHIRING'
    solution = Solution()
    print(solution.convert(s, 3))


if __name__ == '__main__':
    main()
