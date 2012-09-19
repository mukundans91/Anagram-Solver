s=set()
with open('1.txt') as f:
	one=f.readlines()

for word in one:
	s.add(word.split(' ')[0].split('\n')[0])

with open('2.txt') as f:
	one=f.readlines()

for word in one:
	s.add(word.split(' ')[0].split('\n')[0])

with open('3.txt') as f:
	one=f.readlines()

for word in one:
	s.add(word.split(' ')[0].split('\n')[0])

with open('4.txt') as f:
	one=f.readlines()

for word in one:
	s.add(word.split(' ')[0].split('\n')[0])

with open('5.txt') as f:
	one=f.readlines()

for word in one:
	s.add(word.split(' ')[0].split('\n')[0])

with open('6.txt') as f:
	one=f.readlines()

for word in one:
	s.add(word.split(' ')[0].split('\n')[0])

with open('wordsEn.txt') as f:
	one=f.readlines()

for word in one:
	word=word.upper().split('\n')[0].split(' ')[0]
	if word not in s:
		s.add(word)

print len(s)
with open('final.txt','w') as f:
	for word in sorted(s):
		f.write(word+'\n')

s=set()

with open('final.txt') as f:
	one=f.readlines()

for word in one:
	s.add(word.split(' ')[0].split('\n')[0].split('\r')[0])

print len(s)
with open('final.txt','w') as f:
	for word in sorted(s):
		f.write(word+'\n')

