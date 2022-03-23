import json 

n= input("Enter your name: ")
d = input("Enter your Department: ")
num1 = int(input("Enter 1st mark: "))
num2 = int(input("Enter 2nd mark: "))
num3 = int(input("Enter 3rd mark: "))
num4 = int(input("Enter 4th mark: "))
num5 = int(input("Enter 5th mark: "))


class College:

    Name = n
    Dept = d
    m1 = num1
    m2 = num2
    m3 = num3
    m4 = num4
    m5 = num5
 
    def __init__(self):
            print("Name: {}".format(self.Name))
            print("Dept: {}".format(self.Dept))

    def total(self):
        total = self.m1 + self.m2 + self.m3 + self.m4 + self.m5
        return total
            
    def avg(self):
        total = self.m1 + self.m2 + self.m3 + self.m4 + self.m5
        avg = total/5
        return avg
    
    def grade(self):
        avg1 = self.avg()

        if avg1>90:
            return "S Grade"
        elif avg1>80:
            return "A Grade"
        elif avg1>70:
            return "B Grade"
        elif avg1>50 and avg1<70:
            return "C Grade"
        else:
            print("Fail")

student_1 = College()
print("Total: {}".format(student_1.total()))
print("Avg: {}".format(student_1.avg()))


student_1 = {
        'Name':student_1.Name,
        'Dept':student_1.Dept,
        'Mark1':student_1.m1,
        'Mark2':student_1.m2,
        'Mark3':student_1.m3,
        'Mark4':student_1.m4,
        'Mark5':student_1.m5,
        'Total':student_1.total(),
        'avg':student_1.avg(),
        'Grade':student_1.grade()
        }

#print(student_1)


with open("file.json",'w') as f:
    json.dump(student_1,f)

read = open('file.json')
data = json.load(read)
print(data)
