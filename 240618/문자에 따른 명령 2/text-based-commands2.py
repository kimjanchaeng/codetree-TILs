x,y=0,0
dir=3
dx,dy=[1,0,-1,0], [0,-1,0,1]
n=input().split()
if n[0]=='R':
    dir=(dir+1)%4
else:
    dir=(dir+3)%4
x,y=x+dx[dir],y+dy[dir]
print(x,y)