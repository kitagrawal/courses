animals = ["bat","cat","dog"]	#creating list
#----------------------------------------------------------------------------------------------------------------------------------
#APPENDING AND INDEXING TO THE LIST
print animals[2]	#accesing list by index
animals.append("tiger")	#adding "tiger to the list (appending at the end)
print animals
print animals.index("dog")	#printing the index of the animal
dog_index = animals.index("dog")
#------------------------------------------------------------------------------------------------------------------------------------
#INSERTING AND REPLACING IN A LIST
animals.insert(dog_index,"pig")	#inserting "pig" at the index for dog Note: Dog doesn't get replaced but shifts by 1 place to the right
print animals
print animals.index("dog")
animals[0] = "lion"	#instead of inserting, it replaces the animal name at that index
print animals
#---------------------------------------------------------------------------------------------------------------------------------
# SLICING OF THE LISTS
first = animals[:2]	#first contains the animals with index 0,1
second = animals[2:4]	#second contains the animals with index 2,3
third = animals[4:]	#third contains the animals with index 4 till end of the list
print first, second, third
#----------------------------------------------------------------------------------------------------------------------------------
#SORTING A LIST
animals.sort()		#list_name.sort() will sort the list
print animals
#--------------------------------------------------------------------------------------------------------------------------------------
#DELETING
animals.remove("lion")	#list_name.remove(attribute)
#animals.pop(4)		list_name.pop(index_number)
#del[animals(4)]	del[list_name(index_number)]
print animals
#--------------------------------------------------------------------------------------------------------------------------------------
#LIST OF LISTS - RANGE AND FOR LOOP
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here
def flatten(lists):
    results = []
    for numbers in lists:
        for i in range(len(numbers)):
            results.append(numbers[i])
    
    return results

print flatten(n)
