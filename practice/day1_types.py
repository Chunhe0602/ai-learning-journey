# 第 1 课练习 2：数据类型

text = "你好"        # str 字符串：文字
number = 100         # int 整数
price = 3.5          # float 小数
is_ok = True         # bool 布尔：是 / 否

# type() 是照妖镜：查看数据类型
print(type(text))
print(type(number))
print(type(price))
print(type(is_ok))

# 数字类型可以做运算
print(number + 50)
print(price * 2)

# 文字类型可以拼接
print(text + "，世界")

# 试试看：文字加数字会怎样？（取消下面注释跑一次，再注释回去）
print(text ,number)
