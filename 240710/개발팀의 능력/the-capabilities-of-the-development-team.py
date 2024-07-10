# import sys

# # arr=list(map(int,input().split()))
# arr=[1, 7, 8, 3, 8]
# N=5
# INT_MAX=sys.maxsize
# ans=INT_MAX
# t1,t2,t3,s=0,0,0,0
# Flag=False
# for i in range(N):
#     for j in range(i+1,N):
        
#         for k in range(N):
#             for l in range(k+1,N):
#                 if i==k or i==l or j==k or j==l:
#                     continue
#                 t1=arr[i]+arr[j]
#                 t2=arr[k]+arr[l]
#                 t3=sum(arr)-t1-t2
#                 if t1!=t2 and t1!=t3 and t2!=t3:
#                     Flag=True
#                     s=max(t1,t2,t3)-min(t1,t2,t3)
#                     ans=min(ans,s)
# if Flag==False:
#     print(-1)
# else:
#     print(ans)

import sys

arr = list(map(int, input().split()))
total = sum(arr)
is_possible = False
min_diff = sys.maxsize

for i in range(5):
    for j in range(i+1, 5):
        for k in range(5):
            if k != i and k != j:
                team_b = arr[i] + arr[j]
                team_c = arr[k]
                team_a = total - team_c - team_b
                if team_a != team_b and team_b != team_c and team_c != team_a:
                    is_possible = True
                    diff = max(team_a, team_b, team_c) - min(team_a, team_b, team_c)
                    min_diff = min(min_diff, diff)

if is_possible:
    print(min_diff)
else:
    print(-1)