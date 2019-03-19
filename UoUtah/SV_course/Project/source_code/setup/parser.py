import sys, os
import glob2


class features():
	def __init__(self, files,output):
		self.allFiles = files
		self.outputFile = output

	#extracting features from .bpl files
	def extract(self):
		g = open(self.outputFile, 'w')
		for i in range(len(self.allFiles)):
			d = {}
			with open(self.allFiles[i],'r') as f: 
				fileRead = f.readlines()
			fileRead = [x.strip() for x in fileRead]
			#implementing the declaration type [type, const, function, axiom, var, procedure]
			for j in range(len(fileRead)):
				##counting imperative constructs <variable types, functions, procedure & implementation declarations
				#counting implementation declarations
				if 'implementation' in fileRead[j]:
					if 'implement_dec' not in d: d['implement_dec'] = 1;
					else: d['implement_dec'] += 1;

				#counting variable types <constants, global>
				if 'var' in fileRead[j]:
					if 'global_var' not in d: d['global_var'] = 1;
					else: d['global_var'] += 1;
				if 'const' in fileRead[j]:
					if 'const_var' not in d: d['const_var'] = 1;
					else: d['const_var'] += 1;
				if 'type' in fileRead[j]:
					if 'type_dec' not in d: d['type_dec'] = 1;
					else: d['type_dec'] += 1;
				if 'function' in fileRead[j]:
					if 'func_dec' not in d: d['func_dec'] = 1;
					else: d['func_dec'] += 1;
			
			#writing the output to the File
			tmp = self.allFiles[i]
			while '/' in tmp: tmp = tmp[tmp.find('/')+1:];
		    	for name, value in d.items():
				tmp += ' ' + str(value)
			g.write(tmp+'\n')
		g.close()

	#creating the dictionary {filename:[<features>]}
	def create(self, d = {}):
		with open(self.outputFile,'r') as f:
			content = f.readlines()
		content = [x.strip() for x in content]

		for i in range(len(content)):
			tmp = content[i].split(' ')
			if tmp[0] not in d: d[tmp[0]] = tmp[1:];
		return d
