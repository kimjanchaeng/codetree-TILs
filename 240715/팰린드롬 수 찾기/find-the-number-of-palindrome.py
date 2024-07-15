x, y= list(map(int,input().split()))
cnt=0
for i in range(x,y+1):
    arr=list(map(int,str(i)))
    if arr==arr[::-1]:
        cnt+=1
    # print(arr)
    # print(arr[::-1])

print(cnt)