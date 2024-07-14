x, y = list(map(int,input().split()))

def calc(a):
    arr=list(map(int,str(a)))
    arr.sort()
    s=len(arr)
    cnt=1
    for i in range(s-1):
        if arr[i]==arr[i+1]:
            cnt+=1
    if cnt==s-1:
        return True
    else:
        return False
ans=0
for i in range(x,y+1):
    if calc(i):
        ans+=1
print(ans)