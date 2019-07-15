
file = open('filtered_words.txt', 'r', encoding='utf-8')
f = file.read()
qg = f.split('\n')
file.close()
for i in qg:
    print(i)