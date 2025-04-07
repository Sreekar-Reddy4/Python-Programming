# arr = [4, 7, 1, 0]
# Output
# :
#  7 1 0
# Explanation:

#  Rightmost element is always a leader. 7 and 1 are greater than the elements in their right side.

def leader_arr(arr):
    lst=[]
    n=len(arr)
    max_ele=arr[n-1]
    lst.append(max_ele)
    for i in range(len(arr)-1,-1,-1):
        if arr[i]>max_ele:
            lst.append(arr[i])
            max_ele=arr[i]
    return lst

result=leader_arr([4,7,1,0])
for i in result:
    print(i)