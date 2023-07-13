# print (int(str(34.0 //3)[:-2]))
# print(int(6//2.0))

# my_arr = [5, 6, 7, 1]

# x = 's'.join(my_arr)
# print(x)

def my_join (arr):
    finnal_str = ''
    for e in arr:
        finnal_str +=str(e)+ " "
    return finnal_str.split()
# print(my_join([3,1,2,4]))
def dad(dad, son):
    return (dad-2*son)
print(dad(47,14) * dad(33,9))