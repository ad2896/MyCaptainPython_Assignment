#Input: list1 = [12, -7, 5, 64, -14] Output: 12, 5, 64

#Input: list2 = [12, 14, -95, 3] Output: [12, 14, 3]

list = list(map(int, input("Enter multiple value: ").split()))

list1 = [ x for x in list if x>0]
list2 = [x for x in list if x<0]
print("Positive integers are: ",list1)



