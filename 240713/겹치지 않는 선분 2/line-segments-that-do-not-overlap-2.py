N=int(input())

arr=[list(map(int,input().split())) for i in range(N)]
arr.sort()
# print(arr)
cnt=0
a=[]
# print(arr)
for i in range(1,N):
    if arr[i-1][0]<arr[i][0] and arr[i-1][1] >= arr[i][1]:
        # cnt+=1
        # print(1)
        if i not in a:
            a.append(i)
        if i-1 not in a:
            a.append(i-1)
# print(a)
print(len(arr)-len(a))