def sqr(number): #defining a function 'def function name()'
	number = number ** 2
	return number

num = input("enter a number: ")	#input a number Caution: for string use "raw_input"
print "you entered : %d" % num
#print type(num)	prints the type of the input
t = sqr(num)	#function call
print t
