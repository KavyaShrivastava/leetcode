class LongestSubstringWithoutRepeatingCharacters:
    def longestSubstringWithoutRepeatingCharacter(self, s:str) -> int:
        #My code
        # if len(s) == 0:
        #     return 0
        # left = 0
        # right = 1 
        # curr_length = 1
        # max_length = 1
        # window = s[left]
        # while right < len(s):
        #     if s[right] in window: 
        #         curr_length = 1 #This is wrong because the value at s[right] doesn't mean the current_length will become 1 but it can  just reduce. 
        #         while window[left] != window[right]: #this is correct but it doesn't actually update the window which is remove the letters before right
        #             left+=1
        #     else:
        #         window += s[right]  #This doesn't update the window when the chcaracter are skipped because they are repeating
        #         curr_length+=1
        #         max_length = max(curr_length, max_length)
        #     right+=1
        # return max_length
        
        #Correct Code 
        charIndexMap = {} #This hashmap contains the s[right ] as thekey and the last index they occurred at as the value 
        left = 0
        maxLength = 0
        for right in range(len(s)):
            if s[right] in charIndexMap:
            # If the character is in the dictionary, move the left pointer
            # max is used here to avoid moving left pointer backward
                left = max[left, charIndexMap[right]+1]
                # Update the last index of the character i.e. the value of the key
                charIndexMap[s[right]] = right
            #calculate the length of the new left and right length
            maxLength = max(maxLength, right-left+1)
        return maxLength
                
                
    
    
