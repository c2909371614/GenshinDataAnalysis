# -*- coding: utf-8 -*-
#@author: cpx
#creating time = 2020.12.13

ATK = float(input('输入攻击力：'))
CR = float(input('输入暴击率：'))
CD = float(input('输入暴击伤害：'))
EDA = float(input('输入伤害加成：'))
E_S = ATK*(1+CR*CD)*(1+EDA)
print('预期伤害：%.2f' %E_S)