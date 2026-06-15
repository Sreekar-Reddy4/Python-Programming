# Input:
#  arr = [-2,1,-3,4,-1,2,1,-5,4] 

# Output:
#  6 

#Variant 1 - Return maximum sum of subarray
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


#Variant2 -- Return sub array with maximum sum
arr = [-2,1,-3,4,-1,2,1,-5,4]
max_sum=0
start=0
temp_start=0
end=0
sum=0
for i in range(len(arr)):
    sum+=arr[i]
    if sum>max_sum:
        max_sum=sum
        start=temp_start
        end=i
    if sum<0:
        sum=0
        temp_start=i+1
print(max_sum)


