import pickle
file=open("record.txt")
boy=[]
girl=[]
count=0
for each_line in file:
    (role,line_spoken)=each_line.split(':')
    if each_line[:6]!='====':
        if role=='小甲鱼':
            boy.append(line_spoken)
        if role=='小客服':
            gilr.append(line_spoken)
    else:
        count+=1
        boy_file=open("E://boy's file"+str(count)+".txt",'wb')
        pickle.dump(boy,boy_file)
        gilr_file=open("E://girl's file"+str(count)+".txt",'wb')
        pickle.dump(gilr,gilr_file)
        boy=[]
        gilr=[]
        boy_file.close()
        girl_file.close()
file.close()
count+=1
boy_file=open("E://boy's file"+str(count)+".txt",'wb')
pickle.dump(boy,boy_file)
gilr_file=open("E://girl's file"+str(count)+".txt",'wb')
pickle.dump(gilr,gilr_file)
boy_file.close()
girl_file.close()


        
        
    
