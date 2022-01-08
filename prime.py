# first 10 prime numbers


# prime number - it will be only divisible by one and that number



x=int(input("enter the number")) # Explicit Conversion


# % operator used for finding the remainder

i=2
f=1

if(x==1):
    print("The Number is Nither Prime Nor Composite")

else :

    while(i<x) :
        
        if(x%i==0):
            print("The number is  Not prime")
            f=0
            break

        i=i+1




    if(f==1):
        print("The number is Prime")


