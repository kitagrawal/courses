import sys, os
#-------------------------------------------------------------------------------
if len(sys.argv) == 4:
	n = int(sys.argv[1])
	cnfFile = sys.argv[2]
	outputFile = sys.argv[3]

file1 = open(cnfFile,'w+')
file2 = open("satSolverResults.txt",'w+')
file3 = open(outputFile,"w+")

#no. of constraints
row_sum = 0;
for i in range(1,n):
	row_sum += i
ne_sum = row_sum;
for i in range(1,n):
	t = n-i; tmp_sum = 0;
	for j in range(1,t):
		tmp_sum += j
	ne_sum += 2*tmp_sum

#formatting the cnf file
string = "p cnf"+" "+ str(n*n) + " " + str(2*5*row_sum + 2*ne_sum) +  "\n"
file1.write(string)

#create the board, assign the variable names
count = 0; board = [0]*n
for  i in range(n):
    tmp = []
    for j in range(n):
        count += 1
        tmp.append(str(count))
    tmp.append("0\n")
    board[i] = tmp
    file1.write(' '.join(board[i]))

#row constraint
for i in range(n):
    for j in range(n):
        for k in range(j+1,n):
            string = "-"+str(board[i][j])
            string += " -"+str(board[i][k])+" 0\n"
            file1.write(string)

#column constraint
for j in range(n):
	for i in range(n):
		for k in range(i+1,n):
			string = "-"+str(board[i][j])
			string += " -"+str(board[k][j])+" 0\n"
			file1.write(string)

#1. NE ->SW - column constraint
d1 = {};
for i in range(n):
    for j in range(n):
        k = 1
        while (i+k)<n and (j+k)<n:
            num = board[i+k][j+k]
            if board[i][j] in d1:
                d1[board[i][j]].append(str(num))
            else:
                d1[board[i][j]] = [num]
            string = "-"+str(board[i][j])+" -"+str(num)+" 0\n"
            k += 1
            file1.write(string)

#2. NW -> SE - diagonal constraint
d1 = {};
for i in range(n):
    for j in range(n-1,0,-1):
        k = 1
        while (i+k)<n and (j-k)>=0:
            num = board[i+k][j-k]
            if board[i][j] in d1:
                d1[board[i][j]].append(str(num))
            else:
                d1[board[i][j]] = [num]
            string = "-"+str(board[i][j])+" -"+str(num)+" 0\n"
            k += 1
            file1.write(string)

file1.close()

#------------------------------------------------------------------------------
#single execution
exe = "minisat "+cnfFile+" "+"satSolverResults.txt"
os.system(exe)

#exe2 = "cat "+outputFile
#os.system(exe2)

#--------------------------------------------------------------------------------
#finding all possible outputs
#file2 = open(outputFile,"a+")
#line = file2.readline()
with open("satSolverResults.txt","a+") as file2:
	j = 0; k =0;
	target = file2.readlines()
	line = target[j]
	if target[j] == "UNSAT\n": file3.write("No Solution");
	else:
		while line != "":
			if line == "SAT\n":
				k = j + 1;
				tmp = target[k]
				tmp = tmp.strip().split(' ')
				tmp = map(int,tmp)
				for i in range(0,len(tmp)-1,n):
					tempo = tmp[i:i+n]
					print tempo
					for i in range(len(tempo)):
						if tempo[i] > 0: tempo[i] = 'X';
						else: tempo[i] = '.';
					file3.write(''.join(tempo)+'\n')
				file3.write('\n\n')
				tmp = map(lambda i: -1 * i, tmp)
				file1 = open(cnfFile,"a+")
				file1.write(' '.join(map(str,tmp))+"\n")
				file1.close()
				temp = "temp.txt"
				t = open(temp,'w')
				exe = "minisat "+cnfFile+" "+temp
				os.system(exe)
				for line in open(temp):
					file2.write(line)
				file2.seek(0)
				target = file2.readlines()
				j += 2
				line = target[j]
			else:
				os.remove('temp.txt')
				os.remove("satSolverResults.txt")
				file2.close()
				break
