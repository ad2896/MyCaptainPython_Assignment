"""
Write Python code to create a function called most_frequent that takes a string and 
prints the letters in decreasing order of frequency. Use dictionaries.

Your Input and output should look something like this

Input : Please enter a string Mississippi

Output : i = 04 s = 04 p =02 m =01 

"""

repeat = {}

def most_frequent(str):
    for i in str:
        if i in repeat:
            repeat[i] += 1
        else:
            repeat[i] = 1
    print(repeat)

most_frequent('Mississippi')


key = [x for x, y in repeat.items()]
value = [y for x, y in repeat.items()]

for (a,b) in zip(key,value):
    print(str(a)+"=0"+str(b))

# NOTE: Im not aware of how to sort the dictionary based on values(descending order) .

