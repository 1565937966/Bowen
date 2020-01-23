Name=dict()
def newuser():
    name=input("请输入你的用户名:")
    password=input("请输入你的密码:")
    Name[name]=password
    print("注册成功!")
def olduser():
    name=input("请输入你的用户名:")
    if name not in Name:
        print("There is no username")
    else:
        password=input("请输入您的密码:")
        if Name[name]!=password:
            print("密码错误")
            password=input("请输入您的密码:")
        else:
            print("登陆成功！")  
while True:
    x=input("1:新建用户 2:老用户登陆 3:退出系统 请选择:")
    if x=='1':
        newuser()
    if x=='2':
        olduser()
    if x=='3':
        print("谢谢使用")
        break
