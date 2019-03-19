#!/usr/bin/python
import sys, os, time, glob2
from subprocess import Popen, PIPE, check_output, CalledProcessError

class generate():
	def __init__(self,cmd,files):
		self.cmd = cmd
		self.files = files

	def running(self, j):
		f = open('output/ntav'+str(j)+'.txt', 'w')

		for i in range(j,len(self.files),4):
			cmd2 = self.cmd + [self.files[i]]

			p = Popen(cmd2, stdout=PIPE, stderr=PIPE)
			out, err = p.communicate()
			#print err	
			
			for line in err.splitlines():
				if (('found an error' in line) and ('false-unreach' in self.files[i])) or (('found no error' in line) and ('true-unreach' in self.files[i])):
					status = 'SAT'
					break
				elif (('found an error' in line) and ('true-unreach' in self.files[i])) or (('found no error' in line) and ('false-unreach' in self.files[i])):
					status = 'UNSAT'
					break
				elif ('timed out' in line):
					status = 'TIMEOUT'
					break
				else:
					status = 'EXCEPTION'

			print "status = {0}, process = {1}, filename = {2}".format(status,j, self.files[i])
			f.write(self.files[i]+' '+status+'\n')
			f.flush()
		f.close()

class create():
	def __init__(self, filenames, writeFile, pathname):
		self.filenames = filenames
		self.writeFile = pathname + writeFile

	def mergingFiles(self, ftype): #merge the several output files into 1 output file
		g = open(self.writeFile,'w')
		for i in range(len(self.filenames)):			
			with open(self.filenames[i],'r') as f:
				content = f.readlines()
			content = [x.strip() for x in content]
			for j in range(len(content)):
				g.write(content[j]+'\n')
			
		g.close()
		version = self.creating(ftype) #version of label outcome
		return version

	def creating(self,ft): #Creating Dict of output files
		d = {}
		with open(self.writeFile, 'r') as f:
			content = f.readlines()
		content = [x.strip() for x in content]
		for i in range(len(content)):
			tmp = content[i].split(' ')
			#print len(tmp[0]), tmp
			while '/' in tmp[0]: tmp[0] = tmp[0][tmp[0].find('/')+1:];
			if len(tmp) == 2:
				if tmp[0] not in d: d[tmp[0]] = self.assignment(tmp[1],ft);
		
		return d

	def assignment(self, status, ft):
		if ft == 0:
			k = [0]
			k.append(self.labelAssign(status))
		elif ft == 1:
			k = [1]
			k.append(self.labelAssign(status))
		return k
	
	def labelAssign(self, status):
		if status == 'SAT': return 0;
		elif status == 'UNSAT': return 1;
		elif status == "TIMEOUT": return 2;
		elif status == "EXCEPTION": return 3;

class merge():
	def __init__(self):
		pass

	def compareOutputs(self, d1, d2): #compare output to create final labels
		f = ('output/finalLabels.txt','w')
		for item in d1:
			if item in d2:
				if 'true-unreach' in item:
					if d1[item] == 'SAT' and d2[item] != 'SAT': f.write(item +' '+ d1[item])
					elif d2[item] == 'SAT' and d1[item] != 'SAT': f.write(item +' '+ d2[item])
					elif d1[item] == d2[item]: f.write(item +' '+ d1[item])
					#penalizing EXCEPTION More than TIMEOUT
					elif d1[item] == 'EXCEPTION' and d2[item] == 'TIMEOUT': f.write(item +' '+ d2[item])
					elif d1[item] == 'TIMEOUT' and d2[item] == 'EXCEPTION': f.write(item +' '+ d1[item])
				if 'false-unreach' in item:
					if d1[item] == 'UNSAT' and d2[item] != 'UNSAT': f.write(item +' '+ d1[item])
					elif d2[item] == 'UNSAT' and d1[item] != 'UNSAT': f.write(item +' '+ d2[item])
					elif d1[item] == d2[item]: f.write(item +' '+ d1[item])
					elif d1[item] == 'EXCEPTION' and d2[item] == 'TIMEOUT': f.write(item +' '+ d2[item])
					elif d1[item] == 'TIMEOUT' and d2[item] == 'EXCEPTION': f.write(item +' '+ d1[item])

