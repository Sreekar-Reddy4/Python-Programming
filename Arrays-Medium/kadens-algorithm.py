# Input:
#  arr = [-2,1,-3,4,-1,2,1,-5,4] 

# Output:
#  6 

arr = [-2,1,-3,4,-1,2,1,-5,4]
max_sum=0
sum=0
for i in range(len(arr)):
    sum+=arr[i]

    if sum>max_sum:
        max_sum=sum
    if sum<0:
        sum=0
print(max_sum)
