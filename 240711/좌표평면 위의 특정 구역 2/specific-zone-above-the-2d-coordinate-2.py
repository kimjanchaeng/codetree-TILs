import sys
N=int(input())

INT_MAX=sys.maxsize


x_list=[]
y_list=[]
for i in range(N):
    x,y=list(map(int,input().split()))
    x_list.append(x)
    y_list.append(y)
# print(x_list)

ans=INT_MAX
area=0
for i in range(N):
    x_max=-INT_MAX
    y_max=-INT_MAX
    x_min=INT_MAX
    y_min=INT_MAX
    for j in range(N):
        if i==j:
            continue
        # print(x_list[j])
        x_max=max(x_max,x_list[j])
        x_min=min(x_min,x_list[j])
        y_max=max(y_max,y_list[j])
        y_min=min(y_min,y_list[j])
    # print(x_max,x_min)
    area=(x_max-x_min)*(y_max-y_min)
    # print(max(x_list),min(x_list))
    # print(area)
    ans=min(area,ans)
print(ans)