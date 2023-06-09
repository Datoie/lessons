# my_name = "davit"

#     #iteration varialbe
# for char in my_name:
#     print(char)

# print("i" in "nika")
# print("d" in "davit")

# name1 = input("enter name1: ")
# name2 = input("enter name2: ")

# incrementation variables
# amount_of_vowels_in_name1 = 0
# amount_of_vowels_in_name2 = 0

# for char in name1:
#     if char in "aeiou":
#         amount_of_vowels_in_name1 += 1

# for char in name2:
#     if char in "aeiou":
#         amount_of_vowels_in_name2 += 1

# if amount_of_vowels_in_name1 > amount_of_vowels_in_name2:
#     print("the amount of vewls i nmae1 is more and it cotains {} vowels".format(amount_of_vowels_in_name1))
# elif amount_of_vowels_in_name2 > amount_of_vowels_in_name1:
#     print("the amount of vewls i nmae1 is more and it cotains {} vowels".format(amount_of_vowels_in_name1))
# else:
#     print("the have ecaul amount of voleews")

#შემოიტანეთ რაღაც წინადადვება და დაითვალეთ რამდენი "ა" გვხვდება

# my_text = input("enter text: ")

# amount_of_a = 0

# for char in my_text:
#     if char == "a":
#         amount_of_a += 1
# print("there is {} number in youre 'a'".format(amount_of_a))

# print('"Stay hungry,stay follish" by Steve Jobs') #we can write "" or '' in our print all we can do is start print with "" or ''

# num = 48
# if num > 5:
#     print("gg bro")
#     if num <=47:
#         print("god job")



#დავალებაა მომხმარებელს შემოვატანინოთ სახელი და დავპირნტოთ
#როლის სახელშიც მეტი თანხმოვანი იქნება (დავპირნტოთ ლამაზად!!)

num1 = input("enter num1: ")
num2 = input("enter num2: ")

#inc variable
amount_of_consonant_num1 = 0
amount_of_consonant_num2 = 0

for char in num1:
    if char in "aeiou":
        amount_of_consonant_num1 += 0
    else:
        amount_of_consonant_num1 += 1

for char in num2:
    if char in "aeiou":
        amount_of_consonant_num2 += 0
    else:
        amount_of_consonant_num2 += 1

if num1 > num2:
    print("youre number amont of consonant is more {} than {}".format(amount_of_consonant_num2,amount_of_consonant_num1))
else:
    print("youre number amont of consonant is more {} than {}".format(amount_of_consonant_num1,amount_of_consonant_num2))

