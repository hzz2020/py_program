import string

# 九九乘法表
for i in range(1, 10):
    for j in range(1, 10):
        product = i * j
        if i >= j:
            print('%d*%d=%-02d  ' % (j, i, product), end="")
    print('')

# 统计文章中出现的单词次数
path = 'Walden.txt'
with open(path, 'r') as text:
    words = [raw_word.strip(string.punctuation).lower() for raw_word in text.read().split()]
    words_index = set(words)
    counts_dict = {index: words.count(index) for index in words_index}
for word in sorted(counts_dict, key=lambda x: counts_dict[x], reverse=True):
    print('{} -- {} times'.format(word, counts_dict[word]))

# 列表操作
the_list = [1, 2, 3, 4]
print([i for i in the_list if i > 2])
print([i for i in the_list if i % 2])
print({x: f'item{x ** 2}' for x in (2, 4, 6)})
print(len({x for x in 'hello world' if x not in 'abcdefg'}))

fruit = ['pineapple', 'pear']
fruit.insert(1, 'grape')
print(fruit)

fruit[0:0] = ['Orange']
print(fruit)

for num, ff in enumerate(fruit):
    print(ff, 'is ', num+1)


#
a = [i ** 2 for i in range(1, 10)]
print(a)

b = [i + 1 for i in range(1, 10) if i % 2 == 0]
print(b)

c = {key: value.upper() for key, value in zip(range(1, 10), 'abcdefghijklmn')}
print(c)



