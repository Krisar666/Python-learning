german_dict={}
german_dict["Hund"]="Der"
german_dict["Katze"]="Die"
print(german_dict["Hund"])
german_dict["Hund"]="Der(Animal)"
print(german_dict["Hund"])
text="ja nein ja"
words=text.split()
counts={}

for w in words:
    if w in counts:
        counts[w]=counts[w]+1
    else:
        counts[w]=1
print(counts)