#r for "result", 28 for exercise 28

r2801 = True and True   #True
r2802 = False and True  #False
r2803 = 1 == 1 and 2 == 1   #False
r2804 = "test" == "test"    #True
r2805 = 1 ==1 or 2!=1   #True
r2806 = True and 1 == 1 #True
r2807 = False and 0 != 0    #False
r2808 = True or 1 == 1  #True
r2809 = "test" == "testing" #False
r2810 = 1 != 0 and 2 == 1   #False
r2811 = "test" != "testing" #True
r2812 = "test" == 1     #False
r2813 = not (True and False)    #True
r2814 = not (1 == 1 and 0 != 1) #False
r2815 = not (10 == 1 or 1000 == 1000)   #False
r2816 = not (1 != 10 or 3 == 4) #False
r2817 = not ("testing" == "testing" and "Zed" == "Cool guy")    #True
r2818 = 1 == 1 and (not ("testing" == 1 or 1 == 0)) #True
r2819 = "chunky" == "bacon" and (not (3 == 4 or 3 == 3))    #False
r2820 = 3 == 3 and (not ("testing" == "testing" or "Python" == "Python"))   #False

print r2801, r2802, r2803, r2804, r2805, r2806, r2807, r2808, r2809, r2810
print r2811, r2812, r2813, r2814, r2815, r2816, r2817, r2818, r2819, r2820

#actually just add print in front of each line of boolean equation is ok, before adding r28**

#varation of #20:
print 3 != 4 and not ("testing" != "test" or "Python" == "python")  #False

#Common Students Questions 1
print True and 1
print False and 0
print True and 0
print False or 1
print True or "testing"
print "test" and "testing"
print 1 or True
print "test" and "testing"
print "test" and not "testing"
