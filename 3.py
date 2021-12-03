import numpy as np 


list = []
with open('3.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip("\n")
        list.append(line)

print(list)


matri = np.zeros( (1000, 12))

       
#matrix first row gets replaced
def ro(lst,j):
    for i in range(1000):
            matri[i][j] = lst[i][j]
    
def finalMatrix(list=list):
    
    for i in range(12):
        ro(list,i)
    
finalMatrix()



def calc(z):
    zero = 0
    ones = 0
    for num in z:
        if num == 0:
            zero = zero + 1
        elif num == 1:
            ones = ones + 1
    if zero > ones:
        print(0)
    else:
        print(1)


def Part1(l):
    answer = []
    for i in range(12):
        answer.append(calc(matri[:,i]))
    return answer


Part1(matri)
# print(matri[:,0])