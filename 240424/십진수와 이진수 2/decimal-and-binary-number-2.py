n=input()

num=0
for i in n:
    num=num*2+int(i)
num*=17

digits=[]
while True:
    if num<2:
        digits.append(num)
        break

    digits.append(num%2)
    num//=2

for i in digits[::-1]:
    print(i,end='')