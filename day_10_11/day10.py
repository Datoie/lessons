# you get an array of numbers , return sum of all psoitive ones

#1) I create funtion call possitive_arr and I give call arr in parenteses
#2) I create incremetaition variable call my_sum and I equal to zero
#3) I ceaete for loop and call numers in arry because in arry there are only numbers
#4) I create if else condional operatror and I write thet if oure numbers in arry more than zeor (wich is psoitive numbers) plus my_sum plus (psoitive) numbers in arry
#5) I juste return my_sum
#6) I call funtion possitive_arr wrtie random numbers and print funtion soltions wich give us sum of possitive numbers
def possitive_arr(arr):
    my_sum = 0
    for numbers in arr:
        if numbers > 0:
            my_sum += numbers
    return my_sum
# print(possitive_arr([12,-1,1]))

def positive_arr_with_while_loop(arr):
    my_sum = 0
    i = 0
    while i < len(arr):
        if arr[i] > 0:
            my_sum += arr[i]
        i += 1
    return my_sum
# print(positive_arr_with_while_loop([12,-1,-3,3]))

# Compleate the solution so that it reverse the stintg passe into it

def solution(string):
    my_str = ""
    i = len(string)
    while i > 0:
        my_str += string[i-1]
        i -= 1
    return my_str
# print(solution("davit"))


# Write a funtion that accepts an 
# integer n adn a string s as 
# parameters, adn returns string of
#  s repeated exatly n times
# "I" -> "IIIII"
# "Heloo" -> "HelloHelloHelloHello"

def repeate_str(repeate, string):
    return repeate * string
# print(repeate_str(3,"Davit"))

def remove_char(s):
    return s[1:-1]
# print(remove_char   ("davit"))
def remove_char2(s):
    new_str = ""
    i = 1
    while i < len(s) -1 :
        new_str += s[i]
        i+=1
    return new_str
# print(remove_char2("davit"))

surname = "amraziashvili"
# print(surname[1:5])

#easy
def find_smalest_int(arr):
    return min(arr)
# print(find_smalest_int([23,3]))

#with for loop my version to get lowest number
def find_smalest_int2(arr):
    lowest_num = 0
    for numbers in arr:
        if numbers > 0:
            lowest_num = numbers
    return lowest_num 
# print(find_smalest_int([23,3,5,1]))

#with while loop
def find_smalest_int3(arr):
    min_num = arr[0]
    i = 0
    while i < len(arr):
        if min_num > arr[i]:
            min_num = arr[i]
        i += 1
    return min_num
# print(find_smalest_int([3,5,1]))

#with for loop global versiion
def find_smalest_int4(arr):
    min_num = arr[0]
    for num in arr:
        if min_num > num:
            min_num = num
    return min_num
# print(find_smalest_int4([4,5,1]))

def remeve_space(stirng):
    my_str = ""
    for char in stirng:
        if char != " ":
            my_str += char
    return my_str
# print(remeve_space("davitas Didi Guli Aqvs"))

def sqaure_sum(numbers):
    my_sum = 0

    for num in numbers:
        my_sum += num * num
    return my_sum
# print(sqaure_sum([1,2,5]))

def solution(num):
    num_sum = 0
    for numbers in range(num+1):
        num_sum += numbers
    return num_sum

# print(solution(1))

def solution2(num):
    my_sum = 0
    i = 0
    while i < num + 1:
        my_sum += i
        i += 1
    return my_sum
# print(solution2(4))

def count_sheeps(sheep):
    my_sum = 0
    for char in sheep:
        if char == True:
            my_sum += 1
    return my_sum
# print(count_sheeps([True,False,True]))

# get a sum 6 form print("nika 11 keshelava") with function
def sum_from_string_6():
    my_name = "nika 11 keshelava"
    return int(my_name[5]) + int(my_name[6]) + (4)
#print(sum_from_string_6())

def sum_from_string_15():
    my_name = "nika 11 keshelava"
    return int(my_name[5] + my_name[6]) + (4)
#print(sum_from_string_15())

# give a random non-negative number, reevers it and add to list
# 1236 --> [6, 3, 2, 1]
# easy way! ;))))

def list_reverser(nums):
    return nums[::-1]
# print(list_reverser([1,2,3,7]))


def reverse_menu(menu):
    new_menu = []
    n = len(menu)
    i = 0
    while i < n:
        if i < n:
            n -= 1
            i -=1
            new_menu.append(menu[n])
        i += 1
    return new_menu
print(reverse_menu([1,2,3,4,6,8]))

def reverse_menu(menu):
    new_menu = []
    for i in str(menu):
        new_menu.append(int(i))

    return new_menu[::-1]

print(reverse_menu(1235))


 



    
