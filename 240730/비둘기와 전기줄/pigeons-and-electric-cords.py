N=int(input())

change=[0]*11
state=[3]*11

for i in range(N):
    num,loc=list(map(int,input().split()))
    if state[num]!=loc and state[num]!=3:
        change[num]+=1
    state[num]=loc

print(change.index(max(change)))