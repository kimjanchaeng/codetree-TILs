n, m = list(map(int,input().split()))

A=[0]
B=[0]
cur=0
cur1=0
for i in range(n+m):
    v, t = list(map(int,input().split()))

    if i<n:
        for i in range(t):
            cur+=v
            A.append(cur)

    else:
        for i in range(t):
            cur1+=v
            B.append(cur1)

# print(A)
# print(B)
cnt=1
lead=0
for i in range(1,len(A)):
    if A[i]>B[i]:
        if lead==2 or lead==3:
            cnt+=1
            # print(i)
        
        lead=1
    elif A[i]<B[i]:
        if lead==1 or lead==3:
            cnt+=1
            # print(i)
        
        lead=2
    else:
        if lead==1 or lead==2:
            cnt+=1
        lead=3
print(cnt)