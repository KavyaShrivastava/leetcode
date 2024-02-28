from typing import List
class BinarySearch:
    def binarySearchIterative(self, array:List[int], value:int):
        
        #Case 1: iterative approach
        start = 0
        end = len(array)-1
        while start<=end:
            mid = start + (end-start)//2
            if array[mid] == value:
                return mid
            elif array[mid] > value:
                end = mid-1
            else:
                start = mid + 1
        return None

    def binarySearchRecursive(self, array: List[int], value: int, start: int = 0, end: int = None) -> int:
        if end is None:
            end = len(array) - 1

        if start > end:
            return None  # Indicates that the value is not found

        mid = start + (end - start) // 2

        if array[mid] == value:
            return mid
        elif array[mid] > value:
            return self.binarySearchRecursive(array, value, start, mid - 1)
        else:
            return self.binarySearchRecursive(array, value, mid + 1, end)
            
        