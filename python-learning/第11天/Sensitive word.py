#敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。


# file = open("filtered_words.txt", 'r', encoding='utf-8')
# f = file.read()
# a = f.split('\n')
# print(a)
# file.close()
# #a = "北京"
# # for i in range(len(f)):
# #     print(f[i])
# # a = str.split("", f)
# # print(a[0])
def review(reviews):
    file = open("filtered_words.txt", 'r', encoding='utf-8')
    f = file.read()
    over = f.split('\n')
    file.close()
    for i in over:
        if i == reviews:
            return True
            break

    # for i in a:
    #     if i == pd:
    #         print("对")
    #         break
    #     else:
    #         print("错")  ##你媽的，為什麼？
    # for i in args:
    #     print(reviews)
    #     if reviews == i:
    #         return True
    #     else:
    #         return False

if __name__ == "__main__":
    py = review("jianggse")
    if py:
        print("Freedom")
    else:
        print("Human Rights")




    #pd = review("北京", a)
    #print(pd)
    # if pd:
    #     print("Human Rights")
    # else:
    #     print("Freedom")

