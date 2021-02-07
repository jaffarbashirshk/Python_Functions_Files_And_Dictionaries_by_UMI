#Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.
fileref = open("school_prompt.txt",'r')
characters = fileref.read()
beginning_chars = characters[0:30]
print(beginning_chars)

