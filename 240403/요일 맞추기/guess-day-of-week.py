m1,d1,m2,d2=map(int,input().split())
day=[0,31,28,31,30,31,30,31,31,30,31,30,31]
date=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
# date1=date.sort(reverse=True)
date1=date.reverse()
time1=sum(day[m1:])+d1
time2=sum(day[m2:])+d2

if time2-time1>0:
    print(date[(time2-time1)%7-1])
else:
    print(date[(time1-time2)%7-1])