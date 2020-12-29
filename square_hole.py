m=1
x=int(input("write row number"))
y=int(input("write coloumn number"))
while m <= x:
    n=1
    while n <= y:
        if m==1 or m==x or n==1 or n==y:
            print("#",end="  ") 
        else:
            print(" ",end="  ")
        n=n+1
    print()
    m+=1
