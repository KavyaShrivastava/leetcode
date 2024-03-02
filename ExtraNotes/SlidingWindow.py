# The use of the Sliding Window technique can be done in a very specific scenario, 
# where the size of the window for computation is fixed throughout the complete nested loop. Only then the time complexity can be reduced

#The general use of the Sliding window technique can be demonstrated as follows:

# Find the size of the window required 
# Compute the result for 1st window, i.e. from the start of the data structure
# Then use a loop to slide the window by 1, and keep computing the result window by window.

#Array, String, Sub Array, Sub String, Largest Sum, Maximum Sum, Minimum Sum

#Example: Given an array of integers of size ‘n’, Our aim is to calculate the maximum sum of ‘k’ consecutive elements in the array.

# Applying the sliding window technique : 

# We compute the sum of the first k elements out of n terms using a linear loop and store the sum in variable window_sum.
# Then we will graze linearly over the array till it reaches the end and simultaneously keep track of the maximum sum.
# To get the current sum of a block of k elements just subtract the first element from the previous block and add the last element of the current block.

from typing import List
import sys

class SlidingWindow:
    INT_MIN = -sys.maxsize - 1
    
    def maxSum(array:List[int], k:int) -> int:
        n = len(array)
        if n<k:
            return None
        
        window_sum = sum(array[:k]) #calculate the first window's sum
        maxSum = window_sum # calculate the maxSum at this point
        for i in range(n-k): #the loop only goes through until n-k-1 because it'll reach i = n-k-1+k = n-1 which means the last inde when it calculates window
            window_sum = window_sum - array[i] + array[i+k] #calculate the value of window_sum by adding the value of the next index outside the window where the window starts at i
            maxSum = max(window_sum, maxSum)
        
        return maxSum
        