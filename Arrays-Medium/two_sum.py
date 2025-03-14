#Input Format: N = 5, arr[] = {2,6,5,8,11}, target = 14
# Result: YES (for 1st variant)
#        [1, 3] (for 2nd variant)
# Explanation: arr[1] + arr[3] = 14. So, the answer is “YES” for the first variant and [1, 3] for 2nd variant.

#Hash Map
def two_sum(arr,target):
    d = {}
    for i in range(len(arr)):
        res=target-arr[i]
        if res not in d:
            d[arr[i]]=i
        else:
            return [d[res],i]
    

sol = two_sum([2,6,5,8,11],14)
print(sol)


            

#Two pointer approach
def two_sum(arr,target):
    arr.sort()
    i = 0
    j = len(arr)-1
    while i<j:
        if arr[i]+arr[j]==target:
            return [arr[i],arr[j]]
        elif arr[i]+arr[j]<target:
            i+=1
        else:
            j=j-1

print(two_sum([2,3,1,4],4))