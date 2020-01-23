import os
a=dict()
all_files=os.listdir(os.curdir)
for eachfile in all_files:
    if os.path.isdir(eachfile):
        a.setdefault('文件夹',0)
        a['文件夹']+=1
    else:
        ext=os.path.splitext(eachfile)[1]
        a.setdefault(ext,0)
        if ext in a:
            a[ext]+=1
for each_type in a.keys():
    print("该文件夹中一共有类型位%s的文件%d个"%(each_type,a[each_type]))
    
        
        
