def print_n_lines(n,m):
    for i in range(n):
        print("1"*m)
n,m=list(map(int,input().split()))
print_n_lines(n,m)