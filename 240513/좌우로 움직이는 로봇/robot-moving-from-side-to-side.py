n,m = list(map(int,input().split()))

A=[0]
B=[0]
cur=0
cur1=0
for i in range(n+m):
    t, d = list(map(str,input().split()))
    t=int(t)
    if i<n:
        if d=='R':
            cur+=t
            A.append(cur)
        else:
            cur-=t
            A.append(cur)
    else:
        if d=='R':
            cur1+=t
            B.append(cur1)
        else:
            cur1-=t
            B.append(cur1)

a=len(A)
b=len(B)
# print(a,b)

if a>b:
    for i in range(a-b):
        # print(a-b)
        B.append(B[-1])
        
else:
    for i in range(b-a):
        # print(b-a)
        A.append(A[-1])

cnt=0
# print(len(A),len(B))
# print(A)
# print(B)

for j in range(2,len(A)):
    if A[j-1]>B[j-1] and A[j]<=B[j]:
        cnt+=1
    elif A[j-1]<B[j-1] and A[j]>=B[j]:
        cnt+=1
print(cnt)