print("*******判断/循环")

age = 2


if +age >= 18:
  print('adult')
else:
  print('teenager')

# elif:


# 循环1.  for x in y
print("for 循环")
for i in list(range(5)):
  print(i)
# range() 生成一个整数序列   list() 将序列转为list类型

# 循环2. while
print("while 循环")
n = 0
while( n < 2):
  n += 1
  print(n)

print("break, continue 用来跳出循环")