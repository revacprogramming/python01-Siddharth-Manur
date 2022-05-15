# Files

filename = "dataset/mbox-short.txt"
fh = open(filename)
count=0
result=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    l=line.find(':')
    s=line[l+1:]
    num=float(s)
    result=result+num
    count=count+1
avg=result/count
print("Average spam confidence:",avg )
