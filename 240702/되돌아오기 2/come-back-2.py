s=input()
# print(s)

x,y=0,0
dx,dy=[0,1,0,-1],[1,0,-1,0]
dir=3

ans=-1
cnt=0
t=0
for i in s:
    if i=='F':
        x,y=x+dx[dir],y+dy[dir]
        cnt+=1
    elif i=='L':
        dir=(dir+3)%4
    else:
        dir=(dir+1)%4

    t+=1
    if x==0 and y==0 and cnt>0:
        ans=t
        break
print(ans)