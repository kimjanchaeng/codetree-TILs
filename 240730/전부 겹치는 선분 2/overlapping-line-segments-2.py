import sys
n=int(input())
arr=[list(map(int,input().split())) for i in range(n)]

INT_MAX = sys.maxsize


flag=False
for i in range(n):
    max_x1 = 0
    min_x2 = INT_MAX
    for j in range(n):
        if i==j:
            continue
        else:
            x1,x2=arr[j][0],arr[j][1]
            max_x1=max(x1,max_x1)
            min_x2=min(x2,min_x2)

    if min_x2 >= max_x1:
        flag=True

if flag==True:
    print('Yes')
else:
    print('No')