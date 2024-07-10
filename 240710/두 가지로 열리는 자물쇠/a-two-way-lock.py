N=int(input())

arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))

# s1=[]
# s2=[]
# for j in range(3):
#     a1=[]
#     a2=[]
#     for i in range(1,N+1):
#         if abs(i-arr1[j])<=2 or (i+arr1[j])%N<=2:
#             a1.append(i)
    
#         if abs(i-arr2[j])<=2 or (i+arr2[j])%N<=2:
#             a2.append(i)
#     s1.append(a1)
#     s2.append(a2)

# print(s1)
# print(s2)
# for i in s1:
ans=1
digit=[i for i in range(1,N+1)]
# print(digit)
s1=[]
s2=[]
for j in range(3):
    a1=[]
    a2=[]
    for k in range(arr1[j]-3,arr1[j]+2):
        a1.append(digit[k])
    # s1.append(digit[arr1[j]-3:arr1[j]+2])
    for k in range(arr2[j]-3,arr2[j]+2):
        a2.append(digit[k])
    # s2.append(digit[arr2[j]-3:arr2[j]+2])
    # s1.append(a1)
    # s2.append(a2)
    cnt=0
    for l in range(5):
        if a1[l] in a2:
            cnt+=1
    ans=cnt*ans
# print(s1)
# print(s2)
# ans=1
# for i in range(3):
#     cnt=0
#     for j in range(5):
#         if s1[i][j] in s2[i]:
#             cnt+=1
#     ans=ans*cnt
print(250-ans)