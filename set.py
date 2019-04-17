print("******set{}集合")

print("set 无序，无重复元素的集合， 可做交集等& |")
a = set([1,2,3])
b = set([3,2,5,4])
print(a,b)
print("a & b", a & b, "a | b", a | b)

print("add, remove 操作set")
a.add("a")
b.remove(4)
print(a,b)

d = {
  "a": (1, 2, 3),
  "b": (1, [ 2, 3 ])
}

print(set(d))
print("set 只存dict的key值")