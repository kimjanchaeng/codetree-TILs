n=int(input())

arr=list(map(int,input().split()))
# print(arr)
# st=min(arr)
# ls=max(arr)
# print(max(arr))
cnt=0
for i in range(n-1):
    for j in range(i+1,n):
        for k in range(min(arr[i],arr[j]),max(arr[i],arr[j])):
            if arr[i]-k==k-arr[j]:
                cnt+=1
print(cnt)