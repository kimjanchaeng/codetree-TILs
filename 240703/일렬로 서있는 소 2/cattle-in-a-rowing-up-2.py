n=int(input())
arr=list(map(int,input().split()))
cnt=0
for i in range(n):
    for j in range(i+1,n):
        if arr[i]<arr[j]:
            for k in range(j+1,n):
                if arr[j]<arr[k]:
                    cnt+=1

print(cnt)