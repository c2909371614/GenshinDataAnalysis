#coding = utf-8
#author = cpx
import time

# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )
with open("New_coding.txt",'w') as file:
	file.write('#coding = utf-8\n')
	file.write('#author = cpx\n')
	file.write('#created time = ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n'*2)
	

