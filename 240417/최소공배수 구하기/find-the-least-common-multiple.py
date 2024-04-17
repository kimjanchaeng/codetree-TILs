def print_gcd(n,m):
    a=1
    for i in range(min(n,m),n*m+1):
        if i%n==0 and i%m==0:
            print(i)
            break
    




n, m= list(map(int,input().split()))
print_gcd(n,m)