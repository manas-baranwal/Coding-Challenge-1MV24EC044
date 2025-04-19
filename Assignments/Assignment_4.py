n=int(input("enter number: "))
i=0
while i<n:
    j=0
    while (j<n-i-1):
        print(" ",end="")
        j+=1
    k=0
    while k<2*i+1:
        print("*",end="")
        k+=1
    print()
    i+=1
