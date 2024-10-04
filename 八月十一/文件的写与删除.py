import os

with open('床前明月光.txt', 'r', encoding='utf-8') as f1,open('床前明月光.bak', 'w+', encoding='utf-8') as f2:
    old_content = f1.read()
    new_content = old_content.replace('明月','身上')
    f2.write(new_content)
os.remove('床前明月光.txt')
os.rename('床前明月光.bak', '床前明月光.txt')
print(new_content)
