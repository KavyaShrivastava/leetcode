# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers
# such that they add up to a specific target number. 
# Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.                                     

from typing import List
class TwoSumII:
    def twoSumII(self, numbers:List[int], target:int) -> List[int]:
        #Case 1:
        #start the loop from both ends, and update the start and end based on if the sum is larger or smaller than the target
        #since the array is already sorted 
        start = 0
        end = len(numbers)-1
        while start<end:
            if numbers[start] + numbers[end] == target:
                return [start+1, end+1]
            elif numbers[start] + numbers[end] > target:
                end-=1
            else:
                start+=1
        return []
            
            
    #Time compexity: O(n)
    #Space complexity: O(1)
        
        