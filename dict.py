print("******dict{}字典")
d = {
  'a': 1,
  'b': 2
}

print(d['a'])

print("通过以下方式 避免key不存在的错误")
print("1. in ")
print("a" in d, "c" in d)
print("2. get() 获取key所在位置， 若不存在则返回None， 可指定不存在时返回值")
print(d.get("b"), d.get("c"), d.get("c", -1) )

print("删除一个key/value")
d.pop("a")
print(d)