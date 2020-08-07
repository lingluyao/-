
#图形界面
from tkinter import *

#from PIL import ImageTk,Image
import compileclass
def Reset(entry1,txt,txt1):
	entry1.delete(0,END)
	txt.delete(0.0,END)
	txt1.delete(0.0,END)
	compileclass.teststr=['null']*10# def Reset():
	entry1.delete(0,END)
	txt.delete(0.0,END)
	txt1.delete(0.0,END)
def Calculate():
	mygui=Tk()
	mygui.title('计算器')
	# image=Image.open('01.gif')
	# back_ground=ImageTk.PhotoImage(image)
	# w=back_ground.width()
	# h=back_ground.height()
	# mygui.geometry('%dx%d+0+0' % (w,h))
	swidth,sheight=mygui.maxsize()#获取屏幕宽度,高度
	cen_x=(swidth-490)/2;#计算中心坐标
	cen_y=(sheight-500)/2;

	mygui.geometry('%dx%d+%d+%d' %(490,500,cen_x,cen_y))

	#mygui.geometry('490x500')
	bglabel=Label(mygui,bg='#B5B5B5')
	# bglabel=Label(mygui,image=back_ground)
	bglabel.place(x=0,y=0,relwidth=1,relheight=1)

	label1=Label(mygui,text='请输入式子:',padx=15,pady=2,font=('微软雅黑 12'))
	label1.place(x=10,y=10)

	entry1=Entry(mygui)#输入式子
	entry1.place(x=10,y=50,relwidth=0.25,relheight=0.06)


	txt=Text(mygui,bd=5,bg='#E4E3DF',width=30,height=30,font=('微软雅黑 12'))
	txt.place(x=10,y=100,relwidth=0.5,relheight=0.7)
	txt.tag_config("tag_1",foreground='red')#设置tag
	txt.tag_config("tag_2",foreground='blue')

	txt1=Text(mygui,width=30,height=30,font=('微软雅黑 12'))
	txt1.place(x=300,y=50,relwidth=0.25,relheight=0.05)

	button1=Button(mygui,text='确定',width=7,font=('微软雅黑 10'),\
		command=lambda:compileclass.main_pro(entry1.get(),txt,txt1))
	button1.place(x=200,y=10)
	button2=Button(mygui,text='重置',width=7,font=('微软雅黑 10'),command=lambda:\
		Reset(entry1,txt,txt1))
	button2.place(x=200,y=50)

	label2=Label(mygui,text='结果:',padx=15,pady=2,font=('微软雅黑 12'))
	label2.place(x=300,y=10)
	txt1=Text(mygui,width=30,height=30,font=('微软雅黑 12'))
	txt1.place(x=300,y=50,relwidth=0.25,relheight=0.05)
	
	mygui.mainloop()

if __name__ == '__main__':
	Calculate()


