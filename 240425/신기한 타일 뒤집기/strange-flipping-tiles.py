n=int(input())

block=['0']*2000
c=1000
for i in range(n):
    a, b= list(map(str,input().split()))

    if b=='R':
        for j in range(c,c+int(a)):
            # print(block[1000][-1])
            block[j]='B'     
        c=c+int(a)-1
        
    else:
        for j in range(c,c-int(a),-1):
            
            block[j]='W'
            
        c=c-int(a)+1
        
w=0
b=0
for i in block:
    if i=='W':
        w+=1
    elif i=='B':
        b+=1


print(w,b)