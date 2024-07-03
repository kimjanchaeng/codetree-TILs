N, T = list(map(int,input().split()))
s=input()
mat=[list(map(int,input().split())) for i in range(N)]
# print(mat)

def in_range(x,y):
    return 0<=x and x<N and 0<=y and y<N

dx,dy=[0,1,0,-1],[1,0,-1,0]
x,y=N//2,N//2
ans=mat[x][y]
# print(ans)
dir=3

for i in s:
    # nx,ny=x+dx[dir],y+dy[dir]

    if i=='R':
        dir=(dir+1)%4
    elif i=='L':
        dir=(dir+3)%4
    else:
        x,y=x+dx[dir],y+dy[dir]
    
    if in_range(x,y):
        ans+=mat[x][y]
print(ans)