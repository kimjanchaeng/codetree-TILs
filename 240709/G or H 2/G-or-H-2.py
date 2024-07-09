# 2
# 2 G
# 4 G

N=int(input())
# N=2

arr=[0]*101
loc_arr=[]
for i in range(N):
    loc,s= list(map(str,input().split()))
    # fir=min(fir,int(loc))
    # las=max(las,int(loc))
    arr[int(loc)]=s
    loc_arr.append(int(loc))
# arr[2]='G'
# arr[4]='G'
ans=0
# loc_arr.append(2)
# loc_arr.append(4)
loc_arr.sort()
# print(loc_arr)
l=len(loc_arr)
for i in range(l):
    for j in range(i+1,l):
        cnt=0
        cnt1=0
        fir=0
        las=0
        for k in range(i,j+1):
            # fir=min(fir,loc_arr[k])
            # las=max(las,loc_arr[k])
            fir=loc_arr[i]
            las=loc_arr[j]
            if arr[loc_arr[k]]=='G':
                cnt+=1
            else:
                cnt1+=1
        if cnt==cnt1:
            ans=max(ans,las-fir)
        elif cnt%2==0 and cnt1==0:
            ans=max(ans,las-fir)
        elif cnt1%2==0 and cnt==0:
            ans=max(ans,las-fir)
print(ans)