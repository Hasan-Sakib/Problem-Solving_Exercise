from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if (str1 + str2) == (str2 + str1):
            lcs = gcd(len(str1), len(str2))
            return str1[0:lcs]
        return ""


str1 = input()
str2 = input()

solution = Solution()
result = solution.gcdOfStrings(str1, str2)
print(result)
