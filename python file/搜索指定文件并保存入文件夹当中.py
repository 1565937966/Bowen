import os
file_root=input("请输入待查找的初始目录:")
vedio=[]
target=['.mp4','.Mp4','.rmvb','.avi']
def serch(file_root,target):
    os.chdir(file_root)
    for eachfile in os.listdir(os.curdir):
        ext=os.path.splitext(eachfile)[1]
        if ext in target:
            vedio.append(os.getcwd()+os.sep+eachfile)
        if os.path.isdir(eachfile):
            serch(eachfile,target)
            os.chdir(os.pardir)
serch(file_root,target)

file=open(os.getcwd()+os.sep+'vedio.txt','w')
file.writelines(vedio)
file.close()

        
        
    
