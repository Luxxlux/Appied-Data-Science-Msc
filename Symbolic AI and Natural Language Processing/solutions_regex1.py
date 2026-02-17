# Exercise 1: Write a regex that matches all the words in {a,b,c}* that contain exactly two a's.

# Exercise 2: Write a regex that matches all the words in {a,b,c}* where every a is immediately followed by b.

# Exercise 3: Write a regex that matches all the words in {a,b,c}* where all a's appear before any b.

# Exercise 4: Write a regex that matches all the words that do not contain the substring 'aa'.

# Exercise 5: Write a regex that matches all the words with lowercase letters and alternating vowel and consonants.

# Exercise 6: Write a regex that matches all the words with:
# - alphabetical letters (lowercase or uppercase)
# - length between 5 and 8 (included)
# - do not contain the letter 'd' (upper or lower case)

# Exercise 7: Write a regex that matches all the alphabetical words with exactly one uppercase letter.

# Exercise 8: Write a regex that matches all the alphabetical words with at least one uppercase letter.

# Exercise 9: Write a regex that matches all the strings that contain an arbitrary number of words such that:
# - each word contains only word characters (A-Z, a-z, 0-9,)
# - words are separated by the sequence ';;'
# - there can be an arbitrary number of whitespaces between the words and the sequence ';;'
# - the last word is not followed by ';;'

# Exercise 10: Write a regex that matches a <div> HTML block, i.e. any string contained between <div> and </div>.

# Exercise 11: Write a regex that matches all the words that end in pdf.

# Exercise 12: Write a regex that matches all the words that:
# - start with 'ERROR', followed by a 4-digit number
# - do not contain the substring '!!'
# - then ':'.

# Exercise 13: Write a regex that matches all the words w in {a,b,c}* that begin and end with the same letter.

from utils import *


def exercise1():
	# Score: 10/10
	return '[bc]*a[bc]*a[bc]*'


def exercise2():
	# Score: 10/10
	return '([bc]*(ab)*[bc]*)*'

def exercise3():
	# Score: 10/10
	return '(c*a*c*)*(b*c*)*'

def exercise4():
	# Score: 7/10
	return '[\w*]*[^aa][\w*]*'

def exercise5():
	# Score: 7/10
	return '([aeiou][bcdfghjklmnpqrstvwxyz])*'

def exercise6():
	# Score: 10/10
	return '([aeioubcfghjklmnpqrstvwxyz]|[QWERTYUIOPASFGHJKLZXCVBNM]){5,8}'

def exercise7():
	# Score: 10/10
	return '(([aeioubcfghjkldmnpqrstvwxyz])*[DQWERTYUIOPASFGHJKLZXCVBNM]{1}){1}([aeioubcfghjkldmnpqrstvwxyz])*'

def exercise8():
	# Score: 10/10
	return '(([aeioubcfghjkldmnpqrstvwxyz])*[DQWERTYUIOPASFGHJKLZXCVBNM]{1,}){1,}([aeioubcfghjkldmnpqrstvwxyz])*'

def exercise9():
	# Score: 5/10
	return '(\w*;;)*((\w*)*)'

def exercise10():
	# Score: 10/10
	return '<div>.*(</div>)'

def exercise11():
	# Score: 10/10
	return '.*(\.pdf)$'

def exercise12():
	# Score: 8/10
	return 'ERROR[1-9]{4}:.*\s*'

def exercise13():
	# Score: 10/10
	return 'a(a*b*c*)*a|b(a*b*c*)*b|c(a*b*c*)*c'