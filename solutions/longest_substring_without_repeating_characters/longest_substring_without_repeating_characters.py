class Solution1:

    @staticmethod
    def lengthOfLongestSubstring(s: str) -> int:
        sub = ''
        res = ''
        for i in s:
            if i not in sub:
                sub += i
            else:
                if len(res) <= len(sub):
                    res = sub
                sub = sub.split(i)[-1] + i
        return max(len(res), len(sub))


class Solution:
    @staticmethod
    def lengthOfLongestSubstring(s: str) -> int:
        max_length = 0
        hashset = set()
        for i in range(len(s)):
            hashset.add(s[i])
            for j in range(i + 1, len(s)):
                if s[j] not in hashset:
                    hashset.add(s[j])
                else:
                    break

            max_length = len(hashset) if len(hashset) > max_length else max_length
            hashset.clear()
        return max_length



def main():
    # s = 'abcabcbb'
    # print(Solution.lengthOfLongestSubstring(s))
    #
    # s = 'aaabbbbb'
    # print(Solution.lengthOfLongestSubstring(s))
    #
    # s = 'pwwkew'
    # print(Solution.lengthOfLongestSubstring(s))

    s = 'dvdf'
    print(Solution1.lengthOfLongestSubstring(s))


if __name__ == '__main__':
    main()
