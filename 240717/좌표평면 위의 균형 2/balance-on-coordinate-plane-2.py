import sys
n=int(input())
arr=[list(map(int,input().split())) for i in range(n)]
# print(arr)
# ans=0
INT_MAX=sys.maxsize
ans_f=INT_MAX

for i in range(1,101):
    for j in range(1,101):
        if i%2!=0 or j%2!=0:
            continue
        cor=[0]*4

        for k in arr:
            x=k[0]
            y=k[1]
            if x<i and y>j:
                cor[0]+=1
            elif x>i and y>j:
                cor[1]+=1
            elif x>i and y<j:
                cor[2]+=1
            else:
                cor[3]+=1
        ans=max(cor)
        ans_f=min(ans,ans_f)

print(ans_f)