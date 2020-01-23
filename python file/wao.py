from easygui import *
msgbox(msg="欢迎来到测评中心!",title="")
while True:
    name=enterbox(msg="请输入您要测评者的名字:",title="")
    msgbox(msg="您要测评的名字是："+str(name),title="")
    if name in ['刘大萌','刘永衫','LYS','刘泳衫','Liu Yongshan']:
        msgbox("此人性格：母夜叉.母夜叉即夜叉婆,凶恶的妇人，跟母老虎一样)
        msgbox("谢谢使用,系统听了这个名字已经崩溃!!")
        break
    else:
        msgbox("此人性格：温和,恭谦,懂礼貌,5星好评!")
        continue
