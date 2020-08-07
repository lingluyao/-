#主代码
from tkinter import *
import autosystem #用于将其他进制转换为十进制数
import SStack
operatered="+-*/（）#"
index={'+':0, '-':1, '*':2, '/':3, '（':4, '）':5,6:6, '#':7} #用于判断语法分析中每个符号之间的大于小于等于关系
#         +   -   *   /   (   )   i   #
opg=[   ['>','>','<','<','<','>','<','>'],#+
		['>','>','<','<','<','>','<','>'],#-
		['>','>','>','>','<','>','<','>'],#*
		['>','>','>','>','<','>','<','>'],#/
		['<','<','<','<','<','=','<','0'],#(
		['>','>','>','>','0','>','0','>'],#)
		['>','>','>','>','0','>','0','>'],#i
		['<','<','<','<','<','0','<','=']   ]##
teststr=['null']*10
semstr=['null']*10
flag=[0]*3#flag[0]判断词法分析是否正确，flag[1]判断语法分析是否正确

def is_decnumber(x):#是否为十进制
	if x>='1' and x<='9':
		return True
	return False;

def is_hexnumber(x):#是否为十六进制
	if x>='a'and x<='f' or x>='0'and x<='9':
		return True
	return False

def is_octnumber(x):#是否为八进制
	if x>='0' and x<='7':
		return True
	return False

#后缀式计算结果
def Answer(suffix,j):#后缀式计算结果
	answer_stack=SStack.Stack()
	a1,a2=0.0,0.0#用于存操作数
	for i in range(j):
		if operatered.find(str(suffix[i]))>=0:
			a1=answer_stack.peak()
			answer_stack.pop()
			a2=answer_stack.peak()
			answer_stack.pop()
			if suffix[i]=='+':
				a1=float(a1)+float(a2)
			elif suffix[i]=='-':
				a1=float(a2)-float(a1)
			elif suffix[i]=='*':
				a1=float(a1)*float(a2)
			elif suffix[i]=='/':
				a1=(float(a2)/float(a1))
			answer_stack.push(a1)
		else:
			answer_stack.push(suffix[i])
	print(answer_stack.peak())
	return answer_stack.peak()
#中缀式转后缀式
def SEMANTICS(resulttxt):
	suffix=[0]*10
	i,j=0,0
	symbol_stack=SStack.Stack()
	result_stack=SStack.Stack()
	for i in range(cntt+1):
		if semstr[i]=='+' or semstr[i]=='-' or semstr[i]=='*' or semstr[i]=='/':#遇到操作符
			if symbol_stack.is_empty() or symbol_stack.peak()=='（':#栈为空，或者栈顶元素为‘（’，入栈
				symbol_stack.push(semstr[i])
			elif opg[ index[ semstr[i] ] ][ index[ symbol_stack.peak() ] ]=='>':#如果元素优先级大于栈顶元素,入栈
				symbol_stack.push(semstr[i])
			elif opg[ index[ semstr[i] ] ][ index[ symbol_stack.peak() ] ]=='<' or\
			opg[ index[ semstr[i] ] ][ index[ symbol_stack.peak() ] ]=='=':
				temporary=symbol_stack.peak()#取出栈顶元素
				symbol_stack.pop()    #将栈顶元素删除
				result_stack.push(temporary) #将元素压入
				while opg[ index[ semstr[i] ] ][ index[ symbol_stack.peak() ] ]=='<' or\
				opg[ index[ semstr[i] ] ][ index[ symbol_stack.peak() ] ]=='=':#直到优先关系为大于的时候
					temporary=symbol_stack.peak()
					symbol_stack.pop()
					result_stack.push(temporary)
		elif semstr[i]=='（':
			symbol_stack.push(semstr[i])
		elif semstr[i]=='）':#直到找到‘（’，将这之前的元素都压入结果栈中，
			while symbol_stack.peak()!='（' :
				print(symbol_stack.size())
				temporary=symbol_stack.peak()
				symbol_stack.pop()
				result_stack.push(temporary)
				print(symbol_stack.size())
			symbol_stack.pop()#最后将栈顶的‘(’删除
		else:#为操作数
			result_stack.push(semstr[i])
	while symbol_stack.is_empty()==False:#将s1中剩余的运算符依次弹出并压入s2
		temporary=symbol_stack.peak()
		symbol_stack.pop()
		result_stack.push(temporary)
	while result_stack.is_empty()==False:
		suffix[j]=result_stack.peak()
		result_stack.pop()
		j+=1
	suffix1=[0]*j
	for k in range(j):
		suffix1[k]=suffix[j-k-1]
	print(suffix1,j)
	ans=Answer(suffix1,j)
	#print(ans)
	resulttxt.insert(END,ans)#print(Answer(suffix1,j))

