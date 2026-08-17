
##Note:- In the below code we have implemented a condition arr[mid]>=x because it narrows down to left half eventually we will endup at calculating first occurence.

def first_occurence(arr,n,x):
    low = 0
    high = n-1
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid]>=x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

res = first_occurence([3,4,13,13,13,20,40],7,13)
print(res)


def last_occurence(arr,n,x):
    low = 0
    high = n-1
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid]<=x:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans

res1 = last_occurence([3,4,13,13,13,20,40],7,13)
print(res1)



##combined approach
def occurences(arr,target):
    def binary_search(Isfirst):
        low = 0
        high = len(arr)-1
        result = 0
        while low<=high:
            mid = (low+high)//2
            
            if arr[mid]==target:
                result=mid
                if Isfirst:
                    high=mid-1
                else:
                    low=mid+1
            
            elif arr[mid]>target:
                high=mid-1
            
            else:
                low=mid+1
        
        return result
    
    first = binary_search(True)
    last  = binary_search(False)
   
    return [first,last]

nums = [5, 7, 7, 8, 8, 10]
target = 8
print(occurences(nums, target)) 