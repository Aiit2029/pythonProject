# coding=GBK
import random
randomizer = random.randint(1, 100)
count = 10
while count > 0:
    temp = input("Enter a number:")
    if temp.isdigit():
        guess = int(temp)
        if guess == randomizer:
            print('you are right(对了)')
            break
        elif guess > randomizer:
            print('your guess is too big(大了)')
        elif guess < randomizer:
            print('your guess is too small(小了)')
        count = count - 1
        print('you have ' + str(count) + ' chances to guess the result')
