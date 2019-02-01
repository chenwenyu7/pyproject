#culText
import jieba
txt = open("D:/text.txt","r").read()
words = jieba.lcut(txt)
count = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        count[word] = count.get(word,0) + 1
item = list(count.items())
item.sort(key = lambda x:x[1],reverse = True)
for i in range(10):
    word,count = item[i]
    print("{0:<10}{1:>5}".format(word,count))
    
