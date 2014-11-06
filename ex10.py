print "I am 6'2\" tall"     #escape double-quote inside string
print 'I am 6\'2" tall'     #escape single-quote inside string

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat


#test various escape sequences

print """
backslash : \\
single-quote : \'test\' \t    'test'
double-quote : \"test\" \t    "test"
ASCII bell : \a \t whats is this?
ACSII backspace : \b
ACSII formfeed : What is this? \f test?
ACSII linefeed : \n new line?
Character named name in the uncode tablebase(Unicede only) : \N
Carriage Return(CR) : \r ASCII : What is this?
Horizental Tab(TAB) : \t ASCII : leave spaces to right...
Character with 16-bit hex value xxxx(Unicode Only) : \uxxxx : eg : \u12F0
Character with 32-bit hex value xxxxxxxx(Unicode Only) : \Uxxxxxxxx : eg : \U12F0A68B
ACSII vertical tab(VT) : \v (test!?)
Character with octal value ooo : \ooo : eg : \376
Character with hex value hh :
"""
#\xhh :
print '''
eg : \xA8
'''

print "\xA8"
print "\376"
print "\uxxxx"
