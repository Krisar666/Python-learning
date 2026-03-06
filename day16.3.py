def is_long_word(word):
    if len(word)>5:
        return True
    else:
        return False
words=["ich","Student","Uni","Bibliothek"]

for w in words:
    if is_long_word(w):
        print(f"Long word detected:{w}")

    else:
        print(f"Short word:{w}")
        