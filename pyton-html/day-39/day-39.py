# text = input()
# word = input()
# def search(text, word):
#     text=text.split()
#     for char in text:
#         if char == word:
#             return "Word found"
#         elif char != word:
#             return "Word not found" 
        
# print(search(text, word))









# write the function is_anagram

# def is_anagram(test, original):
#     test=test.lower()
#     original=original.lower()
#     arr=[]
#     new_arr=[]
#     for char in test:
#         arr.append(char)
#     for char_1 in range(len(arr)):
#         if test[char_1] in original:
#             arr.remove(test[char_1])
#     # if ''.join(arr) in original and len(test)==len(original):
#     #     return True
#     # else:
#     #     return False
#     return ''.join(arr)
#     for char_1 in arr:
#         if char_1 in original:
#             return True
#         return False

# print(is_anagram("davita", "davita"))




# one way




# def sort_by_length(arr):
#     arr_new = []
#     for item in arr:
#         arr_new.append((len(item), item))
#     arr_new.sort()
#     return [i[1] for i in arr_new]


# num='1234'
# print(bin(int(num,))[2::])
