"""------小游戏------"""
temp = input("不妨猜一下我现在想的什么数字：")
guess = int(temp)
if guess == 8:
        print("恭喜你答对了！")
        print("说明程序正确")
else:
    print("猜错了，我想说的是8")
