N, B = list(map(int,input().split()))

digits=[]
while True:
    if N<B:
        digits.append(N)
        break
    
    digits.append(N%B)
    N//=B

for i in digits[::-1]:
    print(i,end='')