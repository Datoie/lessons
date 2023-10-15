def persistence(num):
    if len(str(num))==1:
        return 0
    num_str = str(num)
    product = 1
    for digit in num_str:
        product *= int(digit)
    return 1+ persistence(product)
# print(persistence(39))
# შეგვიძლია რომ დავუმატოთ ერთი რეკუსიას და ვატრიალოთ ფუნქცია სულ
# print(len('asdfads'))


def find_even_index(arr):
    # count=0
    # sum_arr=[]
    # for i in range(len(arr)):
    #     if sum(arr[i:])==sum(arr[:i+1]):
    #         return i
    return arr[4:]  ,arr[:4+1]
print(find_even_index([1,2,3,4,3,2,1]))
