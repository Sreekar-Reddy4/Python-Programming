#Time complexity - O(n)
#Space complexity - O(1)


def second_smallest(arr,n):
    if (n<2):
        return -1
    else:
        small = float('inf')
        sec_small = float('inf')
        for i in range(n):
            if arr[i]<small:
                sec_small  = small
                small = arr[i]
            elif arr[i]<sec_small and arr[i]!=small:
                sec_small = arr[i]
        return sec_small

def second_largest(arr,n):
    if (n<2):
        return -1
    else:
        large = float('-inf')
        sec_large = float('-inf')
        for i in range(n):
            if arr[i]>large:
                sec_large=large
                large=arr[i]
            elif arr[i]>sec_large and arr[i]!=large:
                sec_large = arr[i]
        return sec_large


if __name__ == '__main__':
    arr=[1,5,2,3,4,6,6]
    n=len(arr)
    res1=second_smallest(arr,n)
    res2=second_largest(arr,n)
    print(res1)
    print(res2)
    