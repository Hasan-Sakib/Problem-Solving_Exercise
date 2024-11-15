class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        max_num = max(candies)
        result = []
        for i in candies:
            if i + extraCandies >= max_num:
                result.append(True)
            else:
                result.append(False)
        return result


candies_input = input("Candies: ")

candies = list(map(int, candies_input.split()))
extraCandies = int(input("Extra candies: "))

solution = Solution()
result = solution.kidsWithCandies(candies, extraCandies)
print(result)
