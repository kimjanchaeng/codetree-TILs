n=int(input())
x,y=0,0

for i in range(n):
    dir,d=map(str,input().split())
    if dir=='W':
        x, y = x - int(d), y
    elif dir=='S':
        x, y = x , y - int(d)
    elif dir=='N':
        x, y = x , y + int(d) 
    else:
        x, y = x + int(d), y 

print(x,y)