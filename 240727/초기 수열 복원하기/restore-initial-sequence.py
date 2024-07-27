import itertools

n=int(input())
arr=list(map(int,input().split()))
n_arr=[i for i in range(1,n+1)]
# print(n_arr)

arr_las=list(itertools.permutations(n_arr,n))

for i in arr_las:
    s=[]
    for j in range(n-1):
        s.append(i[j]+i[j+1])

    if s==arr:
        for k in i:
            print(k,end=' ')