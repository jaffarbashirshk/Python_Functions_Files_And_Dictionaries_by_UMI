#Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.
fileref = open("school_prompt.txt",'r')
contents = fileref.read()
contents = contents.split()
p_words = []
for word in contents:
    if 'p' in word:
        p_words.append(word)
print(p_words)
