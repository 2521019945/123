#coding:gbk
"""
RPSLS��Ϸ ���ߣ�������
"""
import random
def number_to_name(number):#�����ָ�������
	#�Զ��庯��
	if number==0:
		number=("ʯͷ")
	elif number==1:
		number=("ʷ����")
	elif number==2:
		number=("��")
	elif number==3:
		number=("����")
	else:
		number=("����")
	return number
def name_to_number(name):#Ϊ���ָ�������
	#�Զ��庯��
	if name==("ʯͷ"):
		name=0
	elif name==("ʷ����"):
		name=1
	elif name==("��"):
		name=2
	elif name==("����"):
		name=3
	else:
		name=4
	return name  
def rpsls(player_choice):
	#�Զ��庯��
	comp_number=random.randrange(0,5)
	print("�������ѡ��Ϊ��")
	print(number_to_name(comp_number))
	if  player_choice not in [("ʯͷ"),("ʷ����"),("��"),("����"),("����")]:#���1
		print("Error: No Correct Name")
	elif player_choice==number_to_name(comp_number):#���2
		print("���ͼ��������һ����")
	else:#���3
		if   name_to_number(player_choice)==4 and (comp_number==2 or comp_number==3):
			 print("��Ӯ�ˣ�")
		elif name_to_number(player_choice)==0 and (comp_number==3 or comp_number==4):
			 print("��Ӯ�ˣ�")
		elif name_to_number(player_choice)==1 and (comp_number==0 or comp_number==4):
			 print("��Ӯ�ˣ�")
		elif name_to_number(player_choice)==2 and (comp_number==1 or comp_number==0):
			 print("��Ӯ�ˣ�")
		elif name_to_number(player_choice)==3 and (comp_number==1 or comp_number==2):
			 print("��Ӯ�ˣ�")
		else:
			 print("�����Ӯ��")	 
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)
	
    
