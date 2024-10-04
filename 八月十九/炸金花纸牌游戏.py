#  一副扑克牌52张，
import random

#  四个色（spade，heart，diamond,club），
color_list = ['spade','heart','diamond','club']
#  每个色13张，从A到K
faces_list =['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
play_names = input('请输入玩家姓名，用空格隔开').split()

#如果发出一张牌，那么牌库中就不在存在这张牌
all_cards = [f'{color}{face}' for color in color_list for face in faces_list ]
# 允许输入多个玩家姓名 ，不限制个数，
for name in play_names:
    cards = random.sample(all_cards,3)
    for card in cards:
        all_cards.remove(card)
    print(f'{name}的牌是{cards}')

# 为每个玩家随机生成3张牌