from awmc import *
from requests import *
import webbrowser
from tkinter import *
from test import *
import time

root=Tk()
root.title('Python AWMC API GUI')
root.geometry('600x600+100+100')

var1=StringVar()#用于落雪OAuth授权码输入
var2=StringVar(value='OAuth')#用于落雪导入模式切换(TOKEN or OAuth),默认为OAuth
var3=StringVar()#用于任何场景下的qrcode输入
var4=StringVar()#用于落雪Token输入

def lxoauth():#用于落雪OAuth验证
    global token
    #webbrowser.open('https://maimai.lxns.net/oauth/authorize?response_type=code&client_id=18f1b400-6caa-40a9-bbe7-087d828d61e9&redirect_uri=urn%3Aietf%3Awg%3Aoauth%3A2.0%3Aoob&scope=read_user_profile+read_user_token')
    token=getlxusertoken(var1.get())
    print(token)
    lx2.destroy()
    uplx()

def lxtoken():
    global token
    token=var4.get()
    uplx()
    lx2.destroy()
    
def uplx():
    maiunow=Toplevel(root)
    maiunow.title('请输入二维码文本')
    maiunow.geometry('300x150+100+100')
    def postlx():
        maiulx(token='',qrcode=var3.get(),key=token)#构建exe上传release时要填上awmc api token
        maiunow.destroy()
    Entry(maiunow,textvariable=var3,width=40).place(x=0,y=0)
    Button(maiunow,text='确定',command=postlx,font=('等线',10)).place(x=20,y=40)
    
def lxchoose():
    global lx
    lx=Toplevel(root)
    lx.title('请选择落雪上传模式')
    lx.geometry('300x150+100+100')

    oauth=Radiobutton(lx,text='OAuth(推荐)',variable=var2,value='OAuth',font=('等线',10)).place(x=20,y=0)
    token=Radiobutton(lx,text='Token',variable=var2,value='Token',font=('等线',10)).place(x=150,y=0)
    Button(lx,text='确定',command=lxidea,font=('等线',10)).place(x=100,y=100)
def lxidea():
    global lx2
    lx.destroy()
    if var2.get()=='OAuth':
        webbrowser.open('https://maimai.lxns.net/oauth/authorize?response_type=code&client_id=18f1b400-6caa-40a9-bbe7-087d828d61e9&redirect_uri=urn%3Aietf%3Awg%3Aoauth%3A2.0%3Aoob&scope=read_user_profile+read_user_token')
        lx2=Toplevel(root)
        lx2.title('请填入授权码')
        lx2.geometry('300x150+100+100')

        Label(lx2,text='请填入落雪授权码',font=('等线',13)).place(x=0,y=0)
        Entry(lx2,textvariable=var1,width=40).place(x=0,y=50)
        Button(lx2,text='确认',command=lxoauth,font=('等线',10)).place(x=20,y=100)
    if var2.get()=='Token':
        lx2=Toplevel(root)
        lx2.title('请填入落雪Token')
        lx2.geometry('300x150+100+100')
        
        Label(lx2,text='请填入落雪Token',font=('等线',13)).place(x=0,y=0)
        Entry(lx2,textvariable=var4,width=40).place(x=0,y=50)
        Button(lx2,text='确认',command=lxtoken,font=('等线',10)).place(x=20,y=100)

Label(root,text='欢迎使用Python AWMC API GUI',font=('等线',20)).place(x=100,y=200)
Button(root,text='上传至落雪查分器',command=lxchoose,font=('等线',10)).place(x=30,y=100)

root.mainloop()