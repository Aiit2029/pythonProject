class House(object):

    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_dir = []

    def __str__(self):

        return (f'房间户型：{self.house_type},\n'
                f'房间面积：{self.area},\n'
                f'房间剩余面积{self.free_area},\n'
                f'房间家具列表：{self.item_dir}')

    def add_item(self, item):
        print(f'要添加：{item}')
        if float(self.free_area) -float(item.area) >= 0 :
            self.free_area = float(self.free_area) -float(item.area)
            self.item_dir.append(f'{item.name}')
        else:
            print(f'房间剩余面积还有：{self.free_area},{item.name}需要占地面积{item.area}\n请合理安排房间剩余面积')


class HouseItem(object):
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return f'[{self.name}]:{self.area}'


house1 = House('大平层', '700')

bed = HouseItem('席梦思', '400')
chest = HouseItem('衣柜', '200')
table = HouseItem('餐桌', '200')

house1.add_item(bed)
house1.add_item(chest)
house1.add_item(table)
print(house1)
