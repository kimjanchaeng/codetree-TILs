N, M = list(map(int,input().split()))
A=[0]
B=[0]
cur=0
cur1=0
for i in range(N+M):
    v, t = list(map(int,input().split()))
    if i<N:
        for j in range(1,t+1):
            cur+=v
            A.append(cur)
    else:
        for j in range(1,t+1):
            cur1+=v
            B.append(cur1)

cnt=0
for i in range(2,len(A)+1):
    if A[i-1]==B[i-1] and A[i]==B[i]:
        continue
    elif A[i-1]==B[i-1] and A[i]!=B[i]:
        cnt+=1

print(cnt)