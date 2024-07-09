import itertools

N, S= list(map(int,input().split()))
arr=list(map(int,input().split()))

arr_alt=list(itertools.combinations(arr,N-2))
# print(arr_alt)
ans=10000
plus=0
for i in arr_alt:
    plus=abs(sum(i)-S)
    ans=min(ans,plus)
print(ans)