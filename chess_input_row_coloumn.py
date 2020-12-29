m=1
x=int(input("write row number"))
y=int(input("write coloumn number"))
while m<=x:
    n=1
    while n<=y:
        if n>0 and n<=y and n % 2==0 and m%2==0 or n>0 and n<=y and n%2>0 and m%2>0:
            print(" * ",end="")
        else:
            print(" # ",end="")

        # if n>0 and n<=8 and n % 2>0 or n>8 and n<=17 and n%2==0:
        #     print(" # ",end="")
        if n % y==0:
            print()
        n=n+1
    
    m+=1

