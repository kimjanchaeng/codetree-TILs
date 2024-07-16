A, B, C= list(map(int,input().split()))
ans=0
for i in range(1000):
    for j in range(1000):
        sum1=A*i+B*j
        diff=C-sum1
        if diff>=0:
            ans=max(ans,sum1)
print(ans)