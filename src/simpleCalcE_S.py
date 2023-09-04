# -*- coding: utf-8 -*-
#@author: cpx
#creating time = 2020.12.13

CR = CD = DA = ATK = 0
def Get_Input():
	ATK = float(input('输入攻击力：'))
	CR = float(input('输入暴击率：'))
	CD = float(input('输入暴击伤害：'))
	DA = float(input('输入伤害加成：'))
	return [CR,CD,DA,ATK]
def Get_Txt():
	with open('原神角色数值/雷泽面板.txt', 'r') as file:
		ATK = float(file.readline())
		CR = float(file.readline())
		CD = float(file.readline())
		DA = float(file.readline())
	return [CR,CD,DA,ATK]
	# print(CR,CD,DA,ATK)
CR,CD,DA,ATK = Get_Input()
print('ATK:%.0f\nCR:%.3f\nCD:%.3f\nDA:%.3f'%(ATK,CR,CD,DA))
E_S = ATK*(1+CR*CD)*(1+DA)

print('预期伤害：%.2f' %E_S)
input()
