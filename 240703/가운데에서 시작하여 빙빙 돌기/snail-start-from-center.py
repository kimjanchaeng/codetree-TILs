# # n = int(input())
# n=5

# mat=[[0]*n for i in range(n)]

# def in_range(x,y):
#     return 0<=x and x<n and 0<=y and y<n

# x,y= n//2,n//2
# # print(x)
# dir=0
# dx,dy=[0,1,0,-1],[1,0,-1,0]

# mat[x][y]=1
# for i in range(2,n*n+1):
#     nx,ny=x+dx[dir],y+dy[dir]

#     if not in_range(nx,ny) or mat[nx][ny]!=0:
#         dir=(dir+3)%4
    
#     x,y=x+dx[dir],y+dy[dir]
#     mat[x][y]=i

# # print(mat)
# for i in mat:
#     for j in i:
#         print(j,end=' ')
#     print()

n = int(input())
arr = [
    [0] * n
    for _ in range(n)
]

def in_range(x,y) :
    return 0 <= x and x < n and 0 <= y and y < n

dxs, dys = [0,-1,0,1],[-1,0,1,0]
cur_dir = 0
x,y = n -1, n -1
arr[x][y] = n ** 2
for i in range(n**2 -1,0, -1) :
    nx, ny = x + dxs[cur_dir], y + dys[cur_dir]
    if not in_range(nx, ny) or arr[nx][ny] > 0 :
        cur_dir = (cur_dir + 1) % 4
    
    x, y = x + dxs[cur_dir], y + dys[cur_dir]
    arr[x][y] = i

for row in arr :
    for elem in row :
        print(elem, end = " ")
    print()