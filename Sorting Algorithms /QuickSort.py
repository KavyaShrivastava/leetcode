from typing import List
class QuickSort:
    @staticmethod
    def partition(array, low, high):
        pivot = array[high]
        store_index = low
        for i in range(low, high):
            if array[i] < pivot:
                array[i], array[store_index] = array[store_index], array[i]
                store_index+=1
        array[store_index], array[high] = array[high], array[store_index]
        return store_index
    
    @staticmethod
    def quickSort(array:List[int], low:int, high:int):
        if low < high:
            pi = QuickSort.partition(array, low, high)
            QuickSort.quickSort(array, low, pi - 1)
            QuickSort.quickSort(array, pi + 1, high)
            
            
            #Average Case = O(n)
            #Worst Case (On^2)

            
            
        