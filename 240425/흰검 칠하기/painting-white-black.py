n=int(input())

block=['0']*2000
c=1000
for i in range(n):
    a, b= list(map(str,input().split()))

    if b=='R':
        for j in range(c,c+int(a)):
            # print(block[1000][-1])
            if block[j][-1]!='G':
                block[j]=block[j]+'B' 
                # print(block[j])
                cnt=0
                cnt1=0
                for k in block[j]:
                    if k=='W':
                        cnt+=1
                    elif k=='B':
                        cnt1+=1
                if cnt>=2 and cnt1>=2:
                    block[j]=block[j]+'G'
            else:
                continue 
        c=c+int(a)
    else:
        for j in range(c-int(a),c):
            if block[j][-1]!='G':
                block[j]=block[j]+'W'
                cnt=0
                cnt1=0
                for k in block[j]:
                    if k=='W':
                        cnt+=1
                    elif k=='B':
                        cnt1+=1
                if cnt>=2 and cnt1>=2:
                    block[j]=block[j]+'G' 
            else:
                continue
        c=c-int(a)

w=0
b=0
g=0
for i in block:
    if i[-1]=='W':
        w+=1
    elif i[-1]=='B':
        b+=1
    elif i[-1]=='G':
        g+=1

print(w,b,g)