N=int(input())
arr=list(map(int,input().split()))
cnt=0
M=N+1
for i in range(1,M):
    for j in range(1,M):
        for k in range(1,M):
            if abs(i-arr[0])<=2 or abs(j-arr[1])<=2 or abs(k-arr[2])<=2:
                cnt+=1

print(cnt)