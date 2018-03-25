def str_correction(var,e=0):
    c=0
    final="r"
   # for i in range (0,len(var)):
    #   if var[i]==" "
     #  c+=1
    

    for i in range (c,len(var)):
        if final[-1]==".":
            final+=" "
        if var[i] ==" ":
            if final[-1]==" ":
                pass
            else:
                final+=var[i]
        else:
            final+=var[i]
        
        
        # w= var.find('.',e,len(var))
   # if w > -1 :
    #    # var[w+1]=" "
     #   print(w)
      #  print(var[w+1]) 
       # str_correction(var,w+1)

    if final[1]!=" ":
        return final[1:]
    else:
        return final[2:]



z= str_correction("    my . lkl       gdj .sdf.ssfd")
print(z[-1])
print (z)
