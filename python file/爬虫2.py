from urllib import request as r
import easygui as es
import sys
fields=["宽","高"]
choice=es.multenterbox(msg="请填写猫的尺寸",title="下载猫的图片",fields=fields,values=[])
url="http://placekitten.com/"+choice[0]+"/"+choice[1]
response=r.urlopen(url)
url=response.read()
save_path=es.filesavebox(default='.jpg')
with open(save_path,"wb") as f:
    f.write(url)






