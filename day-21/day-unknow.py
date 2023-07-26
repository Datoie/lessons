# For easy I can wtite
# If b == R just a . sort and this srot method is use to increese numbers with inccrese rule and sort(reverse=True) means decrees rule and this work as normal sort method but revrsed
# And if b== L it will reverse


# def flip(b,a):
#     if b=='R':
#         a.sort()
#     elif b== 'L':
#         a.sort(reverse=True)
#     return a
# print(flip("L",[9, 8, 3, 2, 1, 0]))





# სორტირების გარეშე გავაკეთე ფუნქიცა რომელშიც შედის L and R მარჯვნივ ზრდის max მეთოდი და min მარცხნივ,
# I create arr wich eqauls empty arry for add min and max number in oure siuation L and R
# So if b =='L' i made nested for loop one for repeate and one for calcuation because if we only write only one loop it will end soon and ony give us max and nim number each one
# After that i write if i(wich is list numbers)== minimum number a.k.a smallest number I add toour empty arry and remove that min muber to roll thet numbers and after that
# Method shoud end I mean i for loop and our x loop will roll again before the minimum number is will not gone and also it is same function as R I only change min to max to increese numbers
# def flip(b,a):
#     arr=[]
#     if b=="L":
#         for x in range(len(a)):
#             for i in a:
#                 if i == min(a):
#                     arr.append(i)
#                     a.remove(min(a))
#                     break
#         return arr
#     elif b=="R":
#         for y in range(len(a)):
#             for i in a:
#                 if i == max(a):
#                     arr.append(i)
#                     a.remove(max(a))
#                     break
# print(flip("L",[9, 8, 3, 2, 1, 0]))






# another way jus one loop 
# def
#  flip(b,a):
#     arr2=[]
#     for i in range(len(a)):
#         arr2.append(max(a))
#         a.remove(max(a))
#     if b=="R":
#         return arr2
#     arr2.reverse()
#     return arr2
# print(flip("2",[9, 8, 3, 2, 1, 0]))


# def remainder(a,b):
#     if min(a,b)==0:
#         return None
#     elif a>b:
#         return a&b
#     elif a<b:
#         return b&a
    
# print(remainder(-13,2))






# x='!Hi!'

# if "!" == x[-1]:
#     print(x[:-1])
# elif "!" == x[0]:
#     print(x[1:])







# websites = ["codewars"]
# x=0
# for i in range(1000):
#     x+=1
#     print(websites[0]+' '+str(x))


# obj=['even' if i%2==0 else 'odd'for i in range(10)]
# print(obj)


# n=1
# if n ==1 or n==0 or n<0:
#     print(0)
# elif n>1 and n<=13:
#     print(n-1)
# elif n>13:
#     print(n-2)





# x=0
# new_str=''
# for i in range(5):
#     if x==0:
#         new_str+='1'
#         x+=1
#     elif x==1:
#         new_str+='0'
#         x-=1
# print(new_str)




# size=5
# new_srt=''
# for i in range(1,size+1):
#     if i%2==1:
#         new_srt+='1'
#     if i%2==0:        
#         new_srt+='0'
# print(new_srt)


# int_=5
# limit=25
# print([i for i in range(int_,limit+1) if i%int_==0])


# str_='aaaaaawwwwwqqqqqaaaaaaaaa'
# str1=''
# for i in str_:
#     if i in 'aeiou':
#         str1+=''
#     else:
#         str1+=i
# print(str1)





# s='aaaaaaawwwwwwwwwwaaaaaaaa'
# print(''.join(i for i in s if i not in 'aeiou'))




# s='dasdasda'
# vowel_count=0
# for char in s:
#     if char in 'aeiou':
#         vowel_count+=1
# print(vowel_count)




# s='this website is for looser'
# print(s.count('a'))

s='this wEbsIte is for looser'
print(''.join(i for i in s if i.lower() not in 'aeiou'))