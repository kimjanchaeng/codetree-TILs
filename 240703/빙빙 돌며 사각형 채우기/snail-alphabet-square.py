import string
n, m = list(map(int,input().split()))

dx,dy=[0,1,0,-1],[1,0,-1,0]
dir=0

mat=[[0]*m for i in range(n)]
upper = [i for i in string.ascii_uppercase]
# print(upper)

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<m


x,y=0,0
mat[x][y]='A'
for i in range(1,n*m):
    nx,ny=x+dx[dir],y+dy[dir]

    if in_range(nx,ny) and mat[nx][ny]==0:
        if i>len(upper)-1:
            i%=len(upper)
    else:
        dir=(dir+1)%4
    
    x,y=x+dx[dir],y+dy[dir]
    mat[x][y]=upper[i]
# print(mat)

for i in mat:
    for j in i:
        print(j,end=' ')
    print()