N, M = list(map(int,input().split()))
A=list(map(int,input().split()))
B=list(map(int,input().split()))

ans=0
for i in range(N-len(B)+1):
    cnt=0
    for j in range(i,i+len(B)):
        if A[j] in B:
            cnt+=1
    if cnt==len(B):
        ans+=1

print(ans)