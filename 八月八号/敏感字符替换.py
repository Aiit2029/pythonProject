import re

def main():
    sentence = input("请输入你想说的话(注意文明用语哦)：")
    pure = re.sub('[11]','*',sentence,re.I)
    print(pure)

if __name__ == '__main__':
    main()