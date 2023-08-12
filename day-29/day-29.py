# file= open('day-29\day-29.txt')
# print('Rading Content')
# print(file.read())
# print('Done')
# file.close()

# print('______________________________')
# print('')
# file= open('day-29\day-29.txt', 'w')
# file.write('GOA Is Moore Than Learn')
# file.close()
# file=open('day-29\day-29.txt', 'r')
# file.close()
# print('Reading Contents')
# print(file.read())
# print('Done')


# names=['Davit', 'Gio', 'Saloshen']

# file = open('day-29\day-29.txt','w+')

# for name in names:
#     file.write(name+'\n')

# file=open('day-29\day-29.txt','r')
# print(file.read())
def chelsi(mxedari):
    for item in range(1,4,2):
        if item == 3:
            break
        else:
            print(item)
        return item
print(chelsi([3,7,34,[5,2,4,6],'ocdaoci']))
