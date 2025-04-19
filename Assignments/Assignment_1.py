first=0
second=1
n=int(input("enter the number for fobonacci series: "))
if n==1:
    print(first)
elif n==2:
    print(first)
    print(second)
else:
    print(first)
    print(second)
    for i in range(0,n-2):
        n=first+second
        first=second
        second=n
        print(n)
