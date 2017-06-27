
try:
    a = 20
    b = 0
    print(a/b)
except ZeroDivisionError:
    print('hey this is an error')
finally:
    print('this always shows')