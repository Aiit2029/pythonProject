import csv
data = [{'name':'张三','age':25,'city':'广州'},{'name':'李四','age':27,'city':'福州'}]
with open('data.csv','w') as csvfile:
    csv_writer = csv.DictWriter(csvfile, fieldnames=['name','age','city'])
    csv_writer.writeheader()
    csv_writer.writerows(data)
