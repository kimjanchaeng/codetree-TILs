a, b = list(map(int,input().split()))
n=input()

num=0
for i in n:
    num=num*a+int(i)

digits=[]
while True:
    if num<b:
        digits.append(num)
        break

    digits.append(num%b)
    num//=b

for i in digits[::-1]:
    print(i,end='')