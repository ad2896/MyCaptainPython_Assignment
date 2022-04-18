
while True:
    user = input("Please enter (odd/even) to print the list of (odd/even) numbers : ")
    #First 100 odd numbers :
    if user == "odd":
        value= int(input("Enter any number to print the list of odd numbers: "))
        print(f"The first {value} odd numbers are: ")

        def odd_no(value):
            odd = []
            for i in range(1,value+1): 
                if i % 2 == 1:
                    odd += [i]
            print(odd)

        odd_no(value)
        break
    #First 100 even numbers :
    elif user == "even":
        value= int(input("Enter any number to print the list of even numbers: "))
        print(f"The first {value} even numbers are: ")

        def even_no(value): 
            even = []
            for i in range(1,value+1): 
                if i % 2 == 0:
                    even += [i]
            print(even)
        
        even_no(value)
        break
    



