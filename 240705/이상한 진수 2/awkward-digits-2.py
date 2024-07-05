n=input()
arr=[]
for i in range(len(n)):
    ans=''
    for j in range(len(n)):
        if i==j:
            if n[j]=='1':
                ans+='0'
            else:
                ans+='1'
            
            continue
        
        ans+=n[j]
    
    arr.append(ans)

# print(arr)
# print(arr)
s=max(arr)
ans=0
for i in s:
    ans=2*ans+int(i)
print(ans)