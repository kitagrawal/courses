import sys, os, glob2
from subprocess import PIPE, Popen, check_output
from multiprocessing import Pool

def f(j):
	for i in range(j,len(filename),20):
		tmp = filename[i]
		while '/' in tmp:
			tmp = tmp[tmp.index('/')+1:]
		tmp = tmp[:-1]+'bpl'
		#print tmp
		cmd2 = cmd + ['--bpl-file', tmp, filename[i]]
		io = Popen(cmd2,stdout=PIPE, stderr=PIPE)
		out,err = io.communicate()
		
		#count += 1
		print "bplfile = {0}, pool = {1}".format(tmp,j)


if __name__ == "__main__":
	cmd = ['/mnt/local/smack-project/smack/bin/smack','-x=svcomp','--time-limit','3','--unroll','16']
	pathname = '/proj/SMACK/sv-benchmarks/**'
	tunr = glob2.glob(pathname+'/*true-unreach*.c')
	funr = glob2.glob(pathname+'/*false-unreach*.c')
	filename = tunr + funr
	print len(tunr), len(funr), len(filename)
	pool = Pool(20)
	#args = [0,1,2,3,4,5,6,7,8,9]
	pool.map(f,range(20))
	#map(f,args)
