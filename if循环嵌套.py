temp = input("666:")
guess = temp
if guess == secret:
    print("恭喜你，答对了")
    print("程序正确")
else:
    if guess > secret:
        print("大了大了~~~")
    else:
        print("笑了笑了")
