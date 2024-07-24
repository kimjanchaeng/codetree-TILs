N=int(input())
s=input()
seat=[int(i) for i in s]
# print(seat)

def max_seat():
    av_seat=[]
    for i,elem in enumerate(seat):
        if elem==1:
            av_seat.append(i)

    s=len(av_seat)
    ans=N
    for j in range(s-1):
        dis=abs(av_seat[j]-av_seat[j+1])
        ans=min(ans,dis)
    
    return ans



ans1=0
for i in range(N):
    for j in range(i+1,N):
        if seat[i]!=1 and seat[j]!=1:
            seat[i],seat[j]=1,1
            ans1=max(ans1,max_seat())
            
            seat[i],seat[j]=0,0

print(ans1)