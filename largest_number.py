# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(X):
	# write your code in Python 2.7
	S =  str(X)
	largest = 0

	if len(S) == 1:
		return X

	for j in range(0,len(S)-1):
		x = int(S[j])
		y = int(S[j+1])
		av = str((x+y+1)/2)
		temp = S
		temp = int(temp.replace(S[j:j+2],av))
		if largest < temp:
			largest = temp
	return largest

print solution(2244)

