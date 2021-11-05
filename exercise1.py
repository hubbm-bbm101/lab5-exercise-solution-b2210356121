N = int(input("N: "))
oddsum=0
evensum=0
for x in range(1,N+1):
    if(x%2!=0):
        oddsum += x
    else:
        evensum += x
print("sum of odd numbers:", oddsum, "average of even numbers:", evensum/N )
