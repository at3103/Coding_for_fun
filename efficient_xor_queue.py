def even_xor(start, length):

	rem = int(length)%4
	end = start + length -1
	d = {0:0,1:end,2:1,3:end+1}

	return d[rem]


def odd_xor(start, length):
	
	rem = int(length)%4
	end = start + length - 1
	se = start^end
	ze = (end+1)^start
	d = {0:ze,1:start,2:se,3:start-1}

	return d[rem]

def answer(start, length):
	# your code here
	ret = 0
	check_sum = start
	l =[]
	sub_l = length
	new_start = start

	while sub_l > 0:
		
		if new_start%2 == 0:
			l.append(even_xor(new_start,sub_l))
		else:
			l.append(odd_xor(new_start,sub_l))
		new_start += length
		sub_l -= 1

	for e in l:
		ret^=e
	return int(ret)

print answer(10,1000)

#print 253^254^255^256	

# c =252
# x=251
# i=1
# #print 252 ^ 1000099
# while c < 10000046:
# 	x ^= c
# 	c+=1
# 	i+=1
# print x,i
# print 251^ 10000020

#print (252^253^254^255)^256^(257^258^259)
#print 100034^100035^100036^100037^100038^100039
