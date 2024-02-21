from typing import List
class TwoSums:
    def twoSums(self, nums:List[int], target:int)->List[int]:
        #Case 1:
        #num a will be the index that loops through the list, looking for numb which is target-num a, if we don't find it, we update num a 
        
        #Case 2:
        #declare a dictionary {'1': index}
        #we look at each index's data and store the data as key and the index as value
        #we loop through the array and look for the key for target-index[data] its at right now. if it exists we return true
        #otherwise we look at the next value 
        #My written code
        # nums_dict = {index: element for index, element in enumerate(nums)}
        # print(nums_dict)
        # for element_a in nums:
        #     element_b = target-element_a
        #     if element_b in nums_dict.values():
        #         return  [nums.index(element_a), nums.index(element_b)]#index of element a and element b
        # return []
    
    #Correct Solution
        nums_dict = {element:index for index,element in enumerate(nums)} #creates a dictionary where enumerate returns a tuple of index, element
        for index_a, element_a in enumerate(nums): # for the index and the element 
            element_b = target - element_a
            if element_b in nums_dict and index_a != nums_dict[element_b]:
                return [index_a, nums_dict[element_b]]
            
    #O(t): 2O(n)
    #O(s): O(n)
            
        
        