file = open('day-28\day-28.txt','r')
n=int(input('Wich day do u wnat to? : '))
cont=file.readlines()

print('Day ' + str(n) +', '+str(cont[n-1])[:-1]+' pull ups')

file.close
