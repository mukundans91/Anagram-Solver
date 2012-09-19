#http://zyzzyva.net/wordlists.shtml
import sqlite3
import os

crete=False

def alphagram(s):
	s=s.upper()
	return ''.join(sorted(s))


if not os.path.exists('worddb.db'):
	crete=True

db=sqlite3.connect('worddb.db')
if crete:
	db.execute('create table words (word varchar(50),alpha varchar(50))')
	print 'Creating database...'
	with open('final.txt') as f:
		words=f.readlines()
	total=len(words)
	#print words
	print total
	counter=1
	for word in words:
		word=word[:-1]
		db.execute("insert into words values(?,?)",(word,alphagram(word)))
		print '%20s'%(str(int((counter*1.0/total*1.0)*100))+' percent done \r'),
		counter+=1
	print
	db.commit()

#cur=db.execute('select * from words')
#for row in cur:
#	print row

import time
while True:
	inp=raw_input('Enter the word to find the anagram:')
	if inp=='end!':
		break
	
	st=time.time()
	cur=db.execute("select * from words where alpha like '"+alphagram(inp)+"'")
	rows=cur.fetchall()
	cur.close()
	if not rows:
		print 'Word pattern not found in database!!!'
	else:
		elapsed=time.time()-st
		print 'The anagram is :'
		for row in rows:
			print str(row[0])
		print 'The time taken to find the list of anagrams is :',elapsed
