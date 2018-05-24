try:
    print("Hi")
    a=1/0
    f= open("text1.txt",'r')
    print(f.readline())
    t='s'+1
except ZeroDivisionError:
    print("Zero Error")
except TypeError:
    print("Type Error")
except NameError:
    print("Name Error")