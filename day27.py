import os

finnal_couter_of_wolves =[]
myfile= open("test.txt","r")
lines = myfile.readlines()

for line in lines:
    line.split()
    counter=0
    for word in line:
        if word in 'aeiou':
            counter+=1
    finnal_couter_of_wolves.append(counter)

    i=0
for numbers in finnal_couter_of_wolves:
    print('line {} are {} wolves'.format(i+1,finnal_couter_of_wolves[i]))
    i+=1