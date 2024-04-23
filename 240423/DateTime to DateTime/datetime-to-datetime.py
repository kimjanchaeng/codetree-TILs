a, b, c = list(map(int,input().split()))

day1=11*24*60+11*60+11
day2=a*24*60+b*60+c

if day1>day2:
    print(-1)
else:
    print(day2-day1)