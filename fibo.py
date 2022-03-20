num = int(input("Enter a number to find fibonaci of first n numbers: "))

def fibonaci(n):
    a = 0
    b = 1

    if num <= 0:
        print("Invlaid")

    elif num == 1:
        print(a)
    else:
        print(a)
        print(b)
    
    for i in range(2,n):

        c = a+b
        a = b
        b = c
        print(c)

fibonaci(num)