print("******操作")

print("切片")
list = [1,3,5,7,9]
print(list[:2])

print("迭代")
dict = {
  "a": 1,
  "b": 2,
  "c": 3
}
print("遍历 key dict, 遍历 key和value dict.items(), 遍历 value dict.values()")
for k,v in dict.items():
  print(k,v)

print("enumerate() 将list... 转为 索引-元素的形式")
for i, value in enumerate(dict):
  print(i, value)

print("列表生成式")
print([x * y for x in range(1, 11) for y in range(11,12)])