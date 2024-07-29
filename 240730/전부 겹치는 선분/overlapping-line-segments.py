n=int(input())
arr=[list(map(int,input().split())) for i in range(n)]
# print(arr)

def intersect(a,b,c,d):
    if d<a or b<c:
        return False
    else:
        return True

flag=True
for i in range(n):
    for j in range(i+1,n):
        x1,x2,x3,x4=arr[i][0],arr[i][1],arr[j][0],arr[j][1]
        if not intersect(x1,x2,x3,x4):
            print('No')
            flag=False
if flag:
    print('Yes')