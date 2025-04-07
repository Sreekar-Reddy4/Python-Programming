def count_sub_arr(arr,N,k):
    i=0
    start=0
    sum=0
    count=0
    while i<=N-1:
        sum+=arr[i]
        if sum!=k and i==N-1:
            sum=0
            i=start+1
            start+=1
        elif sum==k:
            count+=1
            i+=1
        else:
            i+=1
    return count


print(count_sub_arr([1,2,3],3,3))
