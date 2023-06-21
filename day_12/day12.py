# arr = ["datvi", "gochi", "xbo", "txa"]

# for i, item in enumerate(arr):
    # print(i, item)


# იმიტომ ვანიჭებთ პარამტერს სტინგის ნიშანს რომ for ციკლში ვერ დავშლით ციფრებს აი სტრინგი კიდე მოსულა
# ამ სტინგს შემდგომში გადავაქცევთ ისევ ციფებად
def digitize(n):
    arr = []
    for i in str(n):
        arr.append(int(i))
    arr.reverse()
    return arr
print (digitize(12313))
