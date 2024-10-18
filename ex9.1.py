fname = input("Enter File: ")
if len(fname) < 1 :
    fname = "clown.txt"
handle = open(fname)
counter = dict()
for line in handle:
    line = line.rstrip()
    #print(line)
    words = line.split()
    #print(words)
    for eachword in words:
        #print(eachword)
        #print("!!",eachword,counter.get(eachword,-99))

        #oldcount = counter.get(eachword,0)
       # print(eachword,"old",oldcount)
       # newcount = oldcount + 1
        #counter[eachword] = newcount

        counter[eachword] = counter.get(eachword,0) + 1
        #print(eachword,"new",counter[eachword])



       # if eachword in counter:
            #counter[eachword] = counter[eachword] + 1
            #print("got it")
        #else:
         #   counter[eachword] = 1
            #print("!NEW WORD DETECTED!")
        #print(counter[eachword],eachword+"s")
        #print(eachword, counter[eachword])
#print(counter)
largest = -1
bigword = None
for k,v in counter.items():
    #print(k,v)
    if v > largest:
        largest = v
        bigword = k

print("Done", bigword, largest)
