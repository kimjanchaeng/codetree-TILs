N=int(input())
arr=[list(map(int,input().split())) for i in range(N)]
# print(mat)

ans=0
for i in range(N):
    for j in range(N-2):
        ans=max(ans,arr[i][j]+arr[i][j+1]+arr[i][j+2])

print(ans)