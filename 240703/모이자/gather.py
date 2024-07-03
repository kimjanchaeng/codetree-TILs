import sys
import sys

INT_MAX = sys.maxsize
# INT_MIN
# int_max=sys.maxisze
# int_min=-sys.maxisze

n=int(input())
arr=list(map(int,input().split()))
dis=0

min_tot=INT_MAX
for i in range(n):
    tot_dis=0
    for j in range(n):
        dis=abs(i-j)
        tot_dis+=dis*arr[j]
    min_tot=min(min_tot,tot_dis)

print(min_tot)