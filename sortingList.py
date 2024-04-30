l1=[41,2,12,6,35,8,10,1,19]
n=len(l1)
for i in range(n):
    for j in range(i+1,n):
        if l1[i]>l1[j]:
            l1[i],l1[j]=l1[j],l1[i]
        else:
            l1[i], l1[j] = l1[i], l1[j]

print(l1)