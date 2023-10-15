# კენტი უნდა დაიპრინტოს და არა ლუწი. და შედეგი უნდა შეიკრიბოს შემდეგ დაიპრინტოს
# day 3
def odd_numbers_combinator ():


    num1 = int(input("enter num1: "))
    num2 = int(input("enter num2: "))
    num3 = int(input("enter num3: "))

    if num1 % 2 ==0:
        num1=0
    else:
        num1=num1
    if num2 % 2 ==0:
        num2=0
    else:
        num2=num2
    if num3 % 2 ==0:
        num3=0
    else:
        num3=num3
    result = num1 + num2 + num3
    print("good job you finnaly made it :) here youre result " + str(result))
# odd_numbers_combinator()




# დავალებაა მომხმარებელს შემოვატანინოთ 2 სახელი და დავპირნტოთ
# რომლის სახელშიც მეტი თანხმოვანი იქნება (დავპირნტოთ ლამაზად!!)
# day 4
def consonant_name_letters():
    name1 = input("enter name1: ")
    name2 = input("enter name2: ")

    # inc number
    amount_of_name1 = 0
    amount_of_name2 = 0

    for char in name1:
        if not char in "aeiou":
            amount_of_name1 +=1
    for char in name2:
        if not char in "aeiou":
            amount_of_name2 +=1
    print("In youre name 1 are {} consonat than number 2 {}".format(amount_of_name1,amount_of_name2))
# consonant_name_letters()
        


#ინფუთით შეიტანეთ თქვენი სახელი და გვარი,
#ტერმინალში გამოიტანეთ რომელ ინდექსზე არის ხმოვანი
# day 5
def odd_in_name():
    name = input("enter youre name: ")
    i = 0
    for odd in name:
        if odd in "aeiou":
            print(str(i)+" number are " + str(odd))
        i+=1
    # while i < len(name):
    #     if name[i] in "aeiou":
    #         print(odd[i] + odd)
    #     i+=1
# odd_in_name()

# day 5



# Day 6
def menu_of_food():
    my_list = ["xinkali", "mwvadi", "lobiani", "qababi", "khachapuri", "wyali",]
    price = [2, 20, 15, 10, 15, 2]

    #increment num
    i = 0
    while i < len(my_list):
        print(my_list[i] + " " + str(price[i]))
        i += 1
# menu_of_food()

#1) დაასორტირეთ  scores = [20, 43, 56, 73, 10, 6, 87, 45 ,97]
#sort() მეთოდის გარეშე და maxa  ფუნქციის გარეშე დამიბრუნეთ ყვლეაზე დიდი რიცხვი




# day 7
#1) დაასორტირეთ  scores = [20, 43, 56, 73, 10, 6, 87, 45 ,97]
#sort() მეთოდის გარეშე და max  ფუნქციის გარეშე დამიბრუნეთ ყვლეაზე დიდი რიცხვი
#while ციკლით სათიტადო შეამოწმეთ ელემენტი და მის მარჯვნივ მდგომ, რომელიც უფორ დიდი იქნება,
#დროიებით მიანიჭეთ მაქსიმუმ მნიშვნელობა და შემდეგ შეადარეთ მის მარჯვნივ მდგომს
def sort_without_sort():
    scores = [20, 43, 56, 73, 10, 6, 87, 45 ,97]
    top_num = scores[0]
    i=0
    while i < len(scores):
        if top_num<scores[i]:
            top_num=scores[i]
        i+=1
    print(top_num)
# sort_without_sort()
    
