score = int(input('请输入一个分数:'))
if 100 >= score >= 90:
    print('你的成绩是A')
if 90 > score >= 80:
    print('你的成绩是B')
if 80 > score >= 60:
    print('你的成绩是C')
if 60 > score >= 0:
    print('D')
if score <0 or score >100:
    print("你他娘的输入错误，重新输入")
