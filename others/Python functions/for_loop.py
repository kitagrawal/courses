#CREATING AND PRINTING IN LISTS
names = ["Adam","Alex","Mariah","Martine","Columbus"]	#for variable_name(any) in list_name
for x in names:
    print x
#--------------------------------------------------------------------------------------------------------
#CREATING AND PRINTING IN DICTIONARY
webster = {
	"Aardvark" : "A star of a popular children's cartoon show.",
    "Baa" : "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}

# Add your code below!
for key in webster:
    print webster[key]
#-----------------------------------------------------------------------------------------------------------
#FUNCTIONS + LIST
# Write your function below!
def fizz_count(x):		#functions can have lists as arguments
    count = 0
    for item in x:
        if item == "fizz":
            count += 1
    return count

y = ["fizz","cat","fizz"]
k = fizz_count(y)
print k
#-------------------------------------------------------------------------------------------------------------
#STRINGS
for letter in "Codecademy":
    print letter
    
# Empty lines to make the output pretty
print
print

word = "Programming is fun!"

for letter in word:
    # Only print out the letter i
    if letter == "i":
        print letter
#---------------------------------------------------------------------------------------------------------------
#DICTIONARIES WHEN KEY IN 2/MORE DICTIONARIES ARE SAME	#A PROJECT: DAY AT A SUPEMARKET
prices = {"banana":4, "apple":2, "orange":1.5, "pear":3}
stock = {"banana":6, "apple":0, "orange":32, "pear":15}
shopping_list = ["banana", "orange", "apple"]
for key in prices:
    print key
    print "price: %s" % prices[key]
    print "stock: %s" % stock[key]

"""total = 0
for key in prices:
    print prices[key] * stock[key]
    total = total + (prices[key] * stock[key])
    
print total"""

def compute_bill(food):
    total = 0
for item in food:
        if stock[item] > 0:
	        total = total + prices[item]
	        stock[item] -= 1
return total

#--------------------------------------------------------------------------------------------------------------------------
#FOR/ELSE
animals = ['lion', 'tiger', 'bird', 'banana', 'crab', 'shark']

for a in animals:
    if a == 'banana':
        print "banana is not an animal. It is a fruit!"
        break
    print a
else:
    print "Build your own zoo"
