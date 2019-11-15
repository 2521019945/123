#coding:gbk
"""
RPSLS游戏 作者：罗来金
"""
import random
def number_to_name(number):#给数字赋予文字
	#自定义函数
	if number==0:
		number=("石头")
	elif number==1:
		number=("史波克")
	elif number==2:
		number=("布")
	elif number==3:
		number=("蜥蜴")
	else:
		number=("剪刀")
	return number
def name_to_number(name):#为文字赋予数字
	#自定义函数
	if name==("石头"):
		name=0
	elif name==("史波克"):
		name=1
	elif name==("布"):
		name=2
	elif name==("蜥蜴"):
		name=3
	else:
		name=4
	return name  
def rpsls(player_choice):
	#自定义函数
	comp_number=random.randrange(0,5)
	print("计算机的选择为：")
	print(number_to_name(comp_number))
	if  player_choice not in [("石头"),("史波克"),("布"),("蜥蜴"),("剪刀")]:#情况1
		print("Error: No Correct Name")
	elif player_choice==number_to_name(comp_number):#情况2
		print("您和计算机出的一样呢")
	else:#情况3
		if   name_to_number(player_choice)==4 and (comp_number==2 or comp_number==3):
			 print("您赢了！")
		elif name_to_number(player_choice)==0 and (comp_number==3 or comp_number==4):
			 print("您赢了！")
		elif name_to_number(player_choice)==1 and (comp_number==0 or comp_number==4):
			 print("您赢了！")
		elif name_to_number(player_choice)==2 and (comp_number==1 or comp_number==0):
			 print("您赢了！")
		elif name_to_number(player_choice)==3 and (comp_number==1 or comp_number==2):
			 print("您赢了！")
		else:
			 print("计算机赢了")	 
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
rpsls(choice_name)
	
    
