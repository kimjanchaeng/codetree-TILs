N, M=list(map(int,input().split()))

mat=[[0]*N for i in range(N)]

dx,dy=[0,1,0,-1],[1,0,-1,0]

def in_range(x,y):
    return 0<=x and x<N and 0<=y and y<N

for i in range(M):
    x,y=list(map(int,input().split()))
    x=x-1
    y=y-1
    mat[x][y]=1
    cnt=0
    for j in range(4):
        nx,ny=x+dx[j],y+dy[j]
        if in_range(nx,ny) and mat[nx][ny]==1:
            cnt+=1
    if cnt==3:
        print(1)
    else:
        print(0)