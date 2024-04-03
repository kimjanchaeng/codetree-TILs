m1,d1,m2,d2=map(int,input().split())
day=[0,31,28,31,30,31,30,31,31,30,31,30,31]
date=['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
# date1=date.sort(reverse=True)
# date1=date.reverse()   #이렇게 하면 원본이 바뀌잖아 list(reversed(date)) or date[::-1]
date1=list(reversed(date))
time1=sum(day[m1:])+d1
time2=sum(day[m2:])+d2
d=time2-time1
if d>0:
    print(date[(d)%7+1])
else:
    print(date[-((-d)%7)+1])