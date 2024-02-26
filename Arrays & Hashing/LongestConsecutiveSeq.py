from typing import List
class LongestConsecutiveSequnce:
    def longestconsecutiveSequence(self, nums:List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = sorted(nums)
        print(nums)
        longest_sequence = 1
        curr_sequence = 1 
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 1:
                curr_sequence +=1
            elif nums[i+1] == nums[i]:
                continue
            else:
                curr_sequence = 1
            longest_sequence = max(curr_sequence, longest_sequence)
        return longest_sequence

        