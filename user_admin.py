#GET USER INPUT LIKE name ,age ,phonenumber,mailid into a list 
#use while Loop to get MORE student info until the condition changes 
import csv 

def write_into_csv(info):
    with open('student.csv','a',newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        if csv_file.tell()==0:
            writer.writerow(["Name","Age","Contact number","Email ID"])    
    
        writer.writerow(info)

def new_func(write_into_csv):
    condition = True
    student_num = 1
    while(condition):
        user_input = input("Enter some student info for student #{} in the format (Name Age Phno email id): ".format(student_num))
        #print("The entered info is : "+user_input)

        user_input_list= user_input.split(" ")

        print("Entered info is \nName: {}\nAge: {}\nPh No: {}\nEmail: {} "
    .format(user_input_list[0],user_input_list[1],user_input_list[2],user_input_list[3]))

        choice_check = input("Is the entered info correct(yes/no): ")
        if choice_check == "yes":
            write_into_csv(user_input_list)
            condition_check = input("Enter(yes/no) if you want to enter more info: ")
            if condition_check =="yes":
                condition = True
                student_num = student_num + 1
            elif condition_check =="no":
                condition = False
        elif choice_check == 'no':
            print("\nPlease re-enter the values: ")

if __name__ == '__main__':
 new_func(write_into_csv)

