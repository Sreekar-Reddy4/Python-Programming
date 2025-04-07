# Example 1:
# Input: Matrix[][] = { { 1, 2, 3, 4 },
# 		      { 5, 6, 7, 8 },
# 		      { 9, 10, 11, 12 },
# 	              { 13, 14, 15, 16 } }

# Outhput: 1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10.
# Explanation: The output of matrix in spiral form.


def spiral_matrix(mat):
    top=0
    bottom=len(mat[0])-1
    left=0
    right=len(mat)-1
    ans = []
    while top<=bottom and left<=right:
        for i in range(left,right+1):
            ans.append(mat[top][i])
        top+=1

        for i in range(top,bottom+1):
            ans.append(mat[i][right])
        right-=1

        if top<=bottom:
            for i in range(right,left-1,-1):
                ans.append(mat[bottom][i])
            bottom-=1

        if left<=right:
            for i in range(bottom,top-1,-1):
                 ans.append(mat[i][left])
            left+=1
    
    return ans

mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(spiral_matrix(mat))



