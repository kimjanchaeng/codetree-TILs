# n=int(input())
# h=[int(input()) for i in range(n)]

# n=5
# h=[
# 149,
# 934,
# 175,
# 53,
# 933,
# ]

# print(h)
# max1=0
# for i in range(1,1001):
#     tmp=[h[l] for l in range(n)]
#     cnt=0
#     # print(tmp)
#     for j in range(n):
#         tmp[j]-=i
    
#     if tmp[0]>0:
#         flag=1
#     else:
#         flag=0

#     for k in range(1,n):
#         if flag==0 and tmp[k]>0:
#             cnt+=1
#             flag=1
#         elif flag==1 and tmp[k]<=0:
#             cnt+=1
#             flag=0

#     max1=max(max1,cnt)
# print(max1)
    
    
N = int(input())

ice_berg = [0] * 100

for i in range(N):
    ice_berg[i] = int(input())

max_hegith = max(ice_berg)

max_result = 0
for i in range(max_hegith):
    temp_ice_berg = [ ice_berg[_] for _ in range(N)]

    for j in range(N):
        if temp_ice_berg[j] - i < 0:
            temp_ice_berg[j] = 0
        else:
            temp_ice_berg[j] -= i
    
    count = 0
    bit = 0
    for check in range(N):
        if temp_ice_berg[check] != 0:
            bit = 1

        if bit == 1 and temp_ice_berg[check] == 0:
            bit = 0
            count += 1
            
        if bit == 1 and check == N-1:
            count += 1
    max_result = max(max_result, count)

print(max_result)