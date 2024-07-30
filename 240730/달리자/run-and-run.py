n=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
# print(n,A,B)

cnt=0
for i in range(n-1):
    if A[i]>B[i]:
        cnt+=A[i]-B[i]
        A[i+1]+=A[i]-B[i]
        A[i]=B[i]
        # print(A)

if A==B:
    print(cnt)