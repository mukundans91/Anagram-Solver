permute=[]
def initpermute():
	global permute
	permute=[]

def getpermute():
	global permute
	return permute

def showPattern(st,chars):
	if len(chars) <= 1:
		permute.append(st + chars)
	else:
		for i in range(len(chars)):
			newString = chars[0:i]+chars[i + 1:]
			showPattern(st + chars[i], newString)
if __name__=='__main__':
	import sys
	import time
	st=time.time()
	showPattern("",sys.argv[-1])
	el=time.time()-st
	print 'Permutations \n',permute
	print 'Time taken :',el
