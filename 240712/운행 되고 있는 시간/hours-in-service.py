import sys
N=int(input())
arr=[list(map(int,input().split())) for i in range(N)]

# time=[0]*1001
INT_MAX=sys.maxsize

def cal_wt(a):
    time=[0]*1001
    for i in range(N):
        if i==a:
            continue
        for j in range(arr[i][0],arr[i][1]):
            time[j]=1
    
    return sum(time)

ans=-INT_MAX
for i in range(N):
    ans=max(cal_wt(i),ans)
print(ans)