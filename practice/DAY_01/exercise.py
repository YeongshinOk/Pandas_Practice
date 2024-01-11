# file = open('hello.txt','w')
# file.write('Hello, world!')
# file.close()



# file = open('hello.txt', 'r')
# s = file.read()
# print(s)
# file.close()
#
# with open('hello.txt','r') as file:
#     s = file.read()
#     print(s)

# with open('hello.txt','w') as file:
#     for i in range(3):
#         file.write('Hello, world! {0}\n'.format(i))

# lines = ['안녕하세요.\n','파이썬\n','코딩 도장입니다.\n']
#
# with open('hello.txt', 'w', encoding='utf8') as file:
#     file.writelines(lines)

# with open('hello.txt', 'r', encoding='utf8') as file:
#     lines = file.readlines()
#     print(lines)

# with open('hello.txt', 'r', encoding='utf8') as file:
#     line = None
#
#     while line != '':
#         line = file.readline()
#         print(line.strip())
#
# with open('hello.txt', 'r', encoding='utf8') as file:
#     for line in file:
#
#         print(line.strip())

# import pickle
#
# name = 'james'
# age = 17
# address = '서울시 서초구 반포동'
# scores = {'korean':90, 'english':95, 'mathematics':85, 'science':82 }
#
# with open('james.p', 'wb') as file:
#     pickle.dump(name, file)
#     pickle.dump(age, file)
#     pickle.dump(address, file)
#     pickle.dump(scores, file)
#
# import pickle
#
# with open('james.p', 'rb') as file:
#     name = pickle.load(file)
#     age = pickle.load(file)
#     address = pickle.load(file)
#     scores = pickle.load(file)
#     print(name)
#     print(age)
#     print(address)
#     print(scores)

# 연습문제
lines = ['anonymously\n','compatiability\n','dashboard\n', 'experience\n', 'photography\n', 'spotlight\n', 'warehous\n']
with open('words.txt', 'w') as file:
    file.writelines(lines)

with open('words.txt', 'r', encoding='utf8') as file:
    count = 0
    words = file.readlines()
    for word in words:
        if len(word.strip('\n')) <= 10:
            count += 1
    print(count)

# 심화문제
lines2 = ['Fortunately\n','however\n',
          'for the reputation of Asteroid B-612\n',
          'a Turkish dictator made a law that his subjects\n',
          'under pain of death\n',
          'should change to European costume. So in 1920 the astronomer gave his demonstration all over again\n',
          'dressed with impressive style and elegance. and this time everybody accepted his report.\n']

with open('words.txt2', 'w') as file2:
    file2.writelines(lines2)

c = []

with open('words.txt2', 'r') as file2:
    line = None
    while line != '':
        lines = file2.readlines()

        for line in lines:
            for word in line.split():

                if 'c' in word:
                    print(word.strip('\n').strip('.'))

