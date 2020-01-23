import os
import os.path
director=os.chdir("C://Users//15659//Desktop//CS//python file")
file=os.listdir(director)
for each_file in file:
    name=os.path.splitext(each_file)[1]
    if name=='.txt':
        os.remove(each_file)
    else:
        pass
    
