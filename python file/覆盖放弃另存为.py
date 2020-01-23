from easygui import *
import os.path
import os
def gui():
    choices=['Cover','Cancel','Saved as..']
    click=buttonbox(msg="files changed,make a choice:",title="warnning!",choices=choices)
    return click
    
file_path=fileopenbox(msg="Choose a file",title="File",default=".txt")
with open(file_path) as old_file:
    title=os.path.basename(file_path)
    msg=("the content in %s:"%(title))
    text=old_file.read()
    text_after=textbox(msg=msg,title=title,text=text)
    if text!=text_after:
        choice=gui()
        if choice=='Cover':
            with open (file_path,'w') as old_file:
                old_file.write(text_after)
            msgbox(msg="Finished!",title="Covered file")
        if choice=='Cancel':
            pass
        if choice=='Saved as..':
            another_path=filesavebox(msg="Choose",title="Choose",default='.txt')
            with open(another_path,'w') as new_file:
                new_file.write(text_after)


                
                
   
        
    
    
