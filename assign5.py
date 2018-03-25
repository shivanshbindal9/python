
pyList = ['mix', 'xyz', 'apple', 'xanadu', 'aardvarrk']
c=0
for x in range(0,len(pyList)):

    if(pyList[x][0]=='x'):
        d=pyList[c]
        pyList[c]=pyList[x]
        pyList[x]=d
        c+=1
    
y=sorted(pyList[:c])

z=sorted(pyList[c:])

print(y+z)

#print(sorted(pyList[:3]))
    
#print (pyList[2][2])

