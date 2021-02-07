#We have provided a file called emotion_words.txt that contains lines of words that describe emotions. Find the total number of words in the file and assign this value to the variable num_words.
fileref = open("emotion_words.txt",'r')
lines = fileref.readlines()
num_words = 0
for word in lines:
    num_words +=len(word.split())
print(num_words)
​

