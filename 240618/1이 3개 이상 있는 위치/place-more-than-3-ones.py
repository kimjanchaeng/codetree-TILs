n=int(input())
mat=[]
for i in range(n):
    di=list(map(int,input().split()))
    mat.append(di)
# print(mat)

def in_range(x,y):
    return x>=0 and x<n and y>=0 and y<n

fin=0
dx,dy=[1,0,-1,0],[0,-1,0,1]
for i in range(n):
    for j in range(n):
        cnt=0
        for k in range(4):
            x,y=i+dx[k],j+dy[k]
            if in_range(x,y) and mat[x][y]==1:
                cnt+=1 
        if cnt>=3:
            fin+=1
print(fin)