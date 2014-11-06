# -*- coding: cp936 -*-
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
#yeh i din't think of it print 4'%r %r %r %r' in this line...

print formatter % (
    "I had this thing.",
    "That you type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)


#common questions

#3. fail printing chinese with %r?
print "%r" %"测试"
print "%s" %"测试"
#alright it failed with "%r" but all right with "%s"
