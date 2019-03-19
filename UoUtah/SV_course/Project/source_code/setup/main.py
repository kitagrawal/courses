import sys, os, time, re, glob2
from subprocess import Popen, PIPE, check_output, CalledProcessError
from multiprocessing import Pool


import bplFiles
from labelling import create, merge, generate
from parser import features
from matrix import operations


if __name__ == "__main__":

	#----main Dec----
	benchtype = 'tav'
	pathname = '/home/ankit/SV_course/Project/source_code/setup/output/'
	benchPath = '/proj/SMACK/sv-benchmarks/**'	
	cmdBPL = ['/mnt/local/smack-project/smack/bin/smack', '-x=svcomp','--time-limit','3', '--verifier-options', '/di']
	cmd = ['/mnt/local/smack-project/smack/bin/smack', '-x=svcomp','--verifier=svcomp', '--clang-options=-m64']
	'''
	tunr = glob2.glob(benchPath + '/*true-unreach*.c')
	funr = glob2.glob(benchPath + '/*false-unreach*.c')
	unr = tunr + funr

	#----Generating .bpl files----
	a1 = bplfiles(cmdBPL,unr)
	pool = Pool(10)
	pool.map(a1.running,range(10))
	'''
	#----Generating Features----
	bplPath = '/home/ankit/SV_course/Project/source_code/setup/output/bpl'
	bplFiles = glob2.glob(bplPath + '/*.bpl')
	print len(bplFiles)
	filename = benchtype + 'Feature.txt'
	
	c1 = features(bplFiles,filename)
	c1.extract()	
	features = c1.create()

	'''
	#----Generating labels----
	c2 = generate(cmd,unr)
	pool1 = Pool(10)
	pool2.map(c2.running, range(10))
	'''
	#----Finalizing Labels----
	filesNTAV = glob2.glob(pathname+'n'+benchtype+'*.txt')
	filesTAV = glob2.glob(pathname+benchtype+'*.txt')

	v1 = create(filesNTAV,'N'+benchtype+'.txt',pathname)
	v2 = create(filesTAV,benchtype+'.txt',pathname)
	dict1 = v1.mergingFiles(0)	#contains [<benchtype> = 0, status]
	dict2 = v2.mergingFiles(1)	#contains [<benchtype> = 1, status]

	#----creating the matrix---
	c2 = operations(features, dict1, dict2, 'matrix.txt', pathname)
	c2.create()
	
