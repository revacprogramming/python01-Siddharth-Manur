# Dictionaries

filename = "dataset/mbox-short.txt"
filehandle = open(filename)
dt = dict()

for line in filehandle:
    if len(line) < 3 or not line.startswith("From "): continue
    words = line.strip().split()
    word = words[1]
    dt[word] = dt.get(word,0) + 1

sender = None
no_of_messages = None

for name,count in dt.items():
    if no_of_messages == None or count > no_of_messages :
        sender = name
        no_of_messages = count

print(sender,no_of_messages)