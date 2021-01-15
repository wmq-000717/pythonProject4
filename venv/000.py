x=input().split()
x.sort()
D={}
for v in x:
    if v in D:
        D[v]=D[v]+1
    else:
        D[v]=1
for k in D:
    print(k+":"+str(D[k]))
print('你这是专业版')