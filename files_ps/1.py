f=open("poems.txt")
content=f.read()
if("Twinkle" in content):
    print("word is present")
else:
    print("not present")
f.close()