import sys

n=int(input())
arr=list(map(int,input().split()))

# print(arr)
INT_MAX=sys.maxsize
ans=INT_MAX
for i in range(n):
    arr[i]*=2
    # print(arr)

    for j in range(n):
        remain_arr=[]
        for k in range(n):
            if j==k:
                continue
            remain_arr.append(arr[k])

        # print(remain_arr)
        sum1=0
        for l in range(len(remain_arr)-1):
            sum1+=abs(remain_arr[l]-remain_arr[l+1])
        # print(sum1)
    
        ans=min(sum1,ans)

    arr[i]//=2
    # print(arr)

print(ans)