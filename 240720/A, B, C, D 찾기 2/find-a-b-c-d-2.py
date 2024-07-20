arr=list(map(int,input().split()))
arr.sort()
# print(arr)
n=len(arr)

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            s=[]
            for l in range(k+1,n):
                A,B,C,D=arr[i],arr[j],arr[k],arr[l]
                s=[ A, B, C, D, A + B, B + C, C + D, D + A, A + C, B + D, A + B + C, A + B + D, A + C + D, B + C + D, A + B + C + D]
                if sorted(s)==arr:
                    print(A,B,C,D)
                    break