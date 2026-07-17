minhastring="Hello, World! "
novastring=minhastring.\
    replace("o", "A").\
    lower().\
    replace("!","").\
    split(" ")[1]
print(novastring)