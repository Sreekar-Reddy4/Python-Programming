#Example 1:

# Input:
# arr[] = {1,2,-4,-5}, N = 4
# Output:
# 1 -4 2 -5

# Explanation: 

# Positive elements = 1,2
# Negative elements = -4,-5
# To maintain relative ordering, 1 must occur before 2, and -4 must occur before -5.

#Brute force
# def re_arrange_elements(arr):
#     pos=[]
#     neg=[]

#     for i in range(len(arr)):
#         if arr[i]>0:
#             pos.append(arr[i])
#         else:
#             neg.append(arr[i])
    
#     for i in range(len(pos)):
#         arr[2*i] = pos[i]
#         arr[2*i+1]= neg[i]
    
#     return arr

# A = [1, 2, -4, -5]
# ans = re_arrange_elements(A)
# print(ans)

#optimal approach
def rearr_optimal(arr):
    n = len(arr)
    pos_index = 0
    neg_index = 1
    ans = [0]*n
    for i in range(len(arr)):
        if arr[i]>0:
            ans[pos_index]=arr[i]
            pos_index+=2
        else:
            ans[neg_index]=arr[i]
            neg_index+=2
    return ans

arr=[1, 2, -4, -5]
sol = rearr_optimal(arr)
print(sol)
            


