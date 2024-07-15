n=int(input())
h=[int(input()) for i in range(n)]

n=5
h=[
149,
934,
175,
53,
933,
]

# print(h)
max1=0
for i in range(1,101):
    tmp=[h[l] for l in range(n)]
    cnt=0
    # print(tmp)
    for j in range(n):
        tmp[j]-=i

    for k in range(n-1):

        if tmp[k]>0 and tmp[k+1]<=0:
            cnt+=1
        elif tmp[k]<=0 and tmp[k+1]>0:
            cnt+=1
    max1=max(max1,cnt)
print(max1)