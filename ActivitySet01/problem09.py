# Lists

filename = "dataset/romeo.txt"
fh = open(filename)
c=fh.readlines()
words=list()
for i in c:
    for j in i.split():
        if j not in words:
            words.append(j)
print(sorted(words))