class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        result_list =[]
        for element in candies:
            result_list.append(element + extraCandies >= max(candies))
        return result_list