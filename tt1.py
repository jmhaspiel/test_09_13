# def xplace(stx):
# 	st2 = 'x'+stx[1:]
# 	return st2
# print xplace('potato')

# def shortest_string(lst1):
# 	shortest_length= 999999
# 	shortest = ''
# 	for strin in lst1:
# 		if len(strin) < shortest_length:
# 			shortest = strin
# 			shortest_length = len(strin)
# 	return shortest
# print shortest_string(['dog','potato','avocado','antiaircraft'])

# lst=[]
# newnum = 0
# while newnum >=0:
# 	newnum = int(raw_input('enter a number'))
# 	if newnum >=0:
# 		lst.append(newnum)
# print lst

def combineDict(lst):
	d = {}
	for x in lst:
		for key in x:
			if key not in d:
				d[key] = [x[key]]
			else: 
				d[key].append(x[key])
	return d

print combineDict([{'a':1, 'b':2, 'd':11},{'a':4, 'b':5, 'd':12},{'a':7, 'b':8, 'f':11, 'g':11}])

# el = ['tHANK','GOD','iTS','FRIDAY']
# acro = ""
# for e in el:
# 	acro = acro.upper()+ e[0]
# print acro




