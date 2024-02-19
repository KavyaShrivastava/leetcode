# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.
class ValidAnagram:
    def isAnagram(self, s:str, t:str) -> bool:
        #Case 1:
        #Sort it and match them by looping through them
        # s = list(s)
        # s.sort()
        # t = list(t)
        # t.sort()
        # return s == t
        #O(T) = O(nlogn+mlogm)
        #O(s) = O(n + m)

        #Case 2:
        #take a dictionary and store the letters and their count as their value and subtract it everytime it occurs in th e second word. if it gets to 0, then you return False
        if len(s)!=len(t): return False
        
        letters_of_s_ocurence_dict = {}
        #initialise a dictionary
        for char in s:
            if char in letters_of_s_ocurence_dict:
                letters_of_s_ocurence_dict[char] +=1 
                #loop through for each letter and check if it already exists if so, add one
            else:
                letters_of_s_ocurence_dict[char] = 1
                #if it doesn't exist, add it to the dictionary
        #loop through t 
        for char in t:
            #if the letter exists in s, then check the count of the letter
            if char in letters_of_s_ocurence_dict:
                #subtract the amount of times this letter has occured by 1
                letters_of_s_ocurence_dict[char]-=1
                if letters_of_s_ocurence_dict[char] == 0:
                    del letters_of_s_ocurence_dict[char]
            else:
                #return false if the letter exists in t but not in s
                return False
        
        return len(letters_of_s_ocurence_dict) == 0
#Another way for Case 3 is:
#from collections import Counter
# def are_anagrams(s, t):
#     return Counter(s) == Counter(t)

    
#Edge Cases: 
# The lengths are different. 
# S has extra letters that don't exist in t 
# t has letters that dont exist in s 

                
        