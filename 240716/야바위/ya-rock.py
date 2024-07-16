N=int(input())



ya=[list(map(int,input().split())) for i in range(N)]
# print(ya)

ans=0
for i in range(1,N+1):
    # a,b,c=list(map(int,input().split()))
    arr=[0]*(N+1)
    arr[i]=1
    cnt=0
    for j in ya:
        a,b,c=j[0],j[1],j[2]
        arr[a],arr[b]=arr[b],arr[a]
        cnt+=arr[c]
    ans=max(ans,cnt)
print(ans)