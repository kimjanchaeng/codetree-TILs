N=int(input())

arr=[0]*101
loc_arr=[]
for i in range(N):
    loc,s= list(map(str,input().split()))
    # fir=min(fir,int(loc))
    # las=max(las,int(loc))
    arr[int(loc)]=s
    loc_arr.append(int(loc))
ans=0
loc_arr.sort()
# print(loc_arr[1:])
l=len(loc_arr)
for i in range(l):
    for j in range(i+1,l):
        cnt=0
        cnt1=0
        fir=200
        las=-1
        for k in range(i,j):
            fir=min(fir,loc_arr[k])
            las=max(las,loc_arr[k])
            if arr[loc_arr[k]]=='G':
                cnt+=1
            else:
                cnt1+=1
        if cnt==cnt1:
            ans=max(ans,las-fir)
print(ans)