n, m = list(map(int,input().split()))
arr=[list(map(int,input().split())) for i in range(m)]
# print(arr)
ans=0
for i in range(m):
    cnt=1
    for j in range(i+1,m):
        if arr[i]==arr[j] or arr[i]==[arr[j][1],arr[j][0]]:
            cnt+=1
    ans=max(ans,cnt)

print(ans)