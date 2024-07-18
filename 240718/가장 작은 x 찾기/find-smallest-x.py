import sys
n=int(input())
arr= [list(map(int,input().split())) for i in range(n)]

# n=1
# arr=[[3332, 8726]]
# print(arr)
INT_MAX=sys.maxsize
ans=INT_MAX
for i in range(1,10000):
    x=i
    s=i
    cnt=0
    for j in arr:
        s*=2
        if s>=j[0] and s<=j[1]:
            cnt+=1
        else:
            break
    
    if cnt==len(arr):
        ans=min(ans,x)
print(ans)