def primeno(z):
    d=[]
    for r in range (2,z+1):
             
        c=0
        for x in range(2,r):
            if(r%x==0):
               c+=1
        if (c==0):
            print (" It is a prime no.",r)
            d.append(r)
    print (d)


y=int(input("enter a no."))

primeno(y)


