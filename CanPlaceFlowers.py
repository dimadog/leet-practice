class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        n_defacto = 0
        for i in range(len(flowerbed)):
            print(f'iteration {i}')

            

            if flowerbed[i] == 0 and flowerbed[i+1] == 0 and flowerbed[i+2] == 0:
                print(f'index condition 2 {i}')
                flowerbed[i+1] = 1
                n_defacto += 1

            if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                print(f'index condition 3 {i}')
                flowerbed[i] = 1
                n_defacto += 1

            if flowerbed[i-1] ==0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                print(f'index condition 1 {i}')
                flowerbed[i] = 1
                n_defacto += 1

            

        print(f'{flowerbed} res {n_defacto}')
        return n == n_defacto 

if __name__ == '__main__':
    solution = Solution()
    print('passed' if solution.canPlaceFlowers([1,0,0,0,1], 1) == True else 'failed')
    print()
    print('passed' if solution.canPlaceFlowers([1,0,0,0,1], 2) == False else 'failed')
    print()
    print('passed' if solution.canPlaceFlowers([0,0,1,0,1], 1) == True else 'failed')
    print()
    print('passed' if solution.canPlaceFlowers([1,0,0,0,0,0,1], 2) == True else 'failed')
    print()
    print('passed' if solution.canPlaceFlowers([1,0,0,0,0,1], 2) == False else 'failed')
