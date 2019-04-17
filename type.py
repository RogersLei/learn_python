print("*******基础类型：整数，浮点数，字符串，布尔值， 空值None")

a = 3
b = 3.4
c = "a"
d = 0x10
e = None

print( '%5d' % a, '%.2f' % a, '%s' % c, '%d' % d, e )
print('{0}, {1}'.format('a',b))

print("*****list[]可变 tuple()不可变")

list =  ['Michael', 'Bob', 'Tracy']
print('list',list, len(list), list[0])

list.append('last')
list.pop()
list.insert(1, "insert")
list.pop(1)

tuple = (1,)
print('tuple', tuple)

# 如何进行类型转化
print("2",int("2"), 2 == int("2"))
# int(), float(), str(), bool()

# 如何进行类型检查
print(isinstance(2.4,(str, int)))