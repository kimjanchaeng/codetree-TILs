x,y=0,0
dir=3
dx,dy=[1,0,-1,0], [0,-1,0,1]
n=input()
for i in range(len(n)):
    # print(i)
    if n[i]=='R':
        dir=(dir+1)%4
    elif n[i]=='L':
        dir=(dir+3)%4
    else:
        x,y=x+dx[dir],y+dy[dir]

print(x,y)