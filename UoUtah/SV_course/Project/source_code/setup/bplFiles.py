#!/usr/bin/python
import sys, os, time, re, glob2
from subprocess import Popen, PIPE, check_output, CalledProcessError
from multiprocessing import Pool

class bplFiles():
	def __init__(self,cmd,unr):
		self.cmd = cmd
		self.unr = unr

	def running(self, j):
		for i in range(j,len(self.unr),10):
			tmp = self.unr[i]
			while '/' in tmp:
				tmp = tmp[tmp.find('/')+1:]
			cmd2 = self.cmd + [self.unr[i], '-bpl', tmp[:-2] + '.bpl']
	
			i = Popen(cmd2,stdout = PIPE, stderr = PIPE)
			out, err = i.communicate()
			print "filename = {0}, thread = {1}".format(tmp,j)

