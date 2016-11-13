from array import array

def sanitize(l):
	l.sort(reverse=True)
	return int("".join([str(i) for i in l if str(i).isdigit()]))


def answer(l):
    # your code here
	ret = 0
	flag_z = 0
	flag_o = 0
	count_z = 0
	count_o	= 0
	count_t = 0
	size = len(l)
	sum_l = sum(l)
	if sum_l%3 == 0:
		return sanitize(l)
	else:
		l.sort()
		rem_l = array('H',[0]*(len(l)))
		for i in xrange(0,len(l)):
			rem_l[i] = l[i]%3
		count_z = rem_l.count(0)
		count_o = rem_l.count(1)
		count_t = rem_l.count(2)

		if count_z == 0 and count_o == 0 and count_t < 3:
			return 0
		if count_z == 0 and count_t == 0 and count_o < 3:
			return 0
		if count_o == 0:
			d_to_rem = 2
			to_rem = count_t%3
		elif count_t == 0:
			d_to_rem = 1
			to_rem = count_o%3
		else:
			to_rem = 1
			diff = count_o - count_t
			if diff%3 == 1:
				d_to_rem = 1 if diff > 0 else 2
			else:
				d_to_rem = 2 if diff > 0 else 1

		while to_rem > 0:
			ind = rem_l.index(d_to_rem)
			poped1 = l.pop(ind)
			poped2 = rem_l.pop(ind)
			to_rem -= 1
	return sanitize(l)