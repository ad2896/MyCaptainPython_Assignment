
user_input = input("Input the Filename: ")
ext = user_input.split(".")
#print(ext)
#print(ext[1])
if ext[1] == 'py':
    print("The extension of the file is: 'python'")

elif ext[1] == 'java':
    print("The extension of the file is: 'java'")

elif ext[1] == 'exe':
    print("The extension of the file is: 'Executable'")

else:
    print("Unknown extension")

