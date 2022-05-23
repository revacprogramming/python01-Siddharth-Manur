# Tuples

filename = "dataset/mbox-short.txt"
handle = open(filename)
d=dict()
for line in handle:
	if len(line) < 3 or not line.startswith("From "): continue
	words = line.strip().split()
	word = words[5]
	time = word.split(':')
	hours = time[0]
	d[hours] = d.get(hours,0) + 1
for key, val in sorted(d.items()):
    print(key, val)
