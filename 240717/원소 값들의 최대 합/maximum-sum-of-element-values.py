n , m = list(map(int,input().split()))
arr=list(map(int,input().split()))
ans=0
for i in range(n):
    idx=i
    sum1=0
    # sum1=arr[idx]
    for j in range(m):
        sum1+=arr[idx]
        idx=arr[idx]-1
    ans=max(sum1,ans)

print(ans)