N, M = list(map(int,input().split()))
A=list(map(int,input().split()))
B=list(map(int,input().split()))
# B.sort()

ans=0
for i in range(N-len(B)+1):
    cnt=0
    s=[]
    for j in range(i,i+len(B)):
        s.append(A[j])
    s.sort()
    B.sort()
    for i in range(len(B)):
        if s[i]==B[i]:
            cnt+=1

    if cnt==len(B):
        ans+=1


print(ans)