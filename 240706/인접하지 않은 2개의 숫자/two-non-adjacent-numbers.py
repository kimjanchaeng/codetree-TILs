N=int(input())
arr=list(map(int,input().split()))

# ps=0
s=[]
for i in range(N):
    cnt=0
    for j in range(i+2,N):
        ps=0
        ps=arr[i]+arr[j]
        s.append(ps)     
print(max(s))