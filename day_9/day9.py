def revers_arr(any_arr):

    new_arr = []
    i = len(any_arr)
    for classs in any_arr:
        new_arr.append(any_arr[i-1])
        i-=1
    print(new_arr)

# ფუნქციის მორალი!! რამდენჯერაც დაგვჭირდება ფუნქცია იმდენჯერ გამოივყენბებთ ყველგან
# ფუნქცია არის ყუთი რომელსაც აქვს გარკვეული დანიშნულება და რაც არ უნდ აჩავყაროთ ყუთში ყველაფერი იმუშავებს კანფეტივით :) <3


#შექმენით ფუნქცია რომელსაც გადაეცემა 2 მოთამაშის ქულა
#დაპრინტეთ წინადადება "ამას უფრო მეტი ქულა აქვს ამდენით"

def number_game(p1_score,p2_score):
    
    if p1_score>p2_score:
        print("{} უფრო მეტა {} ქულაზე {}-ით".format(p1_score,p2_score, p1_score-p2_score))
    else:
        print("{} უფრო მეტა {} ქულაზე {}-ით".format(p2_score,p1_score, p2_score-p1_score))
number_game(300,400)

def multipy(a,b):
    return a * b