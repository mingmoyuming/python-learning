import random

secret = random.randint(1,10)
temp = input ("不妨猜一下我现在想的数字:")
guess = int (temp)

while guess != secret:
    temp = input("对不起，你答错了重新输入吧:")
    guess = int(temp)

    if guess == secret:
        print("恭喜你，大队了")
        print("结束！程序正确!")
    else:
            if guess > secret:
                print ("大了大了")
            else:
                print ("小了小了")

print("测试结束，游戏结束。感谢使用！(　＾∀＾)")
