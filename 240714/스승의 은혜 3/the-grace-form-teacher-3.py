N, B = list(map(int,input().split()))
arr=[list(map(int,input().split())) for i in range(N)]
# print(arr)
ans=0
for i in range(N):
    tmp=[arr[i] for i in range(N)]

    tmp[i][0]//=2
    tmp.sort()

    cnt=0
    sum1=0
    for j in range(N):
        sum1+=arr[j][0]+arr[j][1]
        if sum1>B:
            break
        else:
            cnt+=1

    ans=max(cnt,ans)
    


print(ans)