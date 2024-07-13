N , B = list(map(int,input().split()))

pre=[int(input()) for i in range(N)]
pre.sort()
# print(pre)
# print(pre[::-1])
ans=0
for i in range(N):
    sum1=0
    cnt=0
    for j in range(N):
        if i==j:
            sum1+=pre[j]//2
        else:
            sum1+=pre[j]

        if sum1>B:
            continue
        else:
            cnt+=1
    ans=max(ans,cnt)
print(ans)