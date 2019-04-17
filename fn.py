print("******def 方法")

def fn1(a, b):
  if ( a > b):
    print("max: ", a )
    # return a
  else:
    print( "max: ", b )
    # return b

print(fn1(2,5))
print("方法没有return时，返回None")

print("方法可以有多个返回值 此时 返回的为一个元组， 可用多个变量接收" )

def fn2():
  return 1, 3, 5
print(fn2())
c1, c2, c3 = fn2()
print(c1,c2,c3)

# 方法的参数： 一般参数，默认参数，可变参数，命名关键字参数，关键字参数
print("默认参数 def fn(a, b = 2, c = 'a'), 注意参数的顺序")
print("fn(a)", "fn(a, c = 'c')")
print("默认参数不可为可变对象， 因为每次操作后默认参数会被改变，所以需要设为None进行判断")

print("可变参数 被转成元组 *x")
def fn3( a, b=2,*c):
  print("pow a,b:", pow(a,b))
  print(c)
  sum = 0
  for n in c:
      sum = sum + n * n
  print(sum)

print( fn3(5 , 3,  *[3,5] ))
print( fn3(5 , 3,  1,2,3 ))
print("当是参数为list/tuple时，在参数前加* 将起转化为可变参数即可")

print("关键字参数 被转化为dict **x")
def fn4( a, b=2, *c, **d):
  print("pow a,b:", pow(a,b))
  print(c)
  print(d)
dict = { "abc": 1 }
print( fn4(5 , 3, 5,6, **dict ))
print( fn4(5 , 3, *[5,6,7], d = 99 ,abc = 5, ccc = 1 ))

print("命名关键字 *, x,y")
def fn5(*, a, b):
    print(a, b)
print( fn5(a=5, b=4) )
print("命名关键字必须传入参数名称")