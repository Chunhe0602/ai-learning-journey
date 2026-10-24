# 第 1 课练习 3：input 让程序听你说话

name = input("你叫什么名字？")
city = input("你住在哪个城市？")

print("你好，", name)
print("欢迎来自", city, "的朋友")

# 注意：input 收到的永远是文字（str），哪怕输入的是数字
age = input("你今年多大？")
print("age 的类型是：", type(age))
