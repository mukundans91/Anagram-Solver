#http://zyzzyva.net/wordlists.shtml
import sqlite3
import os

def findana(inp,db):
	import itertools as tools
	import time
	st=time.time()
	l=[''.join(r) for r in tools.permutations(inp)]
	print len(l)
	rows=[]
	for word in l:
		cur=db.execute("select * from words where word like '"+word+"'")
		row=cur.fetchall()
		cur.close()
		for wr in row:
			rows.append(str(wr[0]))
	elapsed=time.time()-st
	return rows,elapsed


crete=False


if not os.path.exists('worddb.db'):
	crete=True

db=sqlite3.connect('worddb.db')
if crete:
	db.execute('create table words (word varchar(50))')
	print 'Creating database...'
	with open('final.txt') as f:
		words=f.readlines()
	total=len(words)
	#print words
	print total
	counter=1
	for word in words:
		word=word[:-1]
		db.execute("insert into words values(?)",(word,))
		print '%20s'%(str(int((counter*1.0/total*1.0)*100))+' percent done \r'),
		counter+=1
	print
	db.commit()

#cur=db.execute('select * from words')
#for row in cur:
#	print row


while True:
	inp=raw_input('Enter the word to find the anagram:')
	if inp=='end!':
		break
	rows,elapsed=findana(inp,db)
	if not rows:
		print 'Word pattern not found in database!!!'
	else:
		print 'The anagram is :'
		for row in rows:
			print str(row)
		print 'The time taken to find the list of anagrams is :',elapsed

