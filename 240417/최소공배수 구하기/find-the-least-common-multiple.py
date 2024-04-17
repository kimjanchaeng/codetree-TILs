n, m= list(map(int,input().split()))

a=1
for i in range(1,min(n,m)+1):
    if n%i==0 and m%i==0:
        a*=i


print(a)