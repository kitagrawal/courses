import sys, os, time, re, glob2
from subprocess import Popen, PIPE, check_output, CalledProcessError
from multiprocessing import Pool

def running(j):
	for i in range(j,len(unr),10):
		tmp = unr[i]
		while '/' in tmp:
			tmp = tmp[tmp.find('/')+1:]
		cmd2 = cmd + [unr[i], '-bpl', tmp[:-2] + '.bpl']
	
		i = Popen(cmd2,stdout = PIPE, stderr = PIPE)
		out, err = i.communicate()
		print "filename = {0}, thread = {1}".format(tmp,j)


cmd = ['/mnt/local/smack-project/smack/bin/smack', '-x=svcomp','--time-limit','3', '--verifier-options', '/di']

pathname = '/proj/SMACK/sv-benchmarks/**'
cfilename = glob2.glob(pathname + '/*.c')
tunr = glob2.glob(pathname + '/*true-unreach*.c')
funr = glob2.glob(pathname + '/*false-unreach*.c')
unr = tunr + funr
print "number of c files = {0}".format(len(cfilename))
print len(tunr), len(funr), len(unr)
#print tunr
pool = Pool(10)
args = [0,1,2,3,4,5,6,7,8,9]
pool.map(running,args)
