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
print(position("aaaaab","b"))
