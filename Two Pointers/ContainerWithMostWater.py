# You are given an integer array height of length n. There are n vertical lines drawn 
# such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

from typing import List
class ContainerWithMostWater:
    def containerWithMostWater(self, height:List[int])->int:
        #Case 1
        #calculate area of the rectangle formed by the furthest away lines i.e. with longest width: i at the position 0, height-1
        
        #The correct way to check is which of the two start or end is lower, and increment the one that is shorter
        #why you should not increment based on neighboring elements because you can miss out on combinations where start+1 might be greater than start, 
        # but the area will be lower becuase you have not checked if height[start]>height[end] and vice versa 
             
        start = 0
        end = len(height)-1
        maxArea1 = 0
        while start<end:
            length = end - start
            currArea = length  * min(height[start], height[end])
            maxArea1 = max(currArea, maxArea1)
            if height[start] <  height[end]:
                start+=1
            else:
                end-=1
                
            
        return maxArea1
    
def main():
    container = ContainerWithMostWater()
    result = container.containerWithMostWater([1,3,2,5,25,24,5])
    print(result)
    
if __name__ == "__main__":
    main()
            