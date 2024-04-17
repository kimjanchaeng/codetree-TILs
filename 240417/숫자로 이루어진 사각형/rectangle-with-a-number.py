def print_n_lines(n):
    k=1
    for i in range(n):
        for j in range(n):
            if k>9:
                k=1
            print(k,end=' ')
            k+=1

        print()

n=int(input())
print_n_lines(n)