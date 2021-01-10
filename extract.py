import json
x = 0
y = 0
username = input("Username to filter for: ")

output = open("output.txt", "a")

with open('data.txt') as json_file:
    data = json.load(json_file)
    for p in data['messages']: #Inside messages list
        for y in range(5): # Cycle through sub lists
            lst = p[y]   # inside p, list 0
            author = lst["author"]["username"]
            if lst["author"]["username"] == username:
                print(lst["content"])
                print(lst["content"], file=output)
            else:
                continue
        x = x + 1
output.close()

lines_seen = set() # holds lines already seen
outfile = open("output2.txt", "w")
for line in open("output.txt", "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()
