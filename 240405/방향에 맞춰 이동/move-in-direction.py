n=int(input())
x,y=0,0
# nx,ny=0,0
#W,S,N,E
dx,dy=[-1,0,0,1],[0,-1,1,0]

for i in range(n):
    dir,b=map(str,input().split())
    b=int(b)

    # for i in range(b):
    #     if dir=='W':
    #         nx,ny=x+dx[0],y+dy[0]      #아니 더해주기만 하면 뭐해 update한거에다가 더해줘야지
    #     elif dir=='S':
    #         nx,ny=x+dx[1],y+dy[1]
    #     elif dir=='N':
    #         print(1)
    #         nx,ny=x+dx[2],y+dy[2]
    #         print(nx,ny)
    #     else:
    #         nx,ny=x+dx[3],y+dy[3]
    # # print(nx,ny)

    for i in range(b):
        if dir=='W':
            x+=dx[0]
            y+=dy[0]      
        elif dir=='S':
            x+=dx[1]
            y+=dy[1] 
        elif dir=='N':
            x+=dx[2]
            y+=dy[2]
        else:
            x+=dx[3]
            y+=dy[3]

print(x,y)