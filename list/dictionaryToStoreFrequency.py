List=[7,6,3,4,5,5]
lset=set(l)
dic={}
for i in lset:
    dic[i]=0
# print(dic)
for i in l:
    dic[i]=dic[i]+1
print(dic)
for i in dic:
    if dic[i]==2:
        print(i)
