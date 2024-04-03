# binary = [1, 1, 1, 0, 1]
binary=map(int,input().split())
num = 0

for i in range(5):
    num = num * 2 + binary[i]

print(num)