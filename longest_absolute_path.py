class Solution(object):
	def lengthLongestPath(self, input):
		"""
        :type input: str
        :rtype: int
        """
		list_paths = input.split('\n')
		count = list()
		longest = 0

		for i in range(0,len(list_paths)):
			spaces = 0
			sp_l = 0
			flag = 0
			count.append(list_paths[i].count('\t'))
			if count[i] == 0:
				flag = 1
				count[i] += list_paths[i].count('    ')
			prev = i-1
			if count[prev] >= count[i]:
				while count[prev] >= count[i] and prev > 0:
					prev = prev - 1
			list_paths[i] = list_paths[i].strip('\t')
			if flag == 1:
				spaces = list_paths[i].count('    ')
				list_paths[i] = list_paths[i].strip('    ')
			if count[i] > 0:
				list_paths[i] = list_paths[prev] + '/' + list_paths[i]
			if spaces > 1:
				sp_l = (spaces - 1) * 4
			if list_paths[i].count('.') > 0 and len(list_paths[i]) + sp_l > longest:
				longest = len(list_paths[i]) + sp_l
		return int(longest)

input = "root\n\tsubdir1\n\t\tfile2\n\tsubdir2\n\t\tfile\n\t\tfile1"
#input = "dir\n\tsubdir1\n\t\tfile1aaaaaaaaaaaabasbjbasjbajsbajsb.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
#input = "dir\n    file.txt"
#input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
#input = "dir\n        file.txt"
input = "dir\n\t        file.txt\n\tfile2.txt"
input = "a\n\tb.txt\na2\n\tb2.txt"
print input
#print l
#l = l.strip('\t')
#print l
#and l.count('.') >= 0

list_paths = input.split('\n')
count = list()
longest = 0
print list_paths
for i in range(0,len(list_paths)):
	spaces = 0
	sp_l = 0
	flag = 0
	count.append(list_paths[i].count('\t'))
	if count[i] == 0:
		flag = 1
		count[i] += list_paths[i].count('    ')
	prev = i-1
	if count[prev] >= count[i]:
		while count[prev] >= count[i] and prev > 0:
			prev = prev - 1
	list_paths[i] = list_paths[i].strip('\t')
	if flag == 1:
		spaces = list_paths[i].count('    ')
		list_paths[i] = list_paths[i].strip('    ')
	if count[i] > 0:
		list_paths[i] = list_paths[prev] + '/' + list_paths[i]
	if spaces > 1:
		sp_l = (spaces - 1) * 4
	if list_paths[i].count('.') > 0 and len(list_paths[i]) + sp_l > longest:
		longest = len(list_paths[i]) + sp_l
print longest
#print count
print list_paths
