# 命令行猜数字游戏（完整版）
"""
功能要求：
① 程序随机生成一个1-100的数字
② 用while循环让用户反复输入猜测；
③ 根据用户输入提示"猜大了"或"猜小了"；
④ 猜对了打印"恭喜你用了X次猜对！"并结束程序；
⑤ 若用户输入"quit"则退出游戏；
⑥ 加入次数限制：最多猜7次，超过则游戏失败并公布答案。
"""
import random

num = random.randint(1,100)
count = 1

while count <= 7:
    guess_num = input("请输入一个猜测的数字：")

    if guess_num == "quit":
        print("用户退出游戏！")
        break

    guess_num = int(guess_num)
    
    if guess_num == num:
        print(f"恭喜你用了{count}次猜对！")
        break
    elif guess_num > num:
        print("猜大了！")
    else:
        print("猜小了！")
        
    count += 1

if count == 8:
    print(f"最多猜7次，游戏失败！数字为{num}")