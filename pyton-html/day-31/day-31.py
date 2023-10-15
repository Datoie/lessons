# file = open('day-31\day-31.txt','r')
# for i in file:
#     if '\n' in i:
#         print(i[0]+str(len(i)-1))
#     else:
#         print(i[0]+str(len(i)))
# file.close()

# file = open('day-31\day-31.txt','r')
# arr=[]
# for i in file:
#     if '\n' in i:
#         arr.append(i[0]+str(len(i)-1))
#     else:
#         arr.append(i[0]+str(len(i)))
# for char in arr:
#     print(char)
# file.close()

# dic={'davit':19,'gio':26,'sali':25}
# print(dic.get('salii'))

# arr=[1,2,3,4,5,7,8]
# for num in range(len(arr)):
#     if (num+1)-num!=1:
#         print(num)
# print(num)



# arr=[1,2,3,4,5,7,8]
# i=0
# while i< len(arr)-1:
#     if arr[i+1]-arr[i]!=1:
#         print(arr[i]+1)
#     i+=1 #