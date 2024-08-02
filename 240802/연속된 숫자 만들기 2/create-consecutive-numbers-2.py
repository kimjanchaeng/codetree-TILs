arr=list(map(int,input().split()))
# print(arr)
# diff=[]
cnt=0
for i in range(2):
    diff=abs(arr[i]-arr[i+1])
    if diff>1:
        cnt+=1
print(cnt)