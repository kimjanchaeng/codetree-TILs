n=int(input())

digit=[]
for i in range(n):
    s=int(input())
    digit.append(s)

cnt=1
di=[]
result=1
for i in range(len(digit)-1):
    if digit[i]==digit[i+1]:
        cnt+=1
    else:
        # di.append(cnt)   
        cnt=1
    result=max(cnt,result) 
print(result)