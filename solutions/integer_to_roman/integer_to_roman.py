class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1,
        }

        roman_string = ''
        for k, v in roman.items():
            number_of_values = num // v
            num -= number_of_values * v
            roman_string += k * number_of_values

        return roman_string


def main():
    solution = Solution()
    num = 1994
    print(num, solution.intToRoman(num))


if __name__ == '__main__':
    main()
