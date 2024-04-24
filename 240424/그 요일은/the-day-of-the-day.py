m1, d1, m2, d2 = list(map(int,input().split()))
day=input()

days=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
dates=[0,31,29,31,30,31,30,31,31,30,31,30,31]

s=days.index(day)    #find는 list형태 안됨

day1=sum(dates[:m1])+d1
day2=sum(dates[:m2])+d2

count=1

d=day2-day1
count+=d//7
if d&7>=s:
    count+=1
print(count)