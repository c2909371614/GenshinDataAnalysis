#coding = utf-8
#author = cpx
#created time = 2021-04-23 13:59:31

'''
一个简单的暴击爆伤比例分析
'''
class Att(object):
	"""docstring for ClassName"""
	def __init__(self):
		self.CD = 0
		self.CR = 0
		self.weight = 0
		self.val = 0
	def display(self):
		print('CR:%.4f'% self.CR, 'CD:%.4f'% self.CD, 'val:%.4f'%self.val, 'weight:%d'%weight)

CD_0 = 0.622+0.5
CR_0 = 0
for i in range(1,26):
	# if()
	for j in range(min(30-i, 20)):
		CD = CD_0+j*0.078
		CR = CR_0+i*0.039
		if(i+j != 18):
			continue
		print('CR:%.4f'% (CR), 'CD:%.4f'% (CD), 'exp:%.4f'%(1+CD*CR), 'weight:%d'% (i+j))
		# print('CR:%.4f'%CD)
		# print(CD,CR,1+CD*CR)

