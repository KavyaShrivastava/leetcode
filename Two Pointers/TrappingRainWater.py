from typing import List
class TrappingRainWater:
    def trappingRainWater(self, height:List[int])->int:
        # start = 0 
        # end = len(height)-1
        # currArea = 0
        # currUnit = 0
        # currWidth = 0
        
        # while(start<end):
        #     if start==0 and height[start] < height[start+1]:
        #         start+=1
        #     else:
        #         break
        # currWidth = start
        # while start<end:
        #     if height[start] > height[currWidth]:
        #         currUnit += height[start] - height[start+1]
        #         start+=1
        #     else:
        #         currArea += currUnit * min(height[start]-height[currWidth])

        # #your start is at a new max height 
        # return currArea
        
        ##Case 1:
        # left_max = [0] * len(height)
        # right_max = [0] * len(height)
        # area = 0
        # for i in range(1,len(height)):
        #     left_max[i] = max(left_max[i-1], height[i-1])
        
        # for i in range(len(height)-1, -1):
        #     right_max[i] = max(right_max[i+1], height[i+1])
        
        # for i in range(len(height)):
        #     water_at_curr_index = (min(left_max[i], right_max[i]) - height[i]) 
        #     area += water_at_curr_index if water_at_curr_index > 0 else 0
            
        #Time Complexity: O(n)
        #Space complexity 2O(n)
        
        #Case 2 
        left = 0
        right = len(height)-1
        left_max = height[left]
        right_max = height[right]
        area = 0
        while left < right:
            if left_max < right_max: #updating the pointers based on which one is smaller because it doesn't matter which one is bigger/biggest because it would only trap water relative to the minimum one 
                left+=1
                left_max = max(left_max, height[left]) 
            else:
                right-=1
                right_max = max(right_max, height[right])
            area += min(left_max, right_max) - height[i] if min(left_max, right_max) - height[i] > 0 else 0
        return area
            
                
            
        
            
        
        
    
def main():
    rainWater = TrappingRainWater()
    res = rainWater.trappingRainWater([4,2,0,3,2,5])
    print(res)
    
if __name__ == "__main__":
    main()
            
        
                
            
                
                
            
                
        
        
                

        