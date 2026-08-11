from awmc import *
from requests import *
import webbrowser
from tkinter import *
from test import *

root=Tk()
root.title('Python AWMC API GUI')
root.geometry('600x600+100+100')

var1=StringVar()#用于落雪OAuth授权码输入
var2=StringVar(value='OAuth')#用于落雪导入模式切换(TOKEN or OAuth),默认为OAuth
var3=StringVar()#用于任何场景下的qrcode输入

def lxoauth():#用于落雪OAuth验证
    global token
    #webbrowser.open('https://maimai.lxns.net/oauth/authorize?response_type=code&client_id=18f1b400-6caa-40a9-bbe7-087d828d61e9&redirect_uri=urn%3Aietf%3Awg%3Aoauth%3A2.0%3Aoob&scope=read_user_profile+read_user_token')
    token=getlxusertoken(var1.get())
    print(token)
def uplx():
    maiulx(token='',qrcode=var3.get(),key=token)#构建exe上传release时要填上awmc api token
def lxchoose():
    lx=Toplevel(root)
    lx.title('请选择落雪上传模式')
    lx.geometry('300x150+100+100')

    oauth=Radiobutton(lx,text='OAuth(推荐)',variable=var2,value='OAuth',font=('等线',10)).place(x=20,y=0)
    token=Radiobutton(lx,text='Token',variable=var2,value='Token',font=('等线',10)).place(x=150,y=0)


Label(root,text='欢迎使用Python AWMC API GUI',font=('等线',20)).place(x=100,y=200)
Button(root,text='上传至落雪查分器',command=lxchoose,font=('等线',10)).place(x=30,y=100)

root.mainloop()