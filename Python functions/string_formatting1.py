#creating strings and concatenation
var1 = "Anand Sanghi is "
var2 = str(2)
var3 = ' good'
print var1 + var2 + var3
#---------------------------------------------------------------
#string formatting using %
string_1 = "my name is "
string_2 = "Ankit Agrawal"

print "%s%s"%(string_1,string_2)
#--------------------------------------------------------------
#taking raw input from user for creating strings using %
#remove the below comment (""") to see the results
"""name = raw_input("what is your name? ")
subject = raw_input("what is your subject? ")
color = raw_input("what is your favourite color? ")

print "Ahh your name is %s, you study %s "\
"and your favourite color is %s" %(name,subject,color)
"""
#--------------------------------------------------------------
#combining some string techniques

#assigning string to a variable"
random_string = "xyzabc" 
#printing length of string stored in the variable
print len(random_string) 
#other method is
"""print len("string_name or text")"""
#converting the string to upper and lower cases
print random_string.upper() #upper case
print random_string.lower() #lower case
#other method is
"""print "any_string".upper()
print "any_string".lower()"""


