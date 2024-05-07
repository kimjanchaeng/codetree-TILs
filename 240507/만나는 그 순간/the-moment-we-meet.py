n, m = list(map(int,input().split()))

A=[0]
B=[0]
cur=0
cur1=0
for i in range(n+m):
    d, t = list(map(str,input().split()))
    t=int(t)
    if i<n:
        if d=='R':
            for i in range(t):
                cur+=1
                A.append(cur)
        else:
            for i in range(t):
                cur-=1
                A.append(cur)
    else:
        if d=='R':
            for i in range(t):
                cur1+=1
                B.append(cur1)
        else:
            for i in range(t):
                cur1-=1
                B.append(cur1)

for i in range(1,min(len(A),len(B))):
    if A[i]==B[i]:
        print(i)
        break
    elif i==min(len(A),len(B)) and A[i]!=B[i]:
        print(-1)