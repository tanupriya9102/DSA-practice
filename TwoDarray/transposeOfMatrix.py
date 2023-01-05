m=[[1,2,3],[4,5,6],[7,8,9]]
print(m)
for i in range(len(m)):
    for j in range(0,i):
        m[i][j],m[j][i]=m[j][i],m[i][j]
# for i in m:
#     i[:]=i[::-1]
print(m)
