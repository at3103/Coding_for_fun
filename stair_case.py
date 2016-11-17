def answer(n):
	l =[0]*(n+1)

	for i in xrange(0,n+1):
		l[i] = [0]*(n+1)
		
	for i in xrange(3,n+1):
		for j in xrange(1,n+1):
			l[i][j] = l[i][j-1] 
			if l[i-j][j-1] <= 0 and i-j> 0 and j>i-j:
				l[i][j]+= 1 
			if i-j> 0:
				c = l[i-j][j-1]>0 and (l[i-j][j-1] == l[i-j][j-2])
				l[i][j]+= l[i-j][j-1] + int(c)

	return l[n][n]
