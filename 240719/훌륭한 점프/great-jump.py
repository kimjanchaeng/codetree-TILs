n, k =list(map(int,input().split()))
arr=list(map(int,input().split()))
# print(arr)
def is_possible(a):
    idx=[]
    for k,elem in enumerate(arr):
        if elem>=a:
            idx.append(k)
    
    # print(idx)
    s=len(idx)
    if s>1:
        for j in range(s-1):
            dis=abs(idx[j]-idx[j+1])
            if dis>2:
                return False
    else:
        return False

    return True




ans=0
for i in range(max(arr),0,-1):
    # print(is_possible(i))
    if is_possible(i):
        ans=max(ans,i)
print(ans)