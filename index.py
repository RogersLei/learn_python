print("*******基础类型")

a = 3
b = 3.4
c = "a"
d = 0x10

print( '%5d' % a, '%.2f' % a, '%s' % c, '%d' % d )
print('{0}, {1}'.format('a',b))

print("*****list[] tuple()")

list =  ['Michael', 'Bob', 'Tracy']
print(list, len(list), list[0])

list.append('last')
list.pop()
list.insert(1, "insert")
list.pop(1)