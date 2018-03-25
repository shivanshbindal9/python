r=int(input("enter a no."))
a_list=[0,1]

[a_list.append(a_list[x-2]+a_list[x-1]) for x in range(2,r)]

print(a_list)
