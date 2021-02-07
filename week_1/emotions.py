#Challenge: Create a list called emotions that contains the first word of every line in emotion_words.txt.


fileref = open("emotion_words.txt",'r')
lines = fileref.readlines()
emotions = []
for line in lines:
    line = line.split()
    emotions.append(line[0])
print(emotions)

​
