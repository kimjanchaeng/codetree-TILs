arr=list(map(int,input().split()))

# arr=[4,7,9]
cnt=0
for i in range(2):
    diff=abs(arr[i]-arr[i+1])
    if diff>2:
        cnt+=1
    if diff==2:
        cnt=1
        break
print(cnt)