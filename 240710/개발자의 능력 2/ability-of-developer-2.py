import sys
arr=list(map(int,input().split()))
# print(arr)
INT_MAX=sys.maxsize
arr.sort()
sum3=arr[0]+arr[-1]
ans=INT_MAX
s=0
for i in range(1,5):
    for j in range(i+1,5):
        sum1=arr[i]+arr[j]
        sum2=sum(arr)-sum1-sum3
        s=max(sum1,sum2,sum3)-min(sum1,sum2,sum3)
    ans=min(ans,s)
print(ans)