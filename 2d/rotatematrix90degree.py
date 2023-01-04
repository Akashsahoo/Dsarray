import numpy as np
li = [[1,2,3],[4,5,6],[7,8,9]]
mat = np.array(li)
print(mat)
# print(" "*10)
# l,r = 0,len(mat)-1
# while l<r:
#     top = l
#     bottom = r
#     for i in range(r-l):
#         topleft = mat[top][l+i]
#         mat[top][l+i] = mat[bottom-i][l]
#         mat[bottom-i][l] = mat[bottom][r-i]
#         mat[bottom][r-i] = mat[top + i][r]
#         mat[top + i][r] = topleft
#     l = l+1
#     r = r-1    
#print(mat)
l,r = 0 , len(mat)-1
while l<r:
    top = l
    bottom = r
    for i in range(r-l):
        topleft = mat[top][l+i]
        mat[top][l+i] = mat[bottom-i][l]
        mat[bottom-i][l] = mat[bottom][r-i]
        mat[bottom][r-i] =mat[top+i][r]
        mat[top+i][r] = topleft
    l = l+1
    r = r-1

print(mat)

 