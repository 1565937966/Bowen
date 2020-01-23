file_name=input("请输入文件名:")
a=open(file_name,'w')
print("请输入内容【单独输入:'w'保存并退出:")
while True:
    write_content=input()
    if write_content!=':w':
        a.write(write_content)
    else:
        break

a.close()

        
    
