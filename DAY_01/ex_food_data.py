file = 'food.txt'

kor_food, chinese_food = [],[]
foods={}
kind=''

with open(file, mode='r', encoding='utf8'):
    data = f.readline()
    if not data.index('*'):
        kind = '한식' if data[1:] == '한식' else '중식'
    else:
        if kind == '한식': kor_food.append(data)
        else:
            chinese_food.append(data)

key=''
with open(file, mode='r', encoding='utf8'):
    data = f.readline()
    if not data.index('*'):
        key=data[1:]
        foods[data[1:]] = []
    else:
        foods