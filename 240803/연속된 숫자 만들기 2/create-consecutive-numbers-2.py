arr=list(map(int,input().split()))

# arr=[4,7,9]
# arr=[5,6,10]
cnt1=0
cnt2=0
cnt3=0
for i in range(2):
    diff=abs(arr[i]-arr[i+1])
    if diff==1:
        cnt1+=1
    elif diff==2:
        cnt2+=1
    else:
        cnt3+=1

if cnt1==2:
    print(0)
elif cnt2>0:
    print(1)
else:
    print(2)