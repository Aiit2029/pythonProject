import openpyxl

# 打开 Excel 文件
workbook = openpyxl.load_workbook('test.xlsx')

# 选择要操作的工作表
sheet = workbook.active

# 提取数据并消除 None
data = []

for row in sheet.iter_rows(values_only=True):
    new_row = [cell for cell in row if cell is not None]
    data.append(new_row)

# # 打印处理后的数据
for row in data:
    print(row)

