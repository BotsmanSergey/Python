with open("infile.txt") as infile, open("outfile.txt", "w") as outfile:
    lines = infile.read().splitlines()
    outfile.write("\n".join(reversed(lines)))
    

