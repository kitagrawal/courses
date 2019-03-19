

class operations():
	def __init__(self, dictf1, dictl1, dictl2, writeFile, pathname):
		self.dict1 = dictf1
		self.dict2 = dictl1
		self.dict3 = dictl2
		self.outFile = writeFile
		self.path = pathname
	
	#merging the features with the appropriate labels and flag code
	def create(self):
		tmp1 = {}; tmp2 = {};
		print len(self.dict1), len(self.dict2), len(self.dict3)
		for item in self.dict1:
			#print "item = ",item
			itemshort = item[:-4] + '.c'
			#print "itemShort = ",itemshort
			if itemshort in self.dict3:
				tmp1[item] = self.dict1[item] + self.dict3[itemshort]

			if itemshort in self.dict2:
				tmp2[item] = self.dict1[item] + self.dict2[itemshort]
		print len(tmp1), len(tmp2)
		self.merge(tmp1, tmp2)

	#writing the obtained matrix rows to a file
	def merge(self, d1, d2):
		f = open(self.path + self.outFile,'w'); count = 0;
		for item in d1:
			if item in d2:
				tmp1 = item; tmp2 = item;
				count += 1
				for i in range(len(d1[item])): tmp1 += ',' + str(d1[item][i]);
				for i in range(len(d2[item])): tmp2 += ',' + str(d2[item][i]);
				f.write(tmp1+'\n')
				f.write(tmp2+'\n')
		#print count

		f.close()
