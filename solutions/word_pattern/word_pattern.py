class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(sep=' ')
        if len(words) != len(pattern):
            return False

        hashtable = {}
        for i in range(len(pattern)):
            if not pattern[i] in hashtable:
                if words[i] in hashtable.values():
                    return False
                hashtable[pattern[i]] = words[i]
            else:
                if hashtable[pattern[i]] != words[i]:
                    return False
        return True


def main():
    solution = Solution()

    pattern = "abba"
    s = "dog cat cat dog"
    assert solution.wordPattern(pattern, s) is True

    pattern = "abba"
    s = "dog cat cat fish"
    assert solution.wordPattern(pattern, s) is False

    pattern = "aaaa"
    s = "dog cat cat dog"
    assert solution.wordPattern(pattern, s) is False

    pattern = "abba"
    s = "dog dog dog dog"
    assert solution.wordPattern(pattern, s) is False


if __name__ == '__main__':
    main()
