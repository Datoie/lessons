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
# 1) I create function call odd_or_even and type arr into parentheses 
# 2) I create variable and equal to sum of parentheses
# 3) I create if else conditional operator which give us the number is even or odd
# 4) I call pritn output and call funtion and that function I crate arry to sum some numbers and give us ansver is that nuber odd or even
def odd_or_even(arr):
    sum_off_arr = sum(arr)
    if sum_off_arr % 2==0:
        return "even"
    elif sum_off_arr % 2 == 1:
        return "odd"
print(odd_or_even([1,3]))



# sum in pyton is suming numbers

#1) I create funtion call opposite and write into parantheses number
#2) I create if eles conditional operator which give u sulution if oure parentheses more than zero return negative parenteses if don't
# zero more or equal to zero retunrn begative parentheses

def opposite(number):

  # your solution here
    if number > 0 :
        return -number
    elif number <= 0:
        return-number
#1) or olny multiply to -1
def opposite(number1):
    return number1 * -1
print(opposite(-3))



# Complete the solution so that it reverses the string passed into it.

# 'world'  =>  'dlrow'
# 'word'   =>  'drow'
#I return stirng with square brakets we know that numbers in square brakets first number give us full variable exept fist number or letter second give us last letter
#and therd is give us every chaacter or number in variable and if we give negative one in that square brakets it will give us value top to down
def solutin(stirng):
    return stirng[::1]
print(solutin("davit"))


#1) I create funtion call bool_to_word and write into praantheses bollean
#2) I create if else conditional wich give us solution if oure parantheses eqcual to True return "Yes" else "No"
def bool_to_word(boolean):
    # TODO
    if boolean == True:
        return "Yess"
    else:   
        return "No"
print(bool_to_word(1))
