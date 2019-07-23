#第九个练习-模拟手机充值场景

money = int(input("欢迎使用XXX充值服务，请输入您要充值的金额："))
t = int(input("您输入的充值金额为：" + str(money) +"元，确认充值请按1，取消充值请按2: "))
if t==1:
    print("充值成功，您本次充值金额为" + str(money) + "元。")
elif t==2:
    print("取消成功，您本次未充值。")
else:
    print("对不起，您的输入有误，请重新输入。")