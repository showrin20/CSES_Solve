n=int(input())
lst=[int(i) for i in input().split()]

print(int((n*(n+1)/2)-sum(lst)))
