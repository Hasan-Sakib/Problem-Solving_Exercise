from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        planted = 0

        for i in range(len(flowerbed)):
            leftEmpty = (i == 0) or (flowerbed[i - 1] == 0)
            rightEmpty = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)

            if flowerbed[i] == 0 and leftEmpty and rightEmpty:
                flowerbed[i] = 1
                planted += 1

                if planted == n:
                    return True
        return False


if __name__ == "__main__":
    flowerbed = list(map(int, input("flowerbed= ").split()))
    n = int(input("n= "))

    solution = Solution()
    result = solution.canPlaceFlowers(flowerbed, n)
    print(result)
