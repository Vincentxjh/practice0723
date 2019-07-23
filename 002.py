#第二个练习

#给定身高和体重，并显示
height = 1.76
print("您的身高：" + str(height) + "m")
weight = 68
print("您的体重：" + str(weight) + "kg")

#计算BMI，并显示
bmi = weight/(height * height)
print("您的BMI指数为：" + str(bmi))

#根据BMI判断身材是否合理
if bmi < 18.5:
    print("您的体重过轻，请增加营养 ～＠_＠～ ")
if bmi >= 18.5:
    print("您的体重在正常范围，请保持 ～＾_＾～ ")
if bmi >= 24.9:
    print("您的体重过重，请注意 ～＠_＠～　")
if bmi >= 29.9:
    print("您的体重超重，请减肥 ～＠_＠～ ")



