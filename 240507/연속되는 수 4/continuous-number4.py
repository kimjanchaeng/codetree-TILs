n=int(input())

s=[]

for i in range(n):
    a=int(input())
    s.append(a)

cnt=1
b=[]
for j in range(len(s)-1):
    if s[j]<s[j+1]:
        cnt+=1
    else:
        b.append(cnt)
        cnt=1
print(max(b))