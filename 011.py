#第十一个练习-根据父母身高预测儿子的身高

#提示输入父母的升高，并显示
fat_height = float(input("请输入父亲的身高（单位m）："))
mat_height = float(input("请输入母亲的身高（单位m）："))

#计算推测儿子的身高，并显示
son_height = (fat_height + mat_height) * 0.54
print("预测儿子的身高为：" + str(son_height) + "m。")