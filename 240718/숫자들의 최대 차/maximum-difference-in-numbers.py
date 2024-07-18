n , k = list(map(int,input().split()))
arr=[int(input()) for i in range(n)]
# print(arr)
sta=min(arr)
fin=max(arr)

ans=0
for i in range(sta,fin+1):
    cnt=0
    for j in range(n):
        if arr[j]>=i and arr[j]<=i+k:
            cnt+=1
        
    ans=max(cnt,ans)

print(ans)