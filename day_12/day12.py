# arr = ["datvi", "gochi", "xbo", "txa"]

# for i, item in enumerate(arr):
    # print(i, item)


# იმიტომ ვანიჭებთ პარამტერს სტინგის ნიშანს რომ for ციკლში ვერ დავშლით ციფრებს აი სტრინგი კიდე მოსულა
# ამ სტინგს შემდგომში გადავაქცევთ ისევ ციფებად
def digitize(n):
    arr = []
    for i in str(n):
        arr.append(int(i))
    arr.reverse()
    return arr
print (digitize(12313))


def abbrev_name(name):
    my_arr = name.split()
    return my_arr[0][0].capitalize() + "." + my_arr[1][0].capitalize()
# print(abbrev_name("adad asasasd ddad"))

def find_needle(haystack):
    # your code here
    i = 0
    for elements in haystack:
        if elements == "needle":
            return("found the needle at position {}".format(i) )
        i+=1
# print(find_needle(['3', '123124234', None,'dd',  'needle', 'world', 'hay', 2, '3', True, False]))


def find_average(numbers):
    my_sum = 0
    i = 0 
    for num in numbers:
        if num>0:
            my_sum += num
            i+=1
    my_sum=my_sum / i
    return my_sum
# print(find_average([1]))

def likes(names):
    couner_of_fb_user = 0
    for char in names:
        couner_of_fb_user +=1
    if couner_of_fb_user == 0:
        return "no one like this"
    elif couner_of_fb_user <= 1:
        return"{} likes this".format(names[0])
    elif couner_of_fb_user <= 2:
        return"{} and {} like this".format(names[0],names[1])
    elif couner_of_fb_user <= 3:
        return"{},{} and {} like this".format(names[0],names[1],names[2])
    elif couner_of_fb_user > 3:
        return"{},{} and {} other like this".format(names[0],names[1],couner_of_fb_user-2)
# print(likes((['Jacob', 'Alex'])))

#without loop
def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) <= 1:
        return"{} likes this".format(names[0])
    elif len(names) <= 2:
        return"{} and {} like this".format(names[0],names[1])
    elif len(names) <= 3:
        return"{}, {} and {} like this".format(names[0],names[1],names[2])
    elif len(names) > 3:
        return"{}, {} and {} others like this".format(names[0],names[1],len(names)-2)
# print(likes((['Jacob', 'Alex','dd',"ddd"])))

# return masked string
def maskify(name):
    # return (len(name)-2)
    return len(name)

# print(maskify("599-89-89-92"))
def square_digits(num):
    for i in num:
        1>3
    return len(i)
print(square_digits("12"))