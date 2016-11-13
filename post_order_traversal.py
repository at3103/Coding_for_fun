'''
Find the label of  the parent of the given node for a perfect binary tree of given height h.
The label is computed based on the post-order traversal of the tree. 
'''

def answer(h,q):
	new_list=[]

	for e in q:
		p = int((2**h)-1)
		d = p
		if e==p:
			new_list.append(int(-1))
			continue
		while True:
			d = (d-1)/2
			r = p-1
			l = r-d
			if e == l or e ==r:
				new_list.append(int(p))
				break
			elif e< l:
				p = l
			else:
				p = r

	return new_list