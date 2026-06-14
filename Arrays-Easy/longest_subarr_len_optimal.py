#Prefix Sum

nums = [10, 5, 2, 7, 1, 9]
k = 15  

def longest_sub_arry(arr,k):
    n=len(arr)
    prefix_sum=0
    d={}
    result=0
    for i in range(n):
        prefix_sum+=arr[i]
        
        remaining=prefix_sum-k
        
        if remaining in d:
            result = max(result,i-d[remaining])
        
        else:
            d[prefix_sum]=i
    
    return result

print(longest_sub_arry([-3, 2, 1],6))
