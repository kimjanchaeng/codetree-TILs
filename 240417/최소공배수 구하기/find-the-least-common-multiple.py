def print_gcd(n,m):
    a=1
    for i in range(1,max(n,m)+1):
        if n%i==0 and m%i==0:
            a*=i
    
    print(a)




n, m= list(map(int,input().split()))
print_gcd(n,m)