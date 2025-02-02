#TimeComplexity - O(n)
#SpaceComplexity - O(1)

def sorted_array(arr,n):
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            flag= True
        else:
            flag=False
    return flag

if __name__ == '__main__':
    arr=[1,2,3,4,5,6]
    n = len(arr)
    res=sorted_array(arr,n)
    print(res)

