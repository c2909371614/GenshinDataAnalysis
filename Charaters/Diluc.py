#coding = utf-8
#author = cpx
#created time = 2020-12-22 10:38:10
from Hero import Hero
class Diluc(Hero):
	"""docstring for Diluc"""
	def __init__(self, Att, Talents):
		Talents = {
			'A' = [142, 139, 156, 212],#七级卢老爷天赋
			'E' = [142, 146, 193],
			'Q' = [306, 90]
		}
		super().__init__('迪卢克', Att, Talents, '双手剑')

diluc = Diluc(Att = ' ', Talents = ' ')
print(diluc.name)
