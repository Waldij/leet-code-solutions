class Solution:
    def romanToInt(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")\
            .replace("XL", "XXXX").replace("XC", "LXXXX")\
            .replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number

    def romanToInt1(self, s: str) -> int:
        roman_to_int = {
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
        value = 0
        while s:
            for letters, int_value in roman_to_int.items():
                if s.startswith(letters):
                    value += int_value
                    s = s[len(letters):]
        return value


def main():
    solution = Solution()
    s = 'MCMXCIV'
    print(s, solution.romanToInt(s))


if __name__ == '__main__':
    main()
