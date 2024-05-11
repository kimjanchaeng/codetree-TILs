n,m = list(map(int,input().split()))

A=[0]
B=[0]
cur=0
cur1=0
for i in range(n+m):
    t, d = list(map(str,input().split()))
    if i<n:
        if d=='R':
            cur+=1
            A.append(cur)
        else:
            cur-=1
            A.append(cur)
    else:
        if d=='R':
            cur1+=1
            B.append(cur1)
        else:
            cur1-=1
            B.append(cur1)

a=len(A)
b=len(B)

if a>b:
    for i in range(a-b):
        A.append(A[-1])
else:
    for i in range(b-a):
        B.append(B[-1])

cnt=0
for j in range(2,len(A)):
    if A[i-1]!=B[i-1] and A[i]==B[i]:
        cnt+=1
    else:
        continue
print(cnt)