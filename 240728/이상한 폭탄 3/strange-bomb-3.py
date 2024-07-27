n , k = list(map(int,input().split()))
loc=[int(input()) for i in range(n)]

arr=[0]*(n)
bomb=[0]*101

for i in range(n):
    for j in range(i+1,min(i+k+1,n)):
        if loc[i]==loc[j] and arr[j]==0:
            arr[i],arr[j]=1,1
            # bomb[arr[j]]+=1
s=[]
for i in loc:
    if i not in s:
        s.append(i)
s.sort()
# print(s)
ans=[0]*(len(s))
for i,elem in zip(arr,loc):
    for k in range(len(s)):
        if i==1 and elem==s[k]:
            ans[k]=ans[k]+1
# print(ans)

big1=max(ans)
ans1=[]
for j in range(len(s)):
    if big1==ans[j]:
        ans1.append(s[j])
print(max(ans1))
# print(arr)
# print(bomb)
# big=max(bomb)

# ans=[]
# for i in range(101):
#     if bomb[i]==big:
#         ans.append(i)
# print(max(ans))