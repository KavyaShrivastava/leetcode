from typing import List
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the
# elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

class ProductOfArrayExceptSelf:
    def productOfArrayExceptSelf(self, nums:List[int])->List[int]:
        #have a left product and a right product 
        #have an array of left products 
        # have an array of right products starting from end 
        #multiply both and return the result
        # length = len(array)
        # left_product = list(length)
        # left_product[0] = 1
        # right_product = list(length)
        # right_product[length-1] = 1
        # result = []
        # for i in range(1,length):
        #     left_product[i] = left_product[i-1] * array[i-1]
        #     right_product[length-i-1] = right_product[i+1] * array[length-i+1]
        
        # for i in range(length):
        #     result = left_product[i] * right_product[i]
        
        # return result
        
        
        #Correct Code: 
        #def productExceptSelf(self, nums: List[int]) -> List[int]:
        #have a left product and a right product 
        #have an array of left products 
        # have an array of right products starting from end 
        #multiply both and return the result
        length = len(nums)
        left_product = [1] * length
        left_product[0] = 1
        right_product = [1] * length
        right_product[length-1] = 1
        result = []
        for i in range(1,length):
            left_product[i] = left_product[i-1] * nums[i-1]
        
        for i in range(length-2, -1, -1):
            right_product[i] = right_product[i+1] * nums[i+1]

        for i in range(length):
            result.append(left_product[i] * right_product[i])
        
        return result
    
    #OPTIMISED SOLUTION
             
    # class Solution:
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     answer = [1] * len(nums)
    #     prefix = 1
    #     for i in range(len(nums)):
    #         answer[i] = prefix
    #         prefix = prefix * nums[i]
    #     postfix = 1
    #     for i in range(len(nums) - 1, -1, -1): # iterate in reverse order
    #         answer[i] = answer[i] * postfix # dont replace the old prefix value
    #         postfix = postfix * nums[i]
    #     return answer
            
        
        
        
        