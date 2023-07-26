# a = [4, 1, 2, 3]
# b = list(range(1,6,2)) # b = [1, 3, 5]
# for i in a: #i=4 

#             #4+1=5 and this 5 is out of range because we dont have inde 5 in a
#     b.append(a[i+1] + a[i])
# print(b)

# arr = [[3,5],[2, 1, 4, 1],[1, 1, 2]]

# print(arr[1][3])

# # scalar
# s = 5

# # vector a
# my_arr = [1,5]

# # matrix
# my_matrix = [
#     [3,5],
#     [2, 1, 4, 1],
#     [1, 1, 2]
# ]

# number = list(range(50, 10, -5))
# print(number)




# HOME WORK BROOOOOOO

# პირობა არის რო aa bb cc  რასაც დავწერთ უნდა დაიწეროს ერთმანეთს მიმატებით მაგ:
# (["a", "b", "c", "d"],["1", "2", "3", "4"], ["goga", "guga", "gaga", "dadaaaaaa"])   return a1goga

def ziped(aa,bb,cc):
    ziped = [aa] + [bb] + [cc]
    x = [0,1,2]
    arr = []
    for i in range(4):
        arr.append(ziped[x[0]][i]+str(ziped[x[1]][i])+ziped[x[2]][i])
    return arr
    # return ziped[x][0]+ziped[z][0]+ziped[c][0] +' '+ ziped[x][1]+ziped[z][1]+ziped[c][1] + ' ' + ziped[x][2]+ziped[z][2]+ziped[c][2]
print(ziped(["A", "B", "C", "D"],[1, 2, 3, 4], ["goga", "guga", "gaga", "Dadaaaaaa"]))
