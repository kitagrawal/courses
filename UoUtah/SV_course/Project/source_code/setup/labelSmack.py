import sys, os, time, glob2
from subprocess import Popen, PIPE, check_output, CalledProcessError
from multiprocessing import Pool

def running(j):
	f = open('output/tav'+str(j)+'.txt', 'w')

	for i in range(j,len(files),15):
		cmd2 = cmd + [files[i]]

		p = Popen(cmd2, stdout=PIPE, stderr=PIPE)
		out, err = p.communicate()
		print err	
			
		for line in err.splitlines():
			if (('found an error' in line) and ('false-unreach' in files[i])) or (('found no error' in line) and ('true-unreach' in files[i])):
				status = 'SAT'
				break
			elif (('found an error' in line) and ('true-unreach' in files[i])) or (('found no error' in line) and ('false-unreach' in files[i])):
				status = 'UNSAT'
				break
			elif ('timed out' in line):
				status = 'TIMEOUT'
				break
			else:
				status = 'EXCEPTION'

		print "status = {0}, process = {1}, filename = {2}".format(status,j, files[i])
		f.write(files[i]+' '+status+'\n')
		f.flush()
	f.close()

if __name__ == '__main__':
	benchPath = '/proj/SMACK/sv-benchmarks/**'
	cmd = ['/mnt/local/smack-project/smack/bin/smack', '-x=svcomp','--verifier=svcomp', '--clang-options=-m64']
	tunr = glob2.glob(benchPath + '/*true-unreach*.c')
	funr = glob2.glob(benchPath + '/*false-unreach*.c')

	files = tunr + funr
	pool = Pool(20)
	#running(0)
	pool.map(running, range(15))
