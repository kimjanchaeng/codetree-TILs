R, C= list(map(int,input().split()))

mat=[list(map(str,input().split())) for i in range(C)]
# print(mat)

sta=mat[0][0]
cnt=0
for i in range(1,R-1):
    for j in range(1,C-1):
        if mat[i][j]!=sta:
            for k in range(i+1,R-1):
                for l in range(j+1,C-1):
                    if mat[k][l]!=mat[i][j]:
                        cnt+=1
print(cnt)