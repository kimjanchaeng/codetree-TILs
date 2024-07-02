t,n = list(map(int,input().split()))
r,c,d=list(map(str,input().split()))
# print(str(d))
dx,dy = [0, 1, -1,  0],[1, 0,  0, -1]
dir={'R': 0,
    'D': 1,
    'U': 2,
    'L': 3} 
# print(type(d))
mat=[[0]*n for i in range(n)]
# print(mat)
x=int(r)-1
y=int(c)-1
def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n
# d=str(d)

c_dir=dir[d]
for i in range(t):
    nx,ny=x+dx[c_dir], y+dy[c_dir]

    if in_range(nx,ny):
        x,y=nx,ny
    else:
        c_dir=3-c_dir



print(x+1,y+1)