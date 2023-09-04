#coding = utf-8
#author = cpx
#created time = 2021-05-21 23:40:47

def calc_EM(EM):
	# EM = 100
	P = EM/(0.0037*EM+5)/100 
	Q = P*12.0/5
	R = P*8.0/5
	res = [P,Q,R]#增幅反应倍率，剧变反应倍率，结晶倍率
	return res
EM = [100,200,300,400,500]
for i in EM:
	res = calc_EM(i)
	print("元素精通：%d 增幅反应倍率：%.4f 剧变反应倍率：%.4f 结晶反应倍率：%.4f"%(i,res[0],res[1],res[2]))

