from math import *
total = 0
n = 6
for i in range(7):
	total = total + (factorial(n)/(factorial(n-i)*factorial(i)))

total_power = pow(2,n)

if total == total_power:
	print "true"
else:
	print "false"
