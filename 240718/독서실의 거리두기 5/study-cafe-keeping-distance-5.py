import sys
n=int(input())
# seat=list(map(int,input().split()))
s=input()
seat= [int(i) for i in s]
# print(seat)
INT_MAX=sys.maxsize
ans=INT_MAX

arr=[]
for i in range(n):
    if seat[i]==1:
        arr.append(i)
# print(arr)

for i in range(n):
    for j in arr:
        if i==j:
            continue
        dis=abs(j-i)
        if dis>1:
            ans=min(dis,ans)
        else:
            break
print(ans)
# for i in range(n):
#     tmp_seat=[seat[j] for j in range(n)]
#     if tmp_seat[i]!=1:
#         tmp_seta[i]=2