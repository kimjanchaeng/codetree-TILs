N, K= list(map(int,input().split()))
block=[]
for i in range(N):
    block.append(0)

for i in range(K):
    A, B=list(map(int,input().split()))
    for j in range(A-1,B):
        block[j]=block[j]+1

# print(block)
print(max(block))