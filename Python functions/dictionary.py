#CREATING DICTIONARY
phone_book = {'ankit' : 8013008341, 'mahendra' : 9011015851, 'komal' : 8421624588, 'mohit' : 9028608363}	#key:value pairs
#------------------------------------------------------------------------------------------------------------------------
#ACCESSING
print phone_book['ankit'], phone_book['mohit']	#access by key
#------------------------------------------------------------------------------------------------------------------------
#INSERTING and DELETING
print phone_book
phone_book['nivedita'] = 9860217983	#appends at the beginning Note: In list, it appends at the end of the list
print phone_book
#print len(phone_book)	#length of the dictionary
del phone_book['nivedita']	#deleting an entry
print phone_book
#-------------------------------------------------------------------------------------------------------------------------
#CHANGING VALUE OF THE KEY
phone_book['ankit'] = 9158266126
print phone_book


