raw_text="Der Hund bellt.Der Hund ist braun."
print(f"原始文本:'{raw_text}'")
cleaned_text=raw_text.strip().lower()
print(f"清洗后文本:'{cleaned_text}'")
no_dots=cleaned_text.replace(".","")
print(f"去掉句点后:'{{no_dots}}'")