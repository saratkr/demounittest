import json

line1 = '{"a": 3, "expected": 2 }'

for line in open("file1.txt"):

    #print (line)
    print (json.loads(line))

with open("file1.txt", "r") as content:
    pass
 # print(json.loads(content.read()))

# with open('file1.txt') as f:
 #    for line in f:
 #        print(json.loads(line))