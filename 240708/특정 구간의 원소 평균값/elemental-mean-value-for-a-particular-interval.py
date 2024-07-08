N=int(input())
arr=list(map(int,input().split()))
# print(arr)

num=0
for i in range(N):
    for j in range(i,N):
        cnt=0
        s=[]
        for k in range(i,j+1):
            cnt+=1
            s.append(arr[k])
        if sum(s)/cnt in s:
            num+=1

print(num)