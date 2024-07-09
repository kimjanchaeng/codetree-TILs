arr=list(map(int,input().split()))

def get_avg(a,b,c):
    sum1=a+b+c
    sum2=sum(arr)-sum1
    return abs(sum1-sum2)
avg=0
ans=100000
for i in range(6):
    for j in range(i+1,6):
        for k in range(j+1,6):
            avg=get_avg(arr[i],arr[j],arr[k])
        ans=min(ans,avg)

print(ans)