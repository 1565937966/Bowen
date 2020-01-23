from easygui import *
# import pandas as pd

msgbox(msg="欢迎进入通讯录系统", title="Information")
choices = ['查询联系人资料', '插入联系人资料', '删除联系人资料', '退出系统']
cont = dict()
email = dict()
while 1:
    choice = choicebox(msg="请选择以下操作:", title="Information", choices=choices)
    if choice == '插入联系人资料':
        fields = ['Name', 'Phone', 'E-mail']
        information = multenterbox(msg="请输入联系方式:", title="Information", fields=fields)
        name = information[0]
        if name in cont and email:
            msgbox(msg="用户已经存在")
        else:
            cont[name] = information[1]
            email[name] = information[2]
            msgbox(msg="联系方式如下:\n" + '\n' + name + '\n' + cont[name] + '\n' + email[name])
            msgbox(msg="保存成功!", ok_button="OK")
            continue
    if choice == "查询联系人资料":
        name = enterbox(msg="请输入您需要查询的名字:")
        if name in cont and email:
            if name in ['翟郡', 'Jun Zhai', 'Zhai Jun']:
                msgbox(msg="Warning!")
                msgbox(msg="前方高能!")
                b = choicebox(msg="您确定您要查询吗?!", choices=['废话,查!', '算了,怂!'])
                if b == '废话,查!':
                    buttonbox(msg="不听话是吧?", choices=("坚决不听!"))
                    msgbox(msg="好!成全你!")
                    buttonbox(msg="惊不惊喜 意不意外?", choices=("惊喜", "意外"), image="C://Users//15659//Desktop//pig2.gif")
                    msgbox("联系方式如下:\n" + '\n' + name + '\n' + cont[name] + '\n' + email[name])
                elif b == '算了,怂!':
                    continue
            else:
                msgbox(msg="联系方式如下:\n" + '\n' + name + '\n' + cont[name] + '\n' + email[name])
                a = choicebox(msg="您是否要修改用户资料?", choices=['Yes', 'No'])
                if a == 'Yes':
                    information = multenterbox(msg="请输入联系方式:", title="Information", fields=fields)
                    name = information[0]
                    cont[name] = information[1]
                    email[name] = information[2]
                    msgbox(msg="修改成功！")
        else:
            msgbox(msg="您输入的用户有误或者不存在,请检查后重新输入!")
            continue
    if choice == "删除联系人资料":
        name = enterbox(msg="请输入您要删除的名字:")
        del (cont[name])
        del (email[name])
        msgbox(msg="删除成功!")
        continue
    if choice == '退出系统':
        msgbox(msg="谢谢使用！")
        break
