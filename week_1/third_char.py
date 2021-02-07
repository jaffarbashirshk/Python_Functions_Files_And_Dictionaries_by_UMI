#Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called three.
fileref = open("school_prompt.txt",'r')
characters = fileref.readlines()
three = []
for line in characters:
    line = line.split()
    three.append(line[2])
print(three)
