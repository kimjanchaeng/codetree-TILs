N,K=list(map(int,input().split()))

arr=[0]*101
for i in range(N):
    can,loc=list(map(int,input().split()))
    arr[loc]+=can

ans=0
for i in range(1,101-(2*K+1)+2):
    ans=max(sum(arr[i:i+2*K+1]),ans)
print(ans)