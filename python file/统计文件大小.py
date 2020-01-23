import os
all_files=os.listdir(os.curdir)
a=dict()
for eachfile in all_files:
    if os.path.isfile(eachfile):
        file_size=os.path.getsize(eachfile)
        a[eachfile]=file_size
for eachkey in a.keys():
    print("文件%s的大小是:[%s Bytes]"%(eachkey,a[eachkey]))
    
