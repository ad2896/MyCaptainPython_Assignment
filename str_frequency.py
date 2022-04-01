"""
Write Python code to create a function called most_frequent that takes a string and 
prints the letters in decreasing order of frequency. Use dictionaries.
Your Input and output should look something like this
Input : Please enter a string Mississippi
Output : i = 04 s = 04 p =02 m =01 

"""
from operator import itemgetter
import operator

repeat ={}

def most_frequent(str):
    for i in str:
         if i in repeat:
            repeat[i] += 1
         else:
            repeat[i] = 1

   #print(repeat)
   #METHOD 1
    newDict = dict(sorted(repeat.items(), key=operator.itemgetter(1),reverse=True))
   #print(newDict)

    for keys,values in newDict.items():
        print(keys+"-->",values)

most_frequent('Mississippi')

#METHOD 2
# I TRIED USING FOR LOOPS BUT I GET A KEY ERROR = 'i'
# CANT WE DO LIKE THIS ??
"""
list = sorted(repeat.values(),reverse= True)
print(list)

newDict={}
for i in list:
   for k in repeat.keys():
      if repeat[k] == i:
         newDict[k] == repeat[k]
         break
print(newDict)

"""
#CAN YOU GIVE ME FEEDBACK ON WHY THIS ERROR COMES ?

