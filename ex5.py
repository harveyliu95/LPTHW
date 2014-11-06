my_name = 'Liu Tong'
my_age = 19
my_height = 180 #cm
my_weight = 55 #kg
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Black'

print "Let's talk about %s" % my_name
print "He's %dcm tall." % my_height
print "He's %dkg heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffe."    % my_teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %dI get %d" % (
    my_age, my_height, my_weight, my_age + my_height + my_weight )

#study drills

name = 'Liu Tong'
age = 19
height = 180 / 2.54 #inch
weight = 55 * 2.20462262 #pound
eyes = 'Black'
teeth = 'White'
hair = 'Black'

print "Let's talk about %s" % name
print "He's %f inches tall." % height
print "He's %f pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffe."    % teeth

#this line is tricky, try to get it exactly right
print "If I add %f, %f, and %f I get %f\n" % (
    age, height, weight, age + height + weight )

r = "%d = 5\n"
print "%r" %r
print "%s" %r

#test from www.cnblogs.com/vamei/archive/2013/03/12/2954938.html
print ("%+10x" % 10)
print ("%04d"  % 5 )
print ("%6.3f" % 2.3)
print ("%.*f"  % (4, 1.2) )
