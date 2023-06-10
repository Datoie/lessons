# x = 0
# for i in range(5):
#     for j in range(4):
#         print("davit" + str(x))
#         x += 1


# 18
# 24
# 2
# 5
# 42

# 4 * 100
# total_price = 0
# for i in range(5):
#     age_of_user = int(input("enter user age: "))
#     if age_of_user >= 3:
#         total_price += 100

# print(total_price)

# რასაც დაწერ ციკლში რა სიგრძისას არის ციკლი (loop)


# total_price = 0
# i = 0
# while i < 5:
#     age_of_user = int(input("enter user age: "))
#     if age_of_user >= 3:
#         total_price += 100
#     i += 1
# print(total_price)

# i = 0
# x = 0
# while i < 4:
#     x += i
#     i += 1
#     print (str(i) + " " + str(x))
# print (x)

#list = სია

# int, float, boolean, list

# my_list = ["xinkali","wvadi","lobiani","chaxoxblili"]
# price = [2, 10, 16, 5, 6]
# weid_list = ["davit", "davit1", "davit2",[1,2,3] ,"davit3"]

# print(weid_list[3][1])


# xinkali girs 2 lari
#mwvadi girs 20 lari


my_list = ["xinkali", "mwvadi", "lobiani", "qababi", "khachapuri", "wyali"]
price = [2, 20, 15, 10, 15, 2]

priece_incremet = 0

for food in my_list:
    print(food + " price is: " + str(price[priece_incremet]))
    priece_incremet += 1