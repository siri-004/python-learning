with open("log.txt") as f:
    lines= f.readlines()
lineno=1
for line in lines:
    if("python" in line):
            print(f"Yes it is present in {lineno}")
            break
    lineno +=1
else:
        print("Not present")