import os
x=input("请输入要查找的初始目录:")
y=input("请输入要查找的目标文件:")
def serchfile(x,y):
    os.chdir(x)
    for eachfile in os.listdir(os.curdir):
        if eachfile==y:
            print(os.getcwd()+os.sep+eachfile)
        if os.path.isdir(eachfile):
            serchfile(eachfile,y)
            os.chdir(os.pardir)#?
serchfile(x,y)
