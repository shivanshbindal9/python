x="there are {:d} types of people".format(10)
binary="binary"
do_not="don't"
y = "Those who know {0:s} those who {1:s}".format(binary,do_not)

print (x)
print (y)

print ("I said {}".format(x))
print ("I said {:s}".format(y))

hilarious = False
joke ="Isn't the joke funny ?! {}"

print(joke.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print (w+e)
