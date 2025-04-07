# Example 1:
# Input Format
# : N = 5, array[] = {1,2,2,3,2}
# Result
# : 2
# Explanation:
#  Here we can see that the Count(1) = 1, Count(2) = 3 and Count(3) = 1.Therefore, the count of 2 is greater than N/3 times. Hence, 2 is the answer.

def majority_ele(arr,N):
    d={}
    for i in range(N):
        if arr[i] not in d:
            d[arr[i]]=1
        else:
            d[arr[i]]+=1

    for i in d:
        if d[i]>N/3:
            return i

print(majority_ele([1,2,2,3,2],5))
