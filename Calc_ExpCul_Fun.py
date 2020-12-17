#coding = utf-8
#author = cpx
#created time = 2020-12-16 22:56:29

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('原神数据.xlsx', '角色等级经验')
print(data.info())
exps = list(data['经验'])
exps = exps[:80]

def AnalysisIncreaseRule():

	#-----对等级经验数组进行差分----
	exps_diff = [0]*(len(exps) - 1)
	for i in range(len(exps_diff)):
		exps[i] = int(exps[i]) 
		exps_diff[i] = int(exps[i+1] - exps[i])
	exps[len(exps)-1] = int(exps[len(exps)-1]) 
	#------------二次差分----------
	exps_diff_2 = [0]*(len(exps_diff) - 1)
	for i in range(len(exps_diff_2)):
		exps_diff_2[i] = exps_diff[i+1] - exps_diff[i]
		if(exps_diff_2[i] > 75 or exps_diff_2[i] < 25):
			print(i,':%d = %d - %d '%(exps_diff_2[i], exps_diff[i+1], exps_diff[i]))

	print('-'*40 + '原神等级经验增长规律' + '-'*40, '\n')
	print('       等级经验：', exps, type(exps))
	print('上一行数据的差分：', exps_diff, type(exps_diff))
	print('上一行数据的差分：', exps_diff_2, type(exps_diff_2))
def GetCulmulativeExp():
	#-----对等级经验进行前缀和------
	exps_cul = [0]*int(len(exps))
	exps_cul[0] = exps[0]
	for i in range(len(exps_cul)-1):
		exps_cul[i+1] = exps_cul[i] + exps[i+1]

	# print(exps_cul[60])
	return exps_cul
exps_cul = GetCulmulativeExp()
data['累计'] = exps_cul
# df = pd.DataFrame()
# data.to_excel('原神数据.xlsx', '角色等级经验')
# pd.write_excel('原神数据.xlsx', '角色等级经验')
# x = range(1,81)
# plt.plot(x, exps_cul)
# plt.title('经验花费随角色等级变化图', fontproperties='SimHei')
# plt.xlabel('等级', fontproperties='SimHei')
# plt.ylabel('累计需要的经验值', fontproperties='SimHei')
# plt.show()


