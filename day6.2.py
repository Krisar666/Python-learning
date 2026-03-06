text="Apfel Apfel Kirsche"

words=text.split()
print(words)

freq={}

for word in words:
    if word in freq:
        freq[word]=freq[word]+1
    else:
        freq[word]=1

        print(freq)