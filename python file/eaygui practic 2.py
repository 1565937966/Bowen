from easygui import *
import os
import os.path
#textbox(msg="文件内容:",title="文本内容",text="hello world",codebox=200)
#fileopenbox(msg="文件夹选项:",title="选择文件夹")
'''
pw=passwordbox(msg="请输入密码",title="登录")
string=" "
for i in pw:
    string=string+str(i)
print(string)
'''
'''
choices=['黄瓜','香蕉','梨','苹果']
choice=multchoicebox(msg="请选择:",title="选择",choices=choices)
print(choice)
'''
file_path=fileopenbox(msg="请选择文件夹:",title="文件打开")
file=os.path.splitext(file_path)[1]
text=[]
if file==".txt":
    with open (file_path) as f:
        '''
        for eachline in f:
            text.append(eachline)
        '''
        text=f.read()
textbox(msg="内容如下:",title="",text=text)


