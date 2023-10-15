# def small_enough(arr, limit):
#     for num in arr:
#         if num > limit:
#             return False
#     return True
# print(small_enough([78, 117, 110, 99, 104, 117, 107, 115],107))

# def all_values_below_or_equal_to_limit(arr, limit):
#     for value in arr:
#         if value > limit:
#             return False
#     return True






# def sum_digits(number):
#     arr=[]
#     for num in str(int(int(number))):
#         arr.append(int(num))
#     return sum(arr)
# print(sum_digits(-32))
# print(-15%5)






# def duplicate_count(text):
#     result=0
#     arr=[]
#     text=text.lower()
#     for char in text:
#         counter=text.count(char)
#         if counter>1:
#             arr.append(char)
#     return set(arr)
# print(duplicate_count('gaS3gZLwf3zOhbCi8wWK7QF'))