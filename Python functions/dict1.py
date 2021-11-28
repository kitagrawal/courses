inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}
print inventory
# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']
print inventory
# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 
print inventory
# Your code here
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].remove('dagger')
inventory['backpack'].sort()
inventory['gold'] = inventory['gold'] + 50
print inventory
