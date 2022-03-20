num = int(input("Enter a number to find fibonaci of first n numbers: "))

def fibonaci(n):
    if num <= 0:
        print("Invlaid")

    elif num == 1:
        a = 0
        b = 1
        print(a)
        
    else:
        a = 0
        b = 1
        result = []
        result += [a]
        result += [b]
        for i in range(2,n):
            c = a+b
            a = b
            b = c
            result += [c]
        #print(c)
        print("The fibonaci series of first {} numbers is :".format(num),result)

fibonaci(num)
