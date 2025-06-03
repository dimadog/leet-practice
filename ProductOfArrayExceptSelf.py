import math,operator,functools

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        awnser = [1] * len(nums)
        for i in range(len(nums)):
            awnser[i] = math.prod(nums[:i])*math.prod(nums[i+1:])
        return awnser
    
    def productExceptSelf1(self, nums: list[int]) -> list[int]:
        awnser = [1] * len(nums)
        left, right = 1, 1
        for i in range(len(nums)):
            awnser[i] *= left
            left *= nums[i]
            awnser[-1-i] *= right
            right *= nums[-1-i]
        return awnser
    
    def productExceptSelf2(self, nums: list[int]) -> list[int]:
        awnser = [1] * len(nums)
        for i in range(len(nums)):
            awnser[i] = functools.reduce(operator.mul, nums[:i], 1)*functools.reduce(operator.mul, nums[i+1:], 1)
    
    def productExceptSelf3(self, nums: list[int]) -> list[int]:
        awnser = [1] * len(nums)
        for i in range(len(nums)):
            n , m = 1 , 1
            for x in nums[:i]:
                n *= x
            for x in nums[i+1:]:
                m *= x
            awnser[i] = n * m
        return awnser
