import sys
N=int(input())

arr=[list(map(int,input().split())) for i in range(N)]
INT_MAX=sys.maxsize

def dist(a,b,c,d):
    return (a-c)*(a-c)+(b-d)*(b-d)
s=0
ans=INT_MAX
for i in range(N):
    for j in range(i+1,N):
        s=dist(arr[i][0],arr[i][1],arr[j][0],arr[j][1])
        ans=min(ans,s)
print(ans)