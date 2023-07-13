def dna_to_rna(dna):
    return dna.replace("T", "U")

# print(dna_to_rna("asdasTdsdaTTT"))

def reverse_seq(n):
    arr = []
    for i in range(n):
        arr.append(i+1)
        n-=1
    return (arr)[::-1]
# print(reverse_seq(5))

# s=220 * 100000 // 36000
# print(s)
def sumMul(n, m):
    if n <= 0 or m <= 0:
        return "INVALID"
    
    multiples = []
    for i in range(n, m, n):
        multiples.append(i)
    
    return sum(multiples)
# print(sumMul(2,10))

def get_char(c):
  # Your code goes here ^_^
    if c == c:
        return "A"
# print(get_char(56))

def better_than_average(class_points, your_points):
    sum_class_avarage = sum(class_points) // len(class_points)

    if your_points > sum_class_avarage:
        return True
    else:
        return False
# print(better_than_average([1],45))

def triple_trouble(one, two, three):
    i = 0
    new_str =''
    while i < len(one):
        new_str+=one[i]
        new_str+=two[i]
        new_str+=three[i]
    return new_str
# print(triple_trouble('ff','da','dddd'))

def position(alphabet,letter):
    x = 0
    for letter in alphabet:
        if letter.lower() == letter:
            x += 1
    return "The position of "+ letter +" in the alphabet: {}".format(x)
# print(position("aaaaab","b"))

# seats = 2
# while seats > 0:
#   print("Sell ticket")
#   seats = seats - 1
#   print(seats)


def number_to_string(num):
    # Return a string of the number here!
    new_stirng = ""
    return new_stirng + str(num) 
# print(number_to_string(1))

def find_smallest_int(arr):
    arr.sort()
    return arr.sort()
# print(find_smallest_int([1,2,3]))

def find_smallest_int(arr):
    # Code here
    min_int = arr[0]
    for i in arr:
        if min_int > i:
            min_int = i
    return min_int
# print(find_smallest_int([1,2,4,16,19]))

def summation(num):
    return sum(range(num+1))
# print(summation())       

def century(year):
    # Finish this :)
    if year% 100==0:
        return year//100
    else:
        return year//100 +1
# print(century(2001)) 
def count_positives_sum_negatives(arr):
    new_arr=[]
    p =0
    for i in arr:
        if i >0:
            p+=1
            new_arr.append(p)
    return new_arr
# print(count_positives_sum_negatives([1,4,6,-1,-1,-5]))

def grow(arr):
    sum =0
    for i in arr:
        if i < len(arr):
            sum *=i
    return sum 
# print(grow([5555,5555,5555]))

def cost(d):
    result = d * 80085

    if d < 5 and d <10:
        return result - 69000
    elif d>=10:
        return result -99000
print(cost(10))
