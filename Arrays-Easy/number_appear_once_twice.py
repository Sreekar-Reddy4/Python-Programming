#Time Complexity: O(n2)
#Space Complexity: O(n)


def get_num(arr):
    d={}
    for i in arr:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for i in d:
        if d[i]==1:
            return i

arr = [2,2,1]
res = get_num(arr)
print(res)