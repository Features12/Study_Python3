def a(*args):
    sum = 0.0
    for i in args:
        print("i = ",i)
        sum += i
        print("sum =",sum)
    return sum / len(args)


a(3,5,1)
