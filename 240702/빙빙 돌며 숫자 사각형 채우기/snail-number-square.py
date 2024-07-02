n,m=map(int,input().split())
# print(n)

mat=[[0]*m for i in range(n)]
# print(mat)

def in_range(x,y):
    return 0<=x and x<m and 0<=y and y<n

dx,dy=[0,1,0,-1],[1,0,-1,0]
dir=0
x,y=0,0
mat[0][0]=1

for i in range(2,n*m+1):
    nx,ny=x+dx[dir] ,y+dy[dir]

    if not in_range(nx,ny) or mat[nx][ny]!=0:
        dir=(dir+1)%4

    x,y=x+dx[dir],y+dy[dir]
    mat[x][y]=i

for i in mat:
    for j in i:
        print(j,end=' ')
    print('')