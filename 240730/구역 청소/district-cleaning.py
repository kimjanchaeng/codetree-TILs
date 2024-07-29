a,b=list(map(int,input().split()))
c,d=list(map(int,input().split()))

arr=[0]*101

for i in range(a,b):
    arr[i]=1
for j in range(c,d):
    arr[j]=1

cnt=0
for k in arr:
    if k==1:
        cnt+=1

print(cnt)