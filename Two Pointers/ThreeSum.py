from typing import List
class ThreeSum:
    def threeSum(self, nums:List[int])->List[List[int]]:
        nums.sort() #sorting the value
        res = []
        for i in range(len(nums)-2):
            start = i + 1
            end = len(nums) -1
            while start < end:
                if nums[start] + nums[end] + nums[i] == 0:
                    res.append([nums[start], nums[end], nums[i]])
                    while start < end and nums[start] == nums[start + 1]:  # Skip duplicates for start
                        start += 1
                    while start < end and nums[end] == nums[end - 1]:  # Skip duplicates for end
                        end -= 1
                    start+=1
                    end-=1
                elif nums[start] + nums[end] + nums[i] > 0:
                    end-=1
                else:
                    start+=1
        return res
    
def main():
    nums = [-1, 0, 1, 2, -1, -4]
    three_sum = ThreeSum()
    result = three_sum.threeSum(nums)
    print(result)

if __name__=="__main__":
    main()
        
    