m1, d1, m2, d2 = list(map(int,input().split()))
days=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

dates=[0,31,28,31,30,31,30,31,31,30,31,30,31]

day1=sum(dates[:m1])+d1
day2=sum(dates[:m2])+d2
d=day2-day1
# if d<0:
#     print(days[(d)%7])
# else:
#     print(days[d%7])

print(days[d%7])