#217. Contains Duplicate 
##Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
from typing import List

class ContainsDuplicate:
    def containsDuplicate(self, nums:List[int]) -> bool:
        #Case 1: You can sort the list and check for neighboring elements. if there's a duplicate, you can return True
            #O(T): O(n logn) and O(S) = O(1)
        #Case 2: You can create a dictionary or a data strcutre which can only have one value, which is a set and if the value already exists,then return True. 
            #O(T): O(n) where n = looping through the list and adding it to the ds. O(s): O(n)
        
        #Case 1: 
        # nums = nums.sort()
        # for i in range(len(nums)-1):
        #     if nums[i] == nums[i+1]:
        #         return True
        # else:
        #     return False
            
        #Case 2:
        no_duplicate_set = set()
        for i in range(len(nums)):
            if nums[i] in no_duplicate_set:
                return True
            else:
                no_duplicate_set.add(nums[i])
        return False
    
    #Case 3 
        #return len(nums) != len(set(nums))
    
        
        
        