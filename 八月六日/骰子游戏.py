# 两粒骰子
__author__ = '金不换'
__date__ = '2024_08_06'

import random




        # self.roll = random.randint(1,6)
        # 骰子点数:1-6


def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)

# 次数：
chance = 1
firstdice = None
while True:
    start1 = input('请输入游戏开始：')
    while start1 == '游戏开始':
        sum = roll_dice()

        # 骰子点数相加： 第一次 7 or 11 玩家赢
        if chance == 1:
            if sum == 7 or sum == 11:
                print(f'玩家赢了,点数和是{sum}')
                break
            # 骰子点数相加：第一次时  2 ，3，12 庄家赢
            elif sum == 2 or sum == 3 or sum == 12:
                print('庄家赢了')
                break
            else:
                # 记录玩家摇出的第一次的点数
                firstdice = sum
                print(f'记录了第{chance}次的骰子数：[{firstdice}]')
                print('现在将进行下一次投掷骰子')
                start2 = input('请输入游戏继续：')
                while start2 == '游戏继续':
                    start2 = None
                    chance += 1
                    sum = roll_dice()
        # 投资点数相加：  7 无条件赢
                    while chance >= 2:
                        if sum == 7:
                            print('玩家包赢的，真棒')
                            break
                        # 如果 后续次数摇出第一次除了 2，3，12 外的点数  玩家胜
                        elif firstdice == sum:
                            print(f'第一次的数为{firstdice}，和第{chance}次的数{sum}相等')
                            print('玩家：结果我第一，又强又努力')
                            break
                        else:
                            print('继续')
                            break
                else:
                    start2 = input('请输入游戏继续：')
                    continue
                continue











    # while True  一直到分出胜负
