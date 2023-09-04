#coding = utf-8
#author = cpx
#created time = 2020-12-22 10:39:11

class Hero():
	'''
	定义原神角色的基本属性，天赋，武器类型，名字
	'''
	def __init__(self, name, Att, Talents, weapons):
		'''
		初始化角色信息
		'''
		self.name = name
		self.Att = Att
		self.Talents = Talents
		self.weapons = weapons

	def Get_Strength():
		'''
		计算角色练度
		'''
		ATK = Att['ATK']
		CR = Att['CR']
		CD = Att['CD']
		DA = max(Att['EDA'], Att['PDA'])
		E_S = ATK*(1+CR*CD)*(1+DA)
		return E_S

