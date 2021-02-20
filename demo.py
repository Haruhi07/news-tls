import json

f = open("log.txt", "r")
for line in f:
    print(line)
    data = json.loads(line)
    print(data)
    for x,y in data:
        print(x,y)
f.close()