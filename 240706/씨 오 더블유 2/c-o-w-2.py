N=int(input())

s=input()

cnt=0
cnt1=0
cnt2=0
for i in s:
    if i=='C':
        cnt+=1
    elif i=='O':
        cnt1+=1
    else:
        cnt2+=1
print(cnt*cnt1*cnt2)