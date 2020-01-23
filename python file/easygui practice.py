from easygui import *
import sys
import os
'''
version= "Bowen's Computer"
choice=['确定','取消']
button=buttonbox("你确认离开吗?",title=version,choices=choice)
msgbox(msg=button,title="yoyoyo")
'''

'''
version="Instrcution"
var=ccbox(msg="Would you like to continue?",title=version)
#msgbox(msg=var,title=version)
if var==1:
    msgbox(msg="You continued",title=version)
elif var==0:
    msgbox(msg="You Exit",title=version)
    sys.exit(0)
'''
'''
while 1:
    version=" Choices "
    choices=['Apple','Banana','Pineapple']
    var=choicebox(msg="Please make a choice",title=version, choices=choices)
    if var==choices[0]:
        msgbox(msg=var,title=version)
    elif var==choices[1]:
        msgbox(msg=var,title=version)
    elif var==choices[2]:
        msgbox(msg=var,title=version)
    button=buttonbox(msg="Leave?",title=version,choices=("Yes","No"))
    if button=="No":
        continue
    if button=="Yes":
        break
    msgbox("Thanks for choosing",title=version)
'''

title="Compare"
while True:
    button=buttonbox(msg="魔镜魔镜，告诉我这个世界谁最美",title=title,choices=["刘大萌","甘露"])
    msgbox(msg="你选择了:"+button, title=title)

    if button=="甘露":
        msgbox(msg="恭喜你选对了",title=title)
        break
    elif button=="刘大萌":
        msgbox(msg="不好意思,你估计是眼瞎了",title=title)
        continue

#press=passwordbox(msg="please enter password",title="Guess the\number")
#msgbox(msg=press,title="Number")
'''
field_list=['*用户名','*手机号','QQ','*E-mail']
value_list=['','','','','']
multenterbox(msg="带*号的必填",title="资料搜集",fields=field_list,values=value_list)
'''

