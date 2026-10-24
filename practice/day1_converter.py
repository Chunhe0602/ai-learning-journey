# 练习 2：公里 → 英里换算器
# input 收到的是文字，算术前必须用 float() 转换成数字

km = input("请输入公里数：")
km = float(km)              # float("42") → 42.0，文字变小数
miles = km * 0.621371

print(km, "公里 =", miles, "英里")
