'''
Binary Search:
1. Works on Sorted arrays
2. Uses Divide and Conquer approach to eliminate half elements of sorted array




Step-1: - Identify the middle element of the array int((start_index+end_index)/2)
Step-2: - Compare the middle element to the element to be searched.
Step-3: - If element_to_be_searched==middle element-> return;
          Else: element_to_be_searched < middle element-> upper_bound= mid-1 ;
          Split the array by chaning the upper bound
          Else: element_to_be_searched > middle element-> lower_bound= mid-1 ; 
          Split the array by chaning the lower bound
Step-3: - Repeat Step-1,2,3 again and again until only middle element, upper and lower bound are at the same index, 
          and compare the element to be searched, If not found-> return 


Binary Search Edge Cases
1. If element doesn't exist in the array: Then add stopping criteria, if upper - lower <0 ; return Not Found
2. In case of duplicates: it returns the first instance itself wherever it finds it 
'''




def binary_search(arr:list, element, debug=False):
    lower=0
    upper=len(arr)-1
    while lower <= upper:
        mid=int((lower+upper)/2)      # mid = (lower+upper)//2 Integer Division
        if debug:
            print("Lower, Upper Bounds and Middle are:", lower, upper, mid)
            print("Array Values for Lower, Upper Bounds and Middle are:", arr[lower], arr[upper], arr[mid])
        if element == arr[mid]:
            return "Element Found at index, "+str(mid), mid
        elif element > arr[mid]:
            lower = mid+1
        else:
            upper = mid - 1
    
    return "Element Not Found in the array", -1


arr=[12,34,45,56,56,56,56,67,89]
x1=56
x2=57
print(binary_search(arr, x1, False))
print(binary_search(arr, x2, False))