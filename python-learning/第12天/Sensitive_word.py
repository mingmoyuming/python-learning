#敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。


# a = "北京是个好天气北京"
# for i in a:
#     if i in "北京":
#         print(True)
#         a = a.replace(i, '*'*len(i))
#     else:
#         print(False)
# print(a)

def sensitive(my_input):
    file = open('filtered_words.txt', 'r', encoding='utf-8')
    f = file.read()
    qg = f.split('\n')
    file.close()
    for i in qg:
        if i in my_input:
            my_input = my_input.replace(i, '*'*len(i))
    print(my_input)
    #print(my_input)


if __name__ == "__main__":
    while True:
        my_input = input("请输入你的值:")
        sensitive(my_input)


#正确答案:
# def filter_words(words):
#     # Read filtered words from file named 'filtered_words.txt'
#     file_object = open('filtered_words.txt', 'r', encoding='utf-8')
#     filtered_words = []
#     for line in file_object:
#         filtered_words.append(line.strip('\n'))
#     file_object.close()
#     # Check if the input words include the filtered words and replace the filtered with '*'
#     for filtered_word in filtered_words:
#         if filtered_word in words:
#             words = words.replace(filtered_word, '*'*len(filtered_word))
#     print(words)
#
# if __name__ == '__main__':
#     while True:
#         input_words = input('Input some words:')
#         filter_words(input_words)