n, t = list(map(int,input().split()))
a=list(map(int,input().split()))
# print(a)

cnt=0
num=0
ans=0
for i in a:
    if i>t: 
        if num<i:
            cnt+=1
        else:
            cnt=1
    else:
        cnt=0
    ans=max(cnt,ans)
    num=i
print(ans)