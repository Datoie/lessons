# 1) for loop 
# 2) while loop

# i საიტერაციო ცვლადი 
# for i in range(4): #range(4) = 1 2 3 4 this range is counting numbers in py
#     print("nika")

# for i in range(3,6): # საიტერაციო ცვლადი ართმევს range ობიექტს რიცვს და თავის თავში აჯენს
#     print(str(i) + "davit")


            #start #finish #step
# for i in range(5, 10, 2): # საიტერაციო ცვლადი ართმევს range ობიექტს რიცვს და თავის თავში აჯენს
#     print(str(i) + "davit")


# i = 0 #საიტერაციო ცვლადი
# while i < 5:
#     print("davit")
#     i += 1

# full_name = "davit grdzelishvili"

# i = 0
# while i < len(full_name):
#     print(full_name[i])
#     i += 1


# a = "qwerty"
# b = "asdfgh"

# i = 0
# while i < 6:
#     print(a[i] + b[i])
#     i += 1    

#qa
#ws
#ed
#rf

# boolean logic <3
# if 10 > 5 and 3 > 1: #აუცილებლად უნდა იყოს ორივე სწორი <3
#     print("cool")

# if 10 < 5 or 3 > 1:
#     print("great",)





#ინფუთით შეიტანეთ თქვენი სახელი და გვარი,
#ტერმინალში გამოიტანეთ რომელ ინდექსზე არის ხმოვანი


full_name = input("enter youre full name: ")

i = 0

while i < len(full_name):
    if full_name[i] in "aeiou":
        print(str(i) + " " + full_name[i])
    i += 1