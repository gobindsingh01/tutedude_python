fileName= "output.txt"
text = input("Enter text to write to the file: ")
file = open(fileName,"a")
file.write(text+"\n")
print(f"Data successfully written to {fileName}.\n")

text = input("Enter additional text to append: ")
file.write(text+"\n")
print(f"Data successfully appended.\n")
file.close()

file= open(fileName,"r")
print("Final content of output.txt:")
fileLines = file.readlines()
for i in fileLines:
    print(i,end="")

file.close()