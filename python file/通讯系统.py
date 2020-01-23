print("    欢迎进入通讯录系统    ")
print("    1:查询联系人资料     ")
print("    2:插入联系人资料     ")
print("    3:删除联系人资料     ")
print("    4:退出系统     ")
contr=dict()
while 1:
    x=int(input("请输入相关指令:"))
    if x==1:
        name=input("请输入联系人姓名:")
        if name in contr:
            print(name+':'+contr[name])
        else :
            print("您输入的用户是空")
    if x==2:
        name=input("请输入联系人姓名:")
        number=input("请输入电话号码:")
        contr[name]=number
        #if name in contr:
        print("您输入的名字已保存成功:"+name+contr[name])
        a=input("是否修改用户资料(yes/no):")
        if a=='yes':
            newnumber=input("输入用户联系电话:")
            contr[name]=newnumber
            print("修改成功!")
    if x==3:
        name=input("请输入要删除的名字:")
        del(contr[name])
        print("删除成功！")
    if x==4:
        print("谢谢使用!")
        break

        
            
        
        
