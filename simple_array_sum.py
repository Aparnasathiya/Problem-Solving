from functools import reduce
n=int(input())
arr=list(map(int,input().split()[:n]))
sum=reduce(lambda a,b:a+b,arr)
print(sum)