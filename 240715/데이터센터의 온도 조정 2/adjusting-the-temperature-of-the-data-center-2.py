N, C, G, H =list(map(int,input().split()))

T=[list(map(int,input().split())) for i in range(N)]
# print(T)
def work(a,b,t):
    if t<a:
        return C
    elif a<=t and t<=b:
        return G
    else:
        return H

max_range=0
for i in range(N):
    max_range=max(max_range,T[i][1])
# print(max_range)

ans=0
for j in range(max_range+3):
    s=0
    for i in range(N):
        s+=work(T[i][0],T[i][1],j)
        
    ans=max(s,ans)

print(ans)