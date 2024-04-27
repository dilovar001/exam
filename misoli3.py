a=input().split()

b=int(input())

for i in range(b,len(a)-1):

    a[i]=a[i+1]

a.pop(len(a)-1)

for i in range(len(a)):

   print(a[i],end=' ')