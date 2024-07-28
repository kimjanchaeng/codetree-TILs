import sys
N,K= list(map(int,input().split()))
arr=list(map(int,input().split()))
# print(arr)
INT_MAX=sys.maxsize
ans=INT_MAX

for i in range(10000-K+1):
    small=i
    big=i+K

    cnt=0
    for k in range(N):
        if arr[k]<small or arr[k]>big:
            if abs(big-arr[k])>abs(small-arr[k]):
                cnt+=abs(small-arr[k])*abs(small-arr[k])
            else:
                cnt+=abs(big-arr[k])*abs(big-arr[k])
    
    ans=min(cnt,ans) 

print(ans)