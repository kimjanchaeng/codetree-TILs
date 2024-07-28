import sys

n=int(input())
arr=[int(input()) for i in range(n)]
# print(arr)

INT_MAX=sys.maxsize
ans=INT_MAX

# for i in range(n):
#     for j in range(i+1,n):
#         x,y=arr[i],arr[j]
#         if abs(x-y)<=17:
#             big=max(x,y)
#             small=min(x,y)

#             cnt=0
#             for k in range(n):
#                 if i==k or j==k:
#                     continue
                
#                 if abs(big-arr[k])>abs(small-arr[k]):
#                     cnt+=abs(small-arr[k])*abs(small-arr[k])
#                 else:
#                     cnt+=abs(big-arr[k])*abs(big-arr[k])

#             ans=min(cnt,ans)

# print(ans)
for i in range(84):
    big=i+17
    small=i
    cnt=0
    for k in range(n):
        if arr[k]<small or arr[k]>big:
            if abs(big-arr[k])>abs(small-arr[k]):
                cnt+=abs(small-arr[k])*abs(small-arr[k])
            else:
                cnt+=abs(big-arr[k])*abs(big-arr[k])
    
    ans=min(cnt,ans)
print(ans)