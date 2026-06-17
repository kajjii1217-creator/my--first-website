file = open ("notes . txt", "w")
file.write ("My name is mr kaji basnet\n")
file.write ("I am a teacher\n")
file.write ("I am teaching python programming\n")
file.write("I study in rju university\n")
file.close()
print("File saved!")



file = open("notes.txt", "r")
content = file.read()
print("\nFile content:")
print(content)
file.close()