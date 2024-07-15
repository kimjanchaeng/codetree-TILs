n=int(input())
arr=list(map(int,input().split()))

# n=20
# arr=[83, 25, 47, 61, 14, 13, 71, 100, 95, 79, 26, 88, 34, 54, 42, 3, 57, 72, 44, 94 ]


ans=0

for k in range(1,101):
    cnt=0
    for i in range(n):
        for j in range(i+1,n):
            if max(arr[i],arr[j])-k == k-min(arr[i],arr[j]):
            # if (arr[i]+arr[j])/2==k:
                cnt+=1
    ans=max(ans,cnt)
print(ans)