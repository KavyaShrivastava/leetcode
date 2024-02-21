from typing import List
from collections import defaultdict
class GroupAnagrams:
    def groupAnagrams(self, strs:List[str])-> List[List[str]]:
        #Case 1:
        anagram_match = defaultdict(list) #the key is a list which is 26 length and each index represents the letter in the alphabet 
        #the value is a list of words from str that match the key 
        #every word gets an automatic pattern 
        # for word in strs:
        #     alphabet_count = [0] * 26
        #     for letter in word:
        #         index_of_letter_in_alphabet_count = ord(letter) - ord('a')
        #         alphabet_count[index_of_letter_in_alphabet_count] +=1
        #     alphabet_count = tuple(alphabet_count)
        #     anagram_match[alphabet_count].append(word)
            
        # return list(anagram_match.values)
    #Optimized version of this:
        # for word in strs:
        #     # Directly compute the tuple of letter counts to use as a key
        #     alphabet_count = tuple(word.count(chr(i + ord('a'))) for i in range(26))
        #     anagram_match[alphabet_count].append(word)
            
        # return list(anagram_match.values())
        
        
        #Case 2: 
        groups = defaultdict(list)

        for word in strs:
            sorted_word = tuple(sorted(word))
            print(sorted_word)
            groups[sorted_word].append(word)
        
        return list(groups.values())

    
                
        
        
        