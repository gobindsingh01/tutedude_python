filename = "sample.txt"
try :
    file = open(filename,"r")
    filelines = file.readlines()
    print("Reading file content:")
    for i in range(len(filelines)):
        print(f"Line {i}: {filelines[i]}",end ="")
    print()
    file.close()
except FileNotFoundError:
    print(f"Error: The file {filename} was not found!")