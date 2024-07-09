N, H, T=list(map(int,input().split()))
arr=list(map(int,input().split()))
arr_alt=[]
for i in arr:
    arr_alt.append(abs(H-i))
# print(arr_alt)

ans=100000
for i in range(N-T+1):
    s=0
    for j in range(i,i+T):
        s+=arr_alt[j]
    ans=min(ans,s)
print(ans)