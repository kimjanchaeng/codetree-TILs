N=int(input())
arr=[]
for i in range(N):
    arr.append(int(input()))

# print(arr)
st=[]
for i in range(N):
    dist=0
    for j in range(N):
        dist+=arr[(i+j)%N]*j
    st.append(dist)
# print(st)
print(min(st))