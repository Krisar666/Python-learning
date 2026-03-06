while True:
    sentence=input("Bitte gib einen deutschen Satz ein:")
    print("You entered:",sentence)
    break

while True:
    sentence=input("Satz eingeben(quit zum Beenden):")

    if sentence=="quit":
        print("Tschüss!")
        break

    print("Du hast geschreiben:",sentence)
    
    words=sentence.lower().split()
    print("Wöter:",words)
    print("Anzal der Wöter:",len(words))
