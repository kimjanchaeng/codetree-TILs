N , K= list(map(int,input().split()))
cor=[int(input()) for i in range(N)]

# print(input(cor).split())
ans=-1
# s=0
for i in range(N-1):
    # for j in range(i,i+K):
    # print(cor[i+1:min(i+K+1,N)])

    if cor[i] in cor[i+1:min(i+K+1,N)]:
        # print(333)
        ans=max(ans,cor[i])
print(ans)