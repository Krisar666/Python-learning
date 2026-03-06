def clean_word(w):
    result=w.strip().lower()
    print(f"清洗前:'{w}'->清洗后:'{result}'")

clean_word(" Python")
clean_word("GERMAN")