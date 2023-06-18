# from day9 import revers_arr
# from day9 import number_game
# from day9 import multipy
# students = ["davit", "gio", "lola", "ucha", "goga", "leri"]

# revers_arr(students)

# lisi_mannaers = ["kaxa", "dzigo", "zviada"]
# revers_arr(lisi_mannaers)


# print(multipy(1,2))
#mul
# tipy(1,2) კი გამოითვლა მაგრამ შეინახა return მეთოდში დაამიტომ დაგვჭირდა print ის გამოყენება <3




# Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
def odd_or_even(arr):
    sum_off_arr = sum(arr)
    if sum_off_arr % 2==0:
        return "even"
    elif sum_off_arr % 2 == 1:
        return "odd"
print(odd_or_even([1,3]))



# sum in pyton is suming numbers


def opposite(number):
  # your solution here
    if number > 0 :
        return -number
    elif number <= 0:
        return-number
def opposite(number1):
    return number1 * -1
print(opposite(-3))



# Complete the solution so that it reverses the string passed into it.

# 'world'  =>  'dlrow'
# 'word'   =>  'drow'
def solutin(stirng):
    return stirng[::-1]
print(solutin("davit"))



def bool_to_word(boolean):
    # TODO
    if boolean == True:
        return "Yess"
    else:   
        return "No"
print(bool_to_word(1))