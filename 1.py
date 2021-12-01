
list1 = []
with open('1.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        list1.append(int(line))

print(list1)


def tt(list):
    counter = 0
    for i in range(len(list)-1):
        if list[i] < list[i+1]:
            counter = counter + 1 
    return counter


def ff(x):
    counter=0
    for i in range(3,len(x)):
        if (sum(x[i-2:i+1])-sum(x[i-3:i])) > 0:
            counter+=1
    print(counter)
    

   
    
       
ff(list1)
        
    

