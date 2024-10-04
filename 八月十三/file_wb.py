with open('file_wb_open.txt', 'w') as f:
    f.write('hello world\n')
    f.write('helloworld\n')
    f.write('hello world')
    f.seek(9)
    f.write('Fakerword')