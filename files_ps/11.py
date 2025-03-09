with open("old.txt") as f:
    content =f.read()

with open("Rename.txt","w") as f:
    f.write(content)