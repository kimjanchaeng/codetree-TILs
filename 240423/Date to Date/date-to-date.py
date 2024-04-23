m1, m2, d1, d2= list(map(int,input().split()))

num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

a=sum(num_of_days[:m1+1])+m2
b=sum(num_of_days[:d1+1])+d2
print(max(a,b)-min(a,b))