# a = 'dadasdafhfvcidguiewhiqwu'
# b='wqnsxbncvoiqoxmpqwieio'

# def words(a,b):
#     return ''.join(sorted(set(a+b)))
# print(words(a,b))

# def valitated_pin(pin):
#     return pin.isdigit() and (len(pin)==4 or len(pin)==6)
# print(valitated_pin('1123'))


#       lambda
# print ((lambda x: x+5) (1))





#      map 
#              y
# def add_five(x):
#     return x+5

# def finnal_result(y):
#     return list(map(add_five, y))
# print(finnal_result([1,2,3,4,5]))




#      map
# def finnal_result(y):
#     return list(map(lambda x: x+1, y))
# print(finnal_result([1,2,3,4,5]))




#     recursion
# def odd(x):
#     if x%2==0:
#         return x
#     else:
#         return x+odd(x-1)
# print(odd(7))


# def divisors(num):
#     arr=[]
#     for i in range(num):
#         if type(i // num) ==type(int):
#             arr.append(i)
#     return arr
# print(divisors(15))

# print((10.0//5)/10.0)


def stray(arr):
    new_arr=[]
    for i in arr:
        if arr.count(i) ==1:
            return i

print(stray([1,1,1,1,1,1,2]))