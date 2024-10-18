fname = input("Enter File: ")
if len(fname) < 1 :
    fname = "clown.txt"
handle = open(fname)
counter = dict()
for line in handle:
    line = line.rstrip()
    words = line.split()

    for eachword in words:
        counter[eachword] = counter.get(eachword,0) + 1

#print(counter.items())

#print(sorted(counter.items()))

tmp = dict()
newlist = list()
for k,v in counter.items():
    tup = (v,k)
    newlist.append(tup)
    #print(tup)
#print(newlist)
cool = sorted(newlist, reverse=True)
#print(cool)
for v,k in cool[:5]:
    print(k,v)
