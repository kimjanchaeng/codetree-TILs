x, y = list(map(int,input().split()))
# x=331 
# y=6267

def calc(a):
    arr=list(map(int,str(a)))
    arr.sort()
    s=len(arr)
    cnt=1
    for i in range(s-1):
        if arr[i]==arr[i+1]:
            cnt+=1
            if cnt==2:
                fir=arr[i]
            if cnt==s-1:
                las=arr[i+1]
    if cnt==s-1 and fir==las:
        return True
    else:
        return False
ans=0
for i in range(x,y+1):
    if calc(i):
        ans+=1
print(ans)