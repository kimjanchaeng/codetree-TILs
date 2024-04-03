m1,d1,m2,d2=map(int,input().split())
day=[0,31,28,31,30,31,30,31,31,30,31,30,31]
date=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
# date1=date.sort(reverse=True)
# date1=date.reverse()   #이렇게 하면 원본이 바뀌잖아 list(reversed(date)) or date[::-1]
date1=list(reversed(date))
time1=sum(day[m1:])+d1
time2=sum(day[m2:])+d2

if time2-time1>0:
    print(date[(time2-time1)%7])
else:
    print(date1[(time1-time2)%7-1])