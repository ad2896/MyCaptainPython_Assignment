
count = []
even = []
odd = []

for i in range(0,101):
    count +=[i]
print(count)
for i in count:
    if i % 2 == 0:
      even +=[i]
print(even)
print(f"The count of even numbers in first 100 numbers is {len(even)}")
for i in count:
  if i % 2 ==1:
    odd +=[i]
print(odd)
print(f"The count of odd numbers in first 100 numbers is {len(odd)}")
