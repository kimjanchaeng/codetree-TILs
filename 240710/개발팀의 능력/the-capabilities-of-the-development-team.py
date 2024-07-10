import sys

arr=list(map(int,input().split()))
N=5
INT_MAX=sys.maxsize
ans=INT_MAX
t1,t2,t3,s=0,0,0,0
for i in range(N):
    for j in range(i+1,N):
        
        for k in range(N):
            for l in range(k+1,N):
                if i==k or i==l or j==k or j==l:
                    continue
                t1=arr[i]+arr[j]
                t2=arr[k]+arr[l]
                t3=sum(arr)-t1-t2
                if t1!=t2 and t1!=t3 and t2!=t3:
                    s=max(t1,t2,t3)-min(t1,t2,t3)
                ans=min(ans,s)
if ans==INT_MAX:
    print(-1)

print(ans)