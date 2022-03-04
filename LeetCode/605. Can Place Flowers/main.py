from typing import List

#flowerbed = [1,0,0,0,1]
#n = 2

flowerbeds = [
    #[1,0,0,0,1],
    # [0,0,1,0,1],
     #[0,0,1,0,0],
     #[1,0,1,0,1,0,1],
     [0]
]

ns = [
    #1,
    #2,
    1
]

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return True

        counter = 0
        
        for i in range(len(flowerbed)):
            if self.isNeighborEmpty(i, flowerbed):
                counter += 1
                if counter == n:
                    return True
                flowerbed[i] = 1
        return False
    
    def isNeighborEmpty(self, i: int, flowerbed: List[int]) -> bool:
        if i == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
            return True

        if i == len(flowerbed) - 1 and flowerbed[i] == 0 and flowerbed[i-1] == 0:
            return True

        if i > 0 and i < len(flowerbed) - 1 and flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
            return True

        return False


for i in range(len(flowerbeds)):
    flowerbed = flowerbeds[i]
    n = ns[i]
    print('flowerbed: ', flowerbed, ', n: ', n)
    print(Solution().canPlaceFlowers(flowerbed, n))