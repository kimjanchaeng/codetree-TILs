N, M, K = list(map(int,input().split()))

num=[i for i in range(1,N+1)]
m=[K for i in range(N)]
print

ans=-1
for i in range(M):
    s=int(input())
    m[s-1]-=1
    if m[s-1]==0:
        ans=s
        # print(ans)
        break
print(ans)