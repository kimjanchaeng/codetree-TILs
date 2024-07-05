N=int(input())

s=input()

cnt=0
cnt1=0
cnt2=0

# for i in s:
#     # print(i)
#     if i=='C':
#         cnt+=1
#     elif i=='O':
#         cnt1+=1
#     else:
#         cnt2+=1
# print(cnt*cnt1*cnt2)

for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if s[i]=='C' and s[j]=='O' and s[k]=='W':
                cnt+=1
print(cnt)