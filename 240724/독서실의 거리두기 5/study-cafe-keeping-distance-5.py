# n=17
# s='10001001000100000'
# n=14
# s='10000000100000'

# n=15
# s='010001001000110'

import sys
n=int(input())
s=input()
seat= [int(i) for i in s]
# print(seat)
INT_MAX=sys.maxsize
ans=INT_MAX

# arr=[]
# for i in range(n):
#     if seat[i]==1:
#         arr.append(i)
# print(arr)
# ans=0
# for i in range(n):
#     for j in arr:
#         if i==j or abs(i-j)<=1:
#             continue
#         dis=abs(j-i)
#         ans1=min(dis,ans1)
#     ans=max(ans1,ans)
# print(ans)
las=[]
for i in range(n):
    tmp_seat=[seat[j] for j in range(n)]
    if tmp_seat[i]!=1:
        tmp_seat[i]=1
    else:
        continue

    arr=[]
    for k in range(n):
        if tmp_seat[k]==1:
            arr.append(k)

    s=len(arr)
    flag=True
    s1=[]
    for l in range(s-1):
        dis=abs(arr[l]-arr[l+1])
        if dis<=1:
            flag=False
            
        s1.append(dis)

    if flag==True:
        las.append(min(s1))

if len(las)==0:
    print(1)
else:
    print(max(las))