def show():#可要可不要，用于测试，但是此函数中的num用于语法分析中，为待分析的算式最后加上#，需要移到其他地方
	print('flag:',flag[0],'cnt:',cntt)
	global num
	num=cntt
	num+=1
	teststr[num]='#'#为了算符优先文法的分析，在每个需要分析的最后加上#
	print(teststr)
	print(semstr)

def grammer(txt):#算符优先表的初始化
	global opg
	test=['0']*100
	i,k=0,0
	test[k]='#'
	while i<=num:
		print(i,k)
		print(test[k],opg[ index[test[k]] ][ index[teststr[i]] ],teststr[i])
		if opg[ index[test[k]] ][ index[teststr[i]] ]=='<' or opg[ index[test[k]] ][ index[teststr[i]] ]=='=':
			k+=1
			test[k]=teststr[i]
			i+=1
		elif opg[ index[test[k]] ][ index[teststr[i]] ]=='>':
			now=test[k]
			k-=1
			#print(k,test[k],index[test[k]],now,opg[ index[ test[k] ] ][ index[now] ])
			while opg[ index[ test[k] ] ][ index[now] ]=='>' or opg[ index[ test[k] ] ][ index[now] ]=='=':
				now=teststr[k]
				k-=1
		else:
			txt.insert(END,'\n'+'算符优先文法判断出语法错误！','tag_1')#print('语法错误！')
			txt.insert(END,'第'+str(i+1)+'个单词‘'+teststr[i]+'’出错','tag_1')
			print('错误位置：',test[k],teststr[i],opg[ index[test[k]] ][ index[teststr[i]] ])
			#print(k,test[k],index[test[k]],i,teststr[i],index[teststr[i]],opg[ index[test[k]] ][ index[teststr[i]] ])
			break
	if test[0]==test[1]:
		txt.insert(END,'\n'+'算符优先文法判断出运算式语法正确！'+'\n','tag_2')
		flag[1]=1
		print('接受该语法')

def Printf(id,string,txt,cntt):
	global teststr,semstr #前者用于算符优先文法的语法分析分析，后者后缀式算法的语义分析
	print(cntt,string)
	if id==1:
		teststr[cntt]=string
	else :
		teststr[cntt]=6
	if id==1:#END索引号表示在最后插入
		semstr[cntt]=string
		txt.insert(END,'运算符 '+string+'\n')
	elif id==2:
		semstr[cntt]=string
		txt.insert(END,'十进制整数 '+string+'\n')
	elif id==3:
		flag[0]=1#标志变量，判断词法是否正确
		txt.insert(END,'错误数据 '+string+'\n')
	elif id==4:
		semstr[cntt]=string
		txt.insert(END,'十进制实数 '+string+'\n')
	elif id==5:
		semstr[cntt]=autosystem.oct_to_dec(string)
		txt.insert(END,'八进制整数 '+string+'\n')
	elif id==6:
		semstr[cntt]=autosystem.oct_to_dec(string)
		txt.insert(END,'八进制实数 '+string+'\n')
	elif id==7:
		semstr[cntt]=autosystem.hex_to_dec(string)
		txt.insert(END,'十六进制整数 '+string+'\n')
	elif id==8:
		semstr[cntt]=autosystem.hex_to_dec(string)
		txt.insert(END,'十六进制实数 '+string+'\n')

