from typing import List
from collections import Counter

class TopKFrequentElements:
    def topKFrequentElements(self, nums:List[int], k:int) -> List[int]:
        # count = Counter(nums)
        # unique = list(count.keys())

        # def partition(left, right, pivot_index) -> int:
        #     pivot_frequency = count[unique[pivot_index]]
        #     unique[pivot_index], unique[right] = unique[right], unique[pivot_index]
        #     store_index = left 
        #     for i in range(left, right):
        #         if count[unique[i]] < pivot_frequency:
        #             unique[store_index], unique[i] = unique[i], unique[store_index]
        #             store_index+=1
            
        #     unique[right], unique[store_index] = unique[store_index], unique[right]
        #     return store_index

        # def quickSelect(left, right, k_smallest) -> None:
        #     pivot_index = random.randint(left, right)
        #     pivot_index = partition(left, right, pivot_index)

        #     if left == right:
        #         return

        #     if pivot_index < k_smallest:
        #         quickSelect(pivot_index+1, right, k_smallest)
        #     elif pivot_index > k_smallest:
        #         quickSelect(left, pivot_index-1, k_smallest)
        #     else:
        #         return
        
        # n = len(unique)
        # quickSelect(0, n-1, n-k)
        # return unique[n-k:]
        k_elements = []
        #Case 1:
        #count the number of times an element occurs and add the count to a data structure. Then sort the list and return the the first k elements
        elements = Counter(nums) #O(n)
        print(elements)
        #MY CODE
        # for element in elements.keys() and k>0:
        #     k_elements.append(element)
        #     k-=1
        # return k_elements
        
        #Correct Code:
        k_elements = [element for element,frequency in elements.most_common(k)]
        return k_elements

    
    #


        
        