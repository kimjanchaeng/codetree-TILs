N=int(input())

mat=[[0]*200 for i in range(200)]

dx,dy=[0,1,0,-1],[1,0,-1,0]
dir={
    'E':0,
    'S':1,
    'W':2,
    'N':3
}

x,y=100,100
mat[x][y]='a'
cnt=1
answer=-1

for i in range(N):
    d, t= list(map(str,input().split()))
    for i in range(int(t)):
        cur_dir=dir[d]
        x,y=x+dx[cur_dir],y+dy[cur_dir]
        if mat[x][y]=='a':
            answer=cnt
        mat[x][y]=i
        cnt+=1

print(answer)