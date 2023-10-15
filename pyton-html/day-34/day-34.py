# def gg(x):
#     return x + 1

# num = [1,2,3,4,5,6,7]
# restult= tuple(map(lambda x: x+2,num))
# print(restult)


# names = ['guja','davit','gio','goga','guga','gagai']

# len_name = list(filter(lambda x: len(x)>=5,names))
# print(len_name)



# arr=[]
# for name in names:
#     if len(name)>=5:
#         arr.append(name)
# print(arr)



# def len_name(names):
#     return([name for name in names if len(name)>=5])
# print(len_name(names))

# def yeld_funct():
#     i=0
#     while i<5:
#         yield 1
#         i+=1
# print(yeld_funct())



# txt = input()
# def word(x):
#     for char in x.split():
#         yield char
# print(list(word(txt)))

# def make_word():
#     word = ''
#     x='span'
#     for number in range(len(x)):
#         word+=x
#         return word
# print(list(make_word()))

# def func(n):
#     if n==1:
#         return 1
#     else:
#         return n*func(n-1)
# print(func(4))
