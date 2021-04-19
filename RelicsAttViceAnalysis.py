#coding = utf-8
#author = cpx
#created time = 2021-04-19 09:21:55
ATK_0 = 800
ATK_1 = 0.246
CR_0 = 0
CD_0 = 0.5
EDA_0 = 0.2
ans = 0
count = 0
for ATK in range(4,25):
	for CR in range(5, 35-ATK):

		CD = 38 - ATK - CR
		if(CD > 24):
			continue
		count += 1
		ATK_temp = (ATK_0*(1+ATK*0.058+0.466+ATK_1)+311)
		CR_temp = (CR*0.039+CR_0)
		CD_temp = (CD*0.078+0.62+CD_0)
		DA_temp = (0.466+EDA_0)
		Damage = ATK_temp*(1+CR_temp*CD_temp)*DA_temp
		if(ans < Damage):
			ans = Damage
			print('第%d种：'%count, 'ATK:',ATK,'CR:',CR, 'CD:',CD)
			print('ATK:',ATK_temp, 'CR:%.2f'% CR_temp, 'CD:',CD_temp)
			# print("ATK:%.0f CR：%.2f% CD：%.2f"%(ATK_temp, CR_temp*100, CD_temp*100))
