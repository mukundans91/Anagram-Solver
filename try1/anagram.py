import sqlite3

db=sqlite3.connect(':memory:')
db.execute('create table words (word varchar(50),alpha varchar(50))')

with open('wordsEn.txt') as f:
	words=f.readlines()

def alphagram(s):
	return ''.join(sorted(s))

for word in words:
	word=word[:-2]
	db.execute("insert into words values(?,?)",(word,alphagram(word)))

#cur=db.execute('select * from words')
#for row in cur:
#	print row

while True:
	inp=raw_input('Enter the word to find the anagram:')
	if inp=='end!':
		break
	cur=db.execute("select * from words where alpha like '"+alphagram(inp)+"'")
	print 'The anagram is :'
	for row in cur:
		print str(row[0])

