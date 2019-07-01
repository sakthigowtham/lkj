N=int(input())
m=list(map(int,input().split()))
H=[]
for i in m:
    if m.count(i)>1:
        H.append(i)
        break;
if len(H)==0:
    print("unique")
else:
    print(*h)
