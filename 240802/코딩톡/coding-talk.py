n, m, p = list(map(int,input().split()))
s1='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# s=list(map(str,s1))
# print(s)

s=s1[:n]
exist=[]
# print(loc)

for i in range(n):
    c,u=list(map(str,input().split()))
    if i>=p-1:
        if c not in exist:
            exist.append(c)

# print(exist)
for j in s:
    if j not in exist:
        print(j,end=' ')