def Scan (string,txtt,resulttxt):#词法分析
	global cntt
	global flag
	result=''
	cnt,cntt=0,-1
	flag[0]=0
	flag[1]=0
	m=len(string)
	if m==0:#输入为空串
		return 

	str_1_data=string.split()#把字符串切割成一个列表，默认切割符为空格
	str_1=''
	for i in range(len(str_1_data)):
		str_1+=str_1_data[i]
	string=str_1
	string+='#'
	while cnt<m:
		cntt+=1
		result=''
		if operatered.find(string[cnt])>=0:
			result+=string[cnt]
			Printf(1,result,txtt,cntt)#运算符
			result=''
			cnt+=1
		elif is_decnumber(string[cnt]):#十进制
			result+=string[cnt]
			cnt+=1
			while is_decnumber(string[cnt]) or string[cnt]==0:
				result+=string[cnt]
				cnt+=1
			if string[cnt]=='.':#十进制实数
				result+='.'
				cnt+=1
				if is_decnumber(string[cnt]) or string[cnt]==0:#如果小数部分是十进制数，继续执行
					while is_decnumber(string[cnt]) or string[cnt]==0:
						result+=string[cnt]
						cnt+=1
					if operatered.find(string[cnt])>=0:
						Printf(4,result,txtt,cntt)
					else:
						while operatered.find(string[cnt])<0:
							result+=string[cnt]
							cnt+=1
						Printf(3,result,txtt,cntt)
				else:#如果小数部分不是十进制数，就执行，知道输出是运算符时，结束
					while operatered.find(string[cnt])<0:
						result+=string[cnt]
						cnt+=1
					Printf(3,result,txtt,cntt)
			elif operatered.find(string[cnt])>=0:#十进制整数
				Printf(2,result,txtt,cntt)
			else:#出错数据
				while operatered.find(string[cnt])<0:
						result+=string[cnt]
						cnt+=1
				Printf(3,result,txtt,cntt)
		elif string[cnt]=='0':
			result+='0'
			cnt+=1
			if is_octnumber(string[cnt]):#八进制
				while is_octnumber(string[cnt]):
					result+=string[cnt]
					cnt+=1
				if operatered.find(string[cnt])>=0:#八进制整数
					Printf(5,result,txtt,cntt)
				elif string[cnt]=='.':#八进制实数
					result+='.'
					cnt+=1
					if is_octnumber(string[cnt]):
						while is_octnumber(string[cnt]):
							result+=string[cnt]
							cnt+=1
						if operatered.find(string[cnt])>=0:
							Printf(6,result,txtt,cntt)
						else:
							while operatered.find(string[cnt])<0:
								result+=string[cnt]
								cnt+=1
							Printf(3,result,txtt,cntt)
					else:
						while operatered.find(string[cnt])<0:
							result+=string[cnt]
							cnt+=1
						Printf(3,result,txtt,cntt)
				else:#错误数据
					while operatered.find(string[cnt])<0:
						result+=string[cnt]
						cnt+=1
					Printf(3,result,txtt,cntt)
			elif string[cnt]=='x' or string[cnt]=='X':#十六进制
				result+=string[cnt]
				cnt+=1
				if is_hexnumber(string[cnt]):#如果后面跟着的是十六进制数
					while is_hexnumber(string[cnt]):
						result+=string[cnt]
						cnt+=1
					if operatered.find(string[cnt])>=0:#十六进制整数
						Printf(7,result,txtt,cntt)
					elif string[cnt]=='.':#十六进制实数
						result+=string[cnt]
						cnt+=1
						if is_hexnumber(string[cnt]):
							while is_hexnumber(string[cnt]):
								result+=string[cnt]
								cnt+=1
							if operatered.find(string[cnt])>=0:
								Printf(8,result,txtt,cntt)
							else:
								while operatered.find(string[cnt])<0:
									result+=string[cnt]
									cnt+=1
								Printf(3,result,txtt,cntt)
						else:
							while operatered.find(string[cnt])<0:
									result+=string[cnt]
									cnt+=1
							Printf(3,result,txtt,cntt)
				else:
					while operatered.find(string[cnt])<0:
						result+=string[cnt]
						cnt+=1
					Printf(3,result,txtt,cntt)
			elif string[cnt]=='.':#十进制实数
				results+=string[cnt]
				cnt+=1
				if is_decnumber(string[cnt]):
					while is_decnumber(string[cnt]):
						result+=string[cnt]
						cnt+=1
					if operatered.find(string[cnt])>=0:
						Printf(4,string,txtt,cntt)
					else:
						while operatered.find(string[cnt])<0:
							result+=string[cnt]
							cnt+=1
						Printf(3,result,txtt,cntt)
				else:
					while operatered.find(string[cnt])<0:
						result+=string[cnt]
						cnt+=1
					Printf(3,result,txtt,cntt)
			else:
				Printf(3,result,txtt,cntt)
		else:
			Printf(3,result,txtt,cntt)#flag[0]=1
			return

def main_pro(string,txtt,resulttxt):

	#init(autoreset=True)
	if string.find('(')>=0:
		txtt.insert(END,'\n'+'本程序只能使用中文括号，请重置后重新输入！'+'\n','tag_1')
		return
	
	Scan(string,txtt,resulttxt)
	show()
	if flag[0]==1:
		txtt.insert(END,'\n'+'使用DFA判断出词法错误!,请检查！'+'\n','tag_1')#print('词法错误!,请检查！')
		#print('\033[1;31;40m'+'词法错误!,请检查！'+'\033[0m')
		#print('\033[1;31;40m'+'词法错误!,请检查！'+'\033[0m')
		#print("\033[0;31;40m\tHello World\033[0m") #红色
		return
	else:
		txtt.insert(END,'\n'+'使用DFA分析词法正确'+'\n','tag_2')
	grammer(txtt)
	if not(flag[0]==0 and flag[1]==1):
		resulttxt.insert(END,'有错误！','tag_1')
		print('有错误！')
		return 
	SEMANTICS(resulttxt)
