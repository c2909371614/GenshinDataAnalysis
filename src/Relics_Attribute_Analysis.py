#coding = utf-8
#author = cpx
import matplotlib.pyplot as plt

in_exps = (0,3000,3728,4422,5150,5900,6675,7500,8350,9225,10125, \
 11050,12025,13025,15150,17600,20375,23500,27050,31050,35575)#五星圣遗物1-20级需要的强化经验
money = in_exps  #原神圣遗物强化经验和强化金币需求相同
out_exps = (420, 840, 1260, 2520, 3780)  #1-5星圣遗物作为强化材料的提供的经验
attributes_main_max = {  # +20圣遗物主属性磁条
    'ATK': 0.466,  #攻击力
    'CR': 0.311,  #暴击率
    'CD': 0.622,  #暴击伤害
    'EDA': 0.466,  #元素伤害加成
    'PDA': 0.583  #物理伤害加成
}
attributes_main_min = {  # +0圣遗物主属性磁条
    'ATK': 0.07,  #攻击力
    'CR': 0.047,  #暴击率
    'CD': 0.093,  #暴击伤害
    'EDA': 0.07,  #元素伤害加成
    'PDA': 0.079  #物理伤害加成
}
add_exps = [0] * len(in_exps)

#------对in_exp做前缀和得到累积经验-----
for i in range(len(in_exps) - 1):
    add_exps[i + 1] = add_exps[i] + in_exps[i + 1]

#------计算每级圣遗物主属性增长量----
attributes_main_add = attributes_main_min.copy()  #创建初始化
for temp in attributes_main_min.keys():
    attributes_main_add[temp] = (attributes_main_max[temp] -
                                 attributes_main_min[temp]) / 20

#------计算各等级圣遗物主属性磁条-----
# print(attributes_main_min)
attributes_main = attributes_main_min.copy()
# print(attributes_main_min)

# print(attributes_main_min,'\n', attributes_main_add,'\n',attributes_main)
i = 0
for key in attributes_main.keys():
    # print(attributes_main[key], type(attributes_main[key]))
    attributes_main[key] = [0] * 21  #初始化长度
    attributes_main[key][0] = attributes_main_min[key]
    # print(attributes_main_min[key])
    for j in range(20):
        # print(i*20 + j)
        attributes_main[key][j + 1] = round(
            attributes_main_min[key] + attributes_main_add[key] * (j + 1), 3)

    # i += 1
    # print(key,attributes_main[key])
grade = range(21)

# plt.plot(add_exps, grade, 'y-')
# plt.show()
# print(attributes_main_add)
# print(len(add_exps),len(in_exps))
# am_keys = list(attributes_main.keys())
# print(am_keys)
# # print(attributes_main)
# for i in range(4):
# 	gradeT = (i+2)*4
# 	print('圣遗物+%d：%dmoney' %(gradeT, add_exps[gradeT-1]), end =' ')
# 	for j in range(5):
# 		att = attributes_main[am_keys[j]][gradeT]
# 		print('%.3f%s' %(att, am_keys[j]), end = ' ')
# 	print()
print(add_exps[20] - add_exps[8] + 5675)

# print('圣遗物+8：%d +12:%d +16:%d +20:%d ' %(add_exps[7],add_exps[11],add_exps[15],add_exps[19]))
