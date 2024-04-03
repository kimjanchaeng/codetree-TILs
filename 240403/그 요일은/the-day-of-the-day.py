m1,d1,m2,d2=map(int,input().split())
day=input()

date=[0,31,29,31,30,31,30,31,31,30,31,30,31]
date1=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
time1=sum(date[:m1])+d1
time2=sum(date[:m2])+d2

d=time2-time1
d1=date1.index(day)

answer=d//7
answer1=d%7
if answer1>=d1:
    answer+=1
print(answer)