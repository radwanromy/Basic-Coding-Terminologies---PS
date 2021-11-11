[n,m] = list(map(int,input().strip().split()))
alll=[]
p=int(1e9+7)
for _ in range(n):
    s = input().strip()
    alll.append(s)
target = input().strip()
req = []
no = []
for i in range(m):
    if target[i]=='1':
        req.append(i)
    else:
        no.append(i)
filtered = []
for st in alll:
    bo = 1
    for i in no:
        if st[i]=='1':
            bo = 0
            break
    if bo==1:
        filtered.append(st)
new = []
for i in req:
    for st in filtered:
        if st[i]=='0':
            new.append(i)
            break
w = len(new)
#print(req,filtered,new)
count = {i:0 for i in range(1,w+1)}
setcnt = {}
def subst(L):
    ans = [()]
    k = 1
    for itm in L:
        for j in range(k):
            ans.append(ans[j]+(itm,))
        k*=2
    return(ans[1:])


for st in filtered:
    temp = []
    for i in new:
        if st[i]=='0':
            temp.append(i)
    for sett in subst(temp):
        if sett in setcnt:
            setcnt[sett]+=1
        else:
            setcnt[sett]=1
            
#print(setcnt)

#-------------------------------------
for moo in subst(new):
    if moo in setcnt:
        count[len(moo)]+=pow(2,setcnt[moo],p)-1
        count[len(moo)]%=p
#for yt in range(100000000000000000000000000000000):
#    ko =0
#----------------------------
final = pow(2,len(filtered),p)-1
#print(count,final)
for i in range(1,w+1):
    final+=count[i]*pow(-1,i)
    final%=p

print(final)
                 