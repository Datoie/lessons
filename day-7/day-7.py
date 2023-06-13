# menu = ["xinkali", "mwvadi", "lobiani", "qababi", "khachapuri", "wyali",]

# menu[1] = "BBQ"
# print(menu)

# menu[2:5] = ["a", "bb", "cc"]


# my_name = "nikuhsa"

# new_name = " "

# print(my_name.replace("k", "qq"))

# menu = ["xinkali", "mwvadi", "lobiani", "qababi", "khachapuri", "wyali",]
# menu.insert(3, 'nayini')
# print(menu)
# insert is adding objects in lists

# menu.append("cecxli")
# menu.append("navti")
# print(menu)


#მომხმარებელს შემოატანინეთ 5 საჭმელი
#სიასში შეიტანეთ ისინი რომლებლებიც შეიცავენ მინიმუმ 2 "ა" -ს
# menu = []
# i = 0
# while i < 2:
#     food = input("enert food: ")
#     amount_of_a = 0
#     for char in food:
#         if char == "a":
#             amount_of_a += 1
#     if amount_of_a >=2:
#         menu.append(food)
#     i+= 1
# print(menu)



# menu = ["xinkali", "mwvadi", "lobiani", "qababi", "khachapuri", "wyali",]

# menu.remove("wyali")

# print(menu)

# წაშალეთ ის ელემენტი, რომელში მერე ასო არის a
# menu = ["xinkali", "mwvadi", "lobiani", "qababi", "khachapuri", "wyali",]

# new_menu = []
# for food in menu:
#     if food[1] != "a":
#         new_menu.append(food)
# print(new_menu)

#remove and loop togeder never do that if u want remove object create new list and in youre loop section write that object if u dont want to be in ure liste and maek new list that contain evertihng exept taht item thats all
#do not muatate origran list

# scores = [20, 43, 56, 73, 10, 6, 87, 45 ,97]
# scores.sort(reverse = True)
# print(scores)
# sort help to make list grow up or grow down reverse = True with that


#1) დაასორტირეთ  scores = [20, 43, 56, 73, 10, 6, 87, 45 ,97]
#sort() მეთოდის გარეშე და maxa  ფუნქციის გარეშე დამიბრუნეთ ყვლეაზე დიდი რიცხვი

#while ციკლით სათიტადო შეამოწმეთ ელემენტი და მის მარჯვნივ მდგომ, რომელიც უფორ დიდი იქნება,
#დროიებით მიანიჭეთ მაქსიმუმ მნიშვნელობა და შემდეგ შეადარეთ მის მარჯვნივ მდგომს

# შევქმენი ახლაი ცვლადი და მივანიჭე მას პირველი ლისტის შესაბამისობა ამის შემდეგ
# საიტერაციო ცვლადიც შევქმენი რომელსაც 0 ის მნშვნელობა მივანიჭე
# შემდეგ ვაილ ციკლი შევქმენი.რომელიც რამხელაც იყო ჩვენი ლისტი იმდენჯერ შეამოწმებდა ციკლში დაწერილი ფუნქციას
# შემდეგ დავწერე იფ ელს მეთოდი სადაც ჩვენს მიერ შექმნილი ცვლადი top_num ნაკლები უნდა ყოფილიყო ლისტში მყოფ რიცხვებზე
# რათა მიეღო მას უდიდესი მნიშვნელოა. ჯერ გახდებოდა 20 მერე 43 და ა.შ. სნამ არ მიაღწევდა უდიდეს მნიშვნელობას 

scores = [20, 43, 56, 73, 10, 6, 87, 45, 97]

top_num = scores[0] # 20

i = 0
while i < len(scores):
    # თუ მოგივდებოდა ყველაზე პატარას ნახვა <3 დავწერდით >
        #20 10 6       [20, 43, 56, 73, 10, 6, 87, 45, 97]
    if top_num < scores[i]:
        top_num=scores[i]
    i += 1

print("Omg bro " + str(top_num))
# 2) დაწერეთ უკუღმა menu = ["xinkali", "mwvadi", "lobiani", "qababi", "khachapuri", "wyali",] 
# revers და sort() ის გაეშე <3


# პირველ რიგრში შევქმენი ახალი ლისტი new_menu რომ ჩგვწერეა ჩვენი ახალი სია <3
# შემდეგ შევქმენი ცვლადი n რომელასაც მივანიჭე სიის სიგრძის მნიშვნელობა <3
# შემდეგ საინკრემენტაციო i ცვლადი შევქმენი და while ლუპი მეთოდი დავწერე
# რომელიც შეამოწმებდა ლისტს. რამდენი ობიექტიც იქნებოდა ლისტში იმდენჯერ შეამოწმენდა ეს ციკლი
# მერე if else ფუნქციის დახმარებით დავწერე თუ i < n მაშინ n მოკლდებოდა -1 ციფრი და 6 იდან დაგვრჩებოდა 5
# new_memu ში დავამატე შემდეგ menu ში მყოფი ობიექტვები რომელიც ჩავსვი [n] რათა უკუღმა დაეწყო ობიექტების დაწერა ჩვენს new_menu ში
# ამის შემდეგ ვიღებდი მარტო 3 ობიექტს უკუღმა ამიტომ გდავვყიტე რომ i -= 1 დამეწერა რომ გაეთანაბრებინა n ცვლადის მნიშვნეობა <3



menu = ["xinkali", "mwvadi", "lobiani", "qababi", "khachapuri", "wyali","დათვი"]
new_menu = []
n = len(menu)
i = 0
while i < n:
    if i < n:
        n -= 1
        i -=1
        new_menu.append(menu[n])
    i += 1
print(new_menu)


