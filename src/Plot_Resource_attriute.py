#coding = utf-8
#author = cpx
'''
#-------------------------------
绘制资源图

#-------------------------------
'''
from matplotlib.font_manager import FontProperties  #设置显示中文
import matplotlib.pyplot as plt
import Relics_Attribute_Analysis as Relics_Data

add_exps = Relics_Data.add_exps
grade = Relics_Data.grade
attributes_main = Relics_Data.attributes_main.copy()
for key in attributes_main.keys():
    print(key, attributes_main[key])

# font = FontProperties(fname=r"simsun.ttf", size=14)  # ""里面为字体的相对地址 或者绝对地址
f, ax1 = plt.subplots()
ax1.plot(grade, add_exps, color='red', label='exp')
ax1.set_ylim([0, add_exps[len(add_exps) - 1]])
ax1.set_xlim([0, 20])
ax1.set_ylabel(u'金币和圣遗物经验(思念)', fontproperties='SimHei')
ax2 = ax1.twinx()  # 创建第二个坐标轴
# print(attributes_main['ATK'])
ax2.plot(grade, attributes_main['ATK'], label='ATK')
ax2.plot(grade, attributes_main['CR'], label='CR')
ax2.plot(grade, attributes_main['CD'], label='CD')
ax2.set_ylim([0, 0.7])
ax1.set_xlabel(u'等级', fontproperties='SimHei')  #设置x轴名称 x label
ax2.set_ylabel(u'数值百分比', fontproperties='SimHei')  #设置y轴名称 y label
ax2.set_title(u'原神资源与数值关系对比', fontproperties='SimHei')  #设置图名为Simple Plot
ax1.legend(loc='center left')
ax2.legend(loc='best')

plt.show()
# plt.savefig(fname = '原神资源与数值关系对比.png', figsize = [255,255])