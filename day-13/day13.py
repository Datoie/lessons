def past(h,m,s):
    return h*3600+60+s*1000

def positive_sum(arr):
    sum_of_negative=0
    for elements in arr:
        if elements > 0:
            sum_of_negative += elements
    return [sum_of_negative]
# print(positive_sum([1,2,3,4,5]))