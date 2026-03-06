text_sentense="ich lerne Python und Python ist toll"
word_list=text_sentense.split()
print("切分后的单词列表:",word_list)
word_count={}
word='ich'
if word in word_count:
    word_count[word]=word_count[word]+1
else:
    word_count[word]=1
print("处理完'ich'后，字典变为:",word_count)
word='lerne'
if word in word_count:
    word_count[word]=word_count[word]+1
else:
    word_count[word]=1
print("处理完'lerne'后，字典变为：",word_count)
word_count={}
for word in word_list:
    if word in word_count:
        word_count[word]=word_count[word]+1
    else:
        word_count[word]=1
    print("最终的词频统计结果是：",word_count)