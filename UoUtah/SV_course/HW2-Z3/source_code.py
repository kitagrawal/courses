from z3 import *
import sys

OPS = {'g', '+', '*', '/', '-'}

def add_and_mul(n, operator, inputs, params):
    board1 = params[(inputs[0]*n)+(inputs[1]+1)-1]
    if operator == '+':
        for i in range(2,len(inputs),2):
	       board1 = board1 + params[(inputs[i]*n)+(inputs[i+1]+1)-1]
    elif operator == '*':
        for i in range(2,len(inputs),2):
            board1 = board1 * params[(inputs[i]*n)+(inputs[i+1]+1)-1]
    return board1

def sub_and_div(n,operator,inputs,params):
    if operator == '-':
        board1 = params[(inputs[0]*n)+(inputs[1]+1)-1] - params[(inputs[2]*n)+(inputs[3]+1)-1]
        board2 = params[(inputs[2]*n)+(inputs[3]+1)-1] - params[(inputs[0]*n)+(inputs[1]+1)-1]
    elif operator == '/':
        board1 = params[(inputs[0]*n)+(inputs[1]+1)-1] / params[(inputs[2]*n)+(inputs[3]+1)-1]
        board2 = params[(inputs[2]*n)+(inputs[3]+1)-1] / params[(inputs[0]*n)+(inputs[1]+1)-1]
    return board1, board2

def solve_puzzle(n, puzzle):
    # Write your code for solving using z3 here
    for i in range(len(puzzle)):
        temp = puzzle[i][2:]; operator = puzzle[i][1];
        if operator == '+' or operator == '*':
            c = add_and_mul(n,operator, temp, params)
            s.add(c == puzzle[i][0])
        elif operator == '-' or operator == '/':
            a, b = sub_and_div(n,operator, temp, params)
            s.add(Or(a == puzzle[i][0], b == puzzle[i][0]))
        elif operator == 'g':
            p = params[(temp[0]*n)+(temp[1]+1)-1]
            s.add(p == puzzle[i][0])

    if str(s.check()) == 'sat':
        modelling = s.model()
        tmp = []
        for i in range(0,len(modelling)):
            tmp.append(modelling[params[i]])

        for j in range(0,len(tmp),n):
            k = tmp[j:j+n]
            k = map(str,k)
            print ' '.join(k)
    else:
        print "No Solution"

#----------------------------------------------------------
if len(sys.argv) == 1:
    n = 6
    puzzle=[[11, '+', 0, 0, 1, 0],
            [2,  '/', 0, 1, 0, 2],
            [3,  '-', 1, 1, 1, 2],
            [20, '*', 0, 3, 1, 3],
            [6,  '*', 0, 4, 0, 5, 1, 5, 2, 5],
            [3,  '/', 1, 4, 2, 4],
            [240,'*', 2, 0, 2, 1, 3, 0, 3, 1],
            [6,  '*', 2, 2, 2, 3],
            [6,  '*', 3, 2, 4, 2],
            [7,  '+', 3, 3, 4, 3, 4, 4],
            [30, '*', 3, 4, 3, 5],
            [6,  '*', 4, 0, 4, 1],
            [9,  '+', 4, 5, 5, 5],
            [8,  '+', 5, 0, 5, 1, 5, 2],
            [2,  '/', 5, 3, 5, 4]]
else:
    # haphazard data parsing
    # * doesn't check for correct format
    # grab data and get out
    with open(sys.argv[1], 'r') as f:
        puzzle = [line.strip() for line in f]
    # remove blank lines
    puzzle= filter(lambda x: x != "", puzzle)
    # get n
    n = int(puzzle[0])
    # split rest of the lines
    puzzle = map(lambda x: x.split(), puzzle[1:])
    # cast strings to ints, except for OPS
    for i in range(len(puzzle)):
        puzzle[i] = map(lambda item: item if item in OPS else int(item), puzzle[i])

count = 0; s = Solver(); params = [0]*(n*n)
for i in range(n*n):
    count += 1
    params[i] = Int('x'+str(count))
    #range constraints
    s.add(And(params[i] >= 1),(params[i] <= n))

#row constraints
for i in range(0,len(params),n):
    tmp = params[i:i+n]
    for j in range(len(tmp)-1):
        for k in range(j+1,len(tmp)):
            s.add(tmp[j] != tmp[k])

#column constraints
for i in range(0,n):
    for j in range(0,n):
        for k in range(j+1,n):
            s.add(params[i+n*j] != params[i+n*k])


#other puzzle based constraints
solve_puzzle(n, puzzle)
