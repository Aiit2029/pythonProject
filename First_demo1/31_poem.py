import re

with open('.poem.txt', 'r+') as f:
    content = f.read()
    target_string = '记得来是春未暮'
    content = re.sub(target_string, "记得来时春未暮", content)

with open('.poem.txt', 'w') as f:
    f.write(content)
    print(content)
