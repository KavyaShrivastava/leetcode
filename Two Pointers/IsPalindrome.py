import re

class IsPalindrome:
    def isPalindrome(self, strs:str)->bool:
        
        # #Case 1
        # #convert all to lowercase letters
        # strs = strs.lower()

        # #space all non alpha numeric characters including spaces with "" which is essentialy nothing
        # strs = re.sub(r'[a-z0-9]', "", strs)
        
        # #loop through the string both from the start and end and compare it till you reach the middle 
        # length = len(strs)
        # for i in range(length//2):
        #     if strs[i] != strs[length-i-1]:
        #         return False
        
        # return True 
        
        
        #Case 2
        #you convert the string into a list 
        s = [c.lower() for c in s if c.isalnum()]
        return s == s[::-1]

        #You reverse a string 
        #One way to do it is through slicing 
        
        
        