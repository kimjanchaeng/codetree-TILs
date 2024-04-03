# binary = [1, 1, 1, 0, 1]
# binary=list(map(int,input().split()))     #
binary = list(map(int, list(input())))
num = 0

for i in binary:
    num = num * 2 + i

print(num)