n=int(input())
list1=[n]
while n!=1:
    if n%2!=0:
        n=n*3+1
        list1.append(n)
    else:
        n=n/2
        list1.append(n)
for i in list1:
    print(int(i),end=" ")
 
 
 
