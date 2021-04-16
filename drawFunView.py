import numpy as np
import matplotlib.pyplot as plt

def getExpDam(type):
	ATK = 1800
	CR = 0.5
	CD = 1
	DA = 0.6
	if type == "ATK":
		ATK = np.linspace(0, 1800, 100, endpoint = False)
	elif type == "CR":
		CR = np.linspace(0, 1, 100, endpoint = False)
	elif type == "CD":
		CD = np.linspace(0, 2, 100, endpoint = False)
	elif type == "DA":
		DA = np.linspace(0, 0.6, 100, endpoint = False)
	# print(ATK)
	return ATK*(1+CR*CD)*(1+DA)
# print(E_S)
atk = np.linspace(0, 1800, 100, endpoint = False)
cr = np.linspace(0, 1, 100, endpoint = False)
cd = np.linspace(0, 2, 100, endpoint = False)
da = np.linspace(0, 0.6, 100, endpoint = False)
	# print(ATK)
plt.plot(cr, getExpDam("CR"),'red', cd, getExpDam("CD"),'blue', 
	da, getExpDam("DA"), 'green')
plt.show()