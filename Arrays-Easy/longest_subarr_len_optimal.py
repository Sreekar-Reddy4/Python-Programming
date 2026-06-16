#Prefix Sum

nums = [10, 5, 2, 7, 1, 9]
k = 15  
def len_sub_arr(arr,N,k):
    prefix_sum=0
    d = {0:-1}
    max_length = 0
    for i in range(N):
        prefix_sum+=arr[i]

        remaining = prefix_sum - k

        if remaining in d:
            max_length = max(max_length,i-d[remaining])

        d[prefix_sum]=i

    return max_length
