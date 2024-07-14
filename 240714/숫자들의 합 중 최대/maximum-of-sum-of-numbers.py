X, Y = list(map(int,input().split()))

ans=0
for i in range(X,Y+1):
    sum1=0
    arr=list(map(int,list(str(i))))
    for i in arr:
        sum1+=int(i)

    ans=max(sum1,ans)

print(ans)