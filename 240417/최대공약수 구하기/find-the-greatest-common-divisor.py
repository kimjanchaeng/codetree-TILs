n,m = list(map(int,input().split()))

a=[]
for i in range(1,n+1):
    if n%i==0 and m%i==0:
        a.append(i)

print(max(a))