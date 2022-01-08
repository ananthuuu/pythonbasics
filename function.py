
def isprime(a):
    x=a

    



    i=2
    f=1

    if(x==1):
        return "no"

    else :

        while(i<x) :
            
            if(x%i==0):
                print("The number is  Not prime")
                f=0
                break

            i=i+1




        if(f==1):
            print("The number is Prime")



















x=input("Please Enter your Number")

print(isprime(x